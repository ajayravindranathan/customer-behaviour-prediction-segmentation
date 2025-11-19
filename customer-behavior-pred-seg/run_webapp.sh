#!/bin/bash

echo "🌐 Starting Feature Engineering Agent Web Interface"
echo "=================================================="

# Load environment variables from .env if it exists
if [ -f ".env" ]; then
    echo "📋 Loading environment variables from .env..."
    export $(cat .env | grep -v '^#' | xargs)
    echo "   ✅ Environment loaded"
else
    echo "⚠️  .env file not found"
fi

# Check required environment variables
if [ -z "$AGENT_ARN" ]; then
    echo ""
    echo "❌ AGENT_ARN environment variable not set"
    echo ""
    echo "Please set it manually:"
    echo "   export AGENT_ARN='arn:aws:bedrock-agentcore:REGION:ACCOUNT:runtime/enhanced_feature_agent-xxxxx'"
    echo ""
    echo "Or run ./deploy.sh to deploy the agent first"
    exit 1
fi

AWS_REGION=${AWS_REGION:-us-east-1}

echo ""
echo "📍 Configuration:"
echo "   AWS Region: $AWS_REGION"
echo "   Agent ARN: $AGENT_ARN"
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install webapp dependencies if needed
if ! python3 -c "import streamlit" &>/dev/null; then
    echo "📦 Installing webapp dependencies..."
    pip install -q -r webapp_requirements.txt
fi

echo "🚀 Starting Streamlit webapp..."
echo "   Access the webapp at: http://localhost:8501"
echo ""
echo "   Press Ctrl+C to stop"
echo ""

streamlit run webapp.py
