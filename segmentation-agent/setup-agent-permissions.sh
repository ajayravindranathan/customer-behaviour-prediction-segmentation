#!/bin/bash

set -e

# Execution role name - must be provided via environment variable or command line
EXECUTION_ROLE_NAME=${EXECUTION_ROLE_NAME:-""}

if [ -z "$EXECUTION_ROLE_NAME" ]; then
    echo "❌ Error: EXECUTION_ROLE_NAME not set"
    echo "   Usage: export EXECUTION_ROLE_NAME='your-role-name' && ./setup-agent-permissions.sh"
    exit 1
fi

# Load .env if it exists
if [ -f .env ]; then
    source .env
fi

# Configuration - can be overridden with environment variables
S3_BUCKET=${S3_BUCKET:-"your-customer-data-bucket"}

POLICY_NAME="CustomerSegmentationAgentPolicy"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

echo "Setting up permissions for existing role: $EXECUTION_ROLE_NAME"
echo "Using S3 bucket: $S3_BUCKET"

# Consolidated policy with all required permissions
cat > agent-policy.json << EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "arn:aws:bedrock:*::foundation-model/*"
        },
        {
            "Effect": "Allow",
            "Action": "bedrock-agentcore:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::${S3_BUCKET}",
                "arn:aws:s3:::${S3_BUCKET}/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::*:role/*CodeInterpreter*"
        }
    ]
}
EOF

# Create or update policy
POLICY_ARN="arn:aws:iam::$ACCOUNT_ID:policy/$POLICY_NAME"
if aws iam get-policy --policy-arn $POLICY_ARN >/dev/null 2>&1; then
    aws iam create-policy-version --policy-arn $POLICY_ARN --policy-document file://agent-policy.json --set-as-default
else
    aws iam create-policy --policy-name $POLICY_NAME --policy-document file://agent-policy.json
fi

# Attach policy to existing role
aws iam attach-role-policy --role-name $EXECUTION_ROLE_NAME --policy-arn $POLICY_ARN

rm agent-policy.json
echo "✅ Permissions attached to role: $EXECUTION_ROLE_NAME"
