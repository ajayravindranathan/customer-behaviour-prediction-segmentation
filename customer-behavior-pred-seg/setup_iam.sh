#!/bin/bash
set -e


# Setup IAM roles and policies for Feature Engineering Agent
# This script is portable and works on any fresh AWS account

echo "🚀 Setting up IAM roles and policies for Feature Engineering Agent"
echo "=================================================="

# Get AWS account ID and region
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=${AWS_REGION:-us-east-1}

echo "📍 AWS Account: $AWS_ACCOUNT_ID"
echo "📍 AWS Region: $AWS_REGION"
echo ""

# Check if agent has been deployed
echo "1️⃣  Checking agent deployment..."
if [ ! -f ".bedrock_agentcore.yaml" ]; then
    echo "   ⚠️  Agent not deployed. Please run ./deploy.sh first"
    exit 1
fi
echo "   ✅ Agent deployment verified"
echo ""

# Policy and role names
POLICY_NAME="FeatureEngineeringAgentPolicy"
GLUE_ROLE_NAME="GlueServiceRole"
SAGEMAKER_ROLE_NAME="SageMakerExecutionRole"

# Step 2: Create the custom IAM policy
echo "2️⃣  Creating IAM policy: $POLICY_NAME"
POLICY_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:policy/$POLICY_NAME"

if aws iam get-policy --policy-arn "$POLICY_ARN" &>/dev/null; then
    echo "   ℹ️  Policy already exists, skipping creation"
else
    aws iam create-policy \
        --policy-name "$POLICY_NAME" \
        --policy-document file://iam-policy.json \
        --description "Comprehensive permissions for Feature Engineering Agent" \
        --region "$AWS_REGION"
    echo "   ✅ Policy created: $POLICY_ARN"
fi
echo ""

# Step 3: Create Glue service role
echo "3️⃣  Creating Glue service role: $GLUE_ROLE_NAME"

if aws iam get-role --role-name "$GLUE_ROLE_NAME" &>/dev/null; then
    echo "   ℹ️  Glue role already exists, skipping creation"
else
    # Create trust policy for Glue
    cat > /tmp/glue-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

    aws iam create-role \
        --role-name "$GLUE_ROLE_NAME" \
        --assume-role-policy-document file:///tmp/glue-trust-policy.json \
        --description "Service role for AWS Glue feature engineering jobs" \
        --region "$AWS_REGION"
    
    echo "   ✅ Glue role created"
    rm -f /tmp/glue-trust-policy.json
fi

# Attach policies to Glue role
echo "   📎 Attaching policies to Glue role..."
aws iam attach-role-policy --role-name "$GLUE_ROLE_NAME" --policy-arn "$POLICY_ARN" 2>/dev/null || true
aws iam attach-role-policy --role-name "$GLUE_ROLE_NAME" --policy-arn "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole" 2>/dev/null || true
echo "   ✅ Policies attached to Glue role"
echo ""

# Step 4: Create SageMaker execution role
echo "4️⃣  Creating SageMaker execution role: $SAGEMAKER_ROLE_NAME"

if aws iam get-role --role-name "$SAGEMAKER_ROLE_NAME" &>/dev/null; then
    echo "   ℹ️  SageMaker role already exists, skipping creation"
else
    # Create trust policy for SageMaker
    cat > /tmp/sagemaker-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

    aws iam create-role \
        --role-name "$SAGEMAKER_ROLE_NAME" \
        --assume-role-policy-document file:///tmp/sagemaker-trust-policy.json \
        --description "Execution role for SageMaker training jobs" \
        --region "$AWS_REGION"
    
    echo "   ✅ SageMaker role created"
    rm -f /tmp/sagemaker-trust-policy.json
fi

# Attach policies to SageMaker role
echo "   📎 Attaching policies to SageMaker role..."
aws iam attach-role-policy --role-name "$SAGEMAKER_ROLE_NAME" --policy-arn "$POLICY_ARN" 2>/dev/null || true
aws iam attach-role-policy --role-name "$SAGEMAKER_ROLE_NAME" --policy-arn "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess" 2>/dev/null || true
echo "   ✅ Policies attached to SageMaker role"
echo ""

