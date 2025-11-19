#!/bin/bash

set -e

echo "🚀 Starting Customer Segmentation Agent Deployment"

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found. Please copy .env.template to .env and configure it."
    exit 1
fi

# Load environment variables
source .env

# Validate required variables
if [ -z "$AWS_REGION" ] || [ -z "$S3_BUCKET" ] || [ -z "$S3_KEY" ]; then
    echo "❌ Error: Missing required environment variables in .env"
    echo "   Required: AWS_REGION, S3_BUCKET, S3_KEY"
    exit 1
fi

echo "📋 Configuration:"
echo "   AWS Region: $AWS_REGION"
echo "   S3 Bucket: $S3_BUCKET"
echo "   S3 Key: $S3_KEY"

# Step 1: Configure and launch agent
echo ""
echo "📦 Step 1: Configuring and launching agent..."
agentcore configure -e segmentation_agent.py
agentcore launch

# Step 2: Extract execution role name
echo ""
echo "🔍 Step 2: Extracting execution role name..."
EXECUTION_ROLE_ARN=$(agentcore status --verbose | grep -o '"execution_role": "[^"]*"' | cut -d'"' -f4)

if [ -z "$EXECUTION_ROLE_ARN" ] || [ "$EXECUTION_ROLE_ARN" = "null" ]; then
    echo "⚠️  Warning: Could not automatically extract execution role ARN."
    echo "   Please run manually:"
    echo "   export EXECUTION_ROLE_NAME='your-role-name'"
    echo "   ./setup-agent-permissions.sh"
    exit 1
fi

# Extract role name from ARN (arn:aws:iam::account:role/RoleName -> RoleName)
EXECUTION_ROLE_NAME=$(echo "$EXECUTION_ROLE_ARN" | cut -d'/' -f2)

echo "   Found role ARN: $EXECUTION_ROLE_ARN"
echo "   Role name: $EXECUTION_ROLE_NAME"

# Step 3: Setup permissions
echo ""
echo "🔐 Step 3: Setting up S3 permissions..."
export EXECUTION_ROLE_NAME
export S3_BUCKET
./setup-agent-permissions.sh

echo ""
echo "✅ Deployment complete!"
echo ""
echo "🧪 Test your agent with:"
echo "   agentcore invoke '{\"prompt\": \"Show me the first 10 rows of customer data\"}'"
echo ""
echo "🌐 Run web interface (optional):"
echo "   cd webapp && ./run.sh"
