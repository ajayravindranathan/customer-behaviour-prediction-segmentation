#!/bin/bash
set -e

echo "🚀 Deploying Feature Engineering Agent to AWS"
echo "=================================================="

# Get AWS account ID and region
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=${AWS_REGION:-us-east-1}

echo "📍 AWS Account: $AWS_ACCOUNT_ID"
echo "📍 AWS Region: $AWS_REGION"
echo ""

# Step 1: Make code portable
echo "1️⃣  Making code portable..."
python3 make_portable.py
echo ""

# Step 2: Check for required files
echo "2️⃣  Checking required files..."
REQUIRED_FILES=("enhanced_feature_agent.py" "requirements.txt")
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "   ❌ Missing required file: $file"
        exit 1
    fi
    echo "   ✅ $file"
done
echo ""

# Step 3: Set up environment variables
export AWS_REGION="$AWS_REGION"
export GLUE_SCRIPT_BUCKET="feature-engineering-${AWS_ACCOUNT_ID}"

echo "3️⃣  Environment variables:"
echo "   AWS_REGION=$AWS_REGION"
echo "   GLUE_SCRIPT_BUCKET=$GLUE_SCRIPT_BUCKET"
echo ""

# Step 4: Install dependencies
echo "4️⃣  Installing dependencies..."
pip install --upgrade pip

# Install with compatibility constraints
pip install -r dev_requirements.txt
pip install "bedrock-agentcore-starter-toolkit>=0.1.21"
echo "   ✅ Dependencies installed"
echo ""

# Step 5: Configure agent (interactive)
echo "5️⃣  Configuring agent with agentcore configure..."
echo ""
echo "   📝 When prompted:"
echo "      • Execution Role: Press ENTER to auto-create"
echo "      • ECR Repository: Press ENTER to auto-create"
echo "      • Requirements File: Press ENTER to use requirements.txt"
echo "      • OAuth: Type 'no'"
echo "      • Request Headers: Type 'no'"
echo "      • Memory: Type 's' to skip"
echo ""
read -p "Press ENTER to continue with configuration..."

agentcore configure -e enhanced_feature_agent.py

echo ""
echo "   ✅ Configuration complete"
echo ""

# Step 6: Deploy agent
echo "6️⃣  Deploying agent to Bedrock AgentCore..."
echo "   Using remote container build via CodeBuild..."
echo "   This may take 5-10 minutes..."
echo ""

agentcore launch

echo ""
echo "=================================================="
echo "✅ Deployment Complete!"
echo ""

# Step 7: Get agent ARN
echo "7️⃣  Retrieving agent information..."
if [ -f ".bedrock_agentcore.yaml" ]; then
    AGENT_ARN=$(grep "agent_arn:" .bedrock_agentcore.yaml | head -1 | awk '{print $2}')
    if [ -n "$AGENT_ARN" ]; then
        echo ""
        echo "📋 Agent Details:"
        echo "   Agent ARN: $AGENT_ARN"
        echo ""
        
        # Save to .env file
        echo "AWS_REGION=$AWS_REGION" > .env
        echo "AGENT_ARN=$AGENT_ARN" >> .env
        echo "GLUE_SCRIPT_BUCKET=$GLUE_SCRIPT_BUCKET" >> .env
        echo ""
        echo "   ✅ Environment variables saved to .env file"
        echo ""
        echo "💡 To run the webapp:"
        echo "   ./run_webapp.sh"
    fi
fi

echo ""
echo "🎉 Deployment successful!"