# Step 5: Update AgentCore role (if it exists)
echo "5️⃣  Checking for AgentCore runtime role..."
AGENTCORE_ROLE_NAME="AmazonBedrockAgentCoreSDKRuntime-${AWS_REGION}"

# Find the actual AgentCore role (it has a suffix)
AGENTCORE_ROLE=$(aws iam list-roles --query "Roles[?starts_with(RoleName, '$AGENTCORE_ROLE_NAME')].RoleName" --output text | head -1)

if [ -n "$AGENTCORE_ROLE" ]; then
    echo "   ℹ️  Found AgentCore role: $AGENTCORE_ROLE"
    echo "   📎 Attaching policies to AgentCore role..."
    
    aws iam attach-role-policy --role-name "$AGENTCORE_ROLE" --policy-arn "$POLICY_ARN" 2>/dev/null || true
    aws iam attach-role-policy --role-name "$AGENTCORE_ROLE" --policy-arn "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess" 2>/dev/null || true
    
    # Update trust policy to include SageMaker
    cat > /tmp/agentcore-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "bedrock-agentcore.amazonaws.com",
          "sagemaker.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
    
    aws iam update-assume-role-policy \
        --role-name "$AGENTCORE_ROLE" \
        --policy-document file:///tmp/agentcore-trust-policy.json 2>/dev/null || true
    
    rm -f /tmp/agentcore-trust-policy.json
    echo "   ✅ AgentCore role updated"
else
    echo "   ℹ️  AgentCore role not found (will be created during agent deployment)"
fi
echo ""

# Step 6: Deploy AWS Marketplace policies
echo "6️⃣  Deploying AWS Marketplace policies..."
echo "   📋 Marketplace permissions included in policy:"
echo "      • aws-marketplace:ViewSubscriptions"
echo "      • aws-marketplace:Subscribe"
echo "   ✅ Marketplace policies deployed with IAM policy"
echo ""

# Step 7: Create S3 bucket for Glue scripts
GLUE_SCRIPT_BUCKET="feature-engineering-${AWS_ACCOUNT_ID}"
echo "7️⃣  Creating S3 bucket for Glue scripts: $GLUE_SCRIPT_BUCKET"

if aws s3 ls "s3://$GLUE_SCRIPT_BUCKET" &>/dev/null; then
    echo "   ℹ️  Bucket already exists"
else
    if [ "$AWS_REGION" = "us-east-1" ]; then
        aws s3 mb "s3://$GLUE_SCRIPT_BUCKET" --region "$AWS_REGION"
    else
        aws s3 mb "s3://$GLUE_SCRIPT_BUCKET" --region "$AWS_REGION" --create-bucket-configuration LocationConstraint="$AWS_REGION"
    fi
    echo "   ✅ S3 bucket created"
fi
echo ""

# Summary
echo "=================================================="
echo "✅ IAM Setup Complete!"
echo ""
echo "🚨 CRITICAL WARNING:"
echo "   The webapp WILL NOT work for 15 minutes after this deployment"
echo "   due to AWS IAM policy propagation delays. DO NOT test until then."
echo ""
echo "📋 Summary:"
echo "   • Policy: $POLICY_ARN"
echo "   • Glue Role: arn:aws:iam::$AWS_ACCOUNT_ID:role/$GLUE_ROLE_NAME"
echo "   • SageMaker Role: arn:aws:iam::$AWS_ACCOUNT_ID:role/$SAGEMAKER_ROLE_NAME"
echo "   • S3 Bucket: s3://$GLUE_SCRIPT_BUCKET"
if [ -n "$AGENTCORE_ROLE" ]; then
    echo "   • AgentCore Role: arn:aws:iam::$AWS_ACCOUNT_ID:role/$AGENTCORE_ROLE"
fi
echo ""
echo "🎯 Next Steps:"
echo "   1. Run: ./deploy.sh"
echo "   2. After deployment, run: ./run_webapp.sh"
echo ""
echo "💡 Environment variables to set:"
echo "   export AWS_REGION=$AWS_REGION"
echo "   export GLUE_SCRIPT_BUCKET=$GLUE_SCRIPT_BUCKET"
