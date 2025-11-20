# 🔍 Customer Behavior Segmentation Agent

An AI-powered customer segmentation agent built with Amazon Bedrock AgentCore that analyzes customer data from S3 and provides intelligent insights using code interpretation capabilities.

> **Part of the [Customer Behavior Prediction & Segmentation](../README.md) platform**

**✅ Fully Portable** - Deploy to any AWS account and region with zero hardcoded values

## Overview

This agent provides:
- **Interactive Customer Analysis**: AI-powered data exploration and insights
- **Intelligent Segmentation**: Automated customer grouping based on behavior patterns  
- **Code Interpretation**: Advanced analytics with secure Python execution
- **S3 Integration**: Seamless data storage and retrieval
- **Web Interface**: User-friendly interface for data analysis

## Architecture

- **Runtime**: Amazon Bedrock AgentCore
- **Framework**: Strands Agents  
- **Interface**: Streamlit web app
- **Processing**: AgentCore Code Interpreter, S3
- **Region**: Configurable (defaults to us-east-1)

## Prerequisites

1. **AWS Account** with appropriate permissions
2. **AWS CLI** configured with credentials  
3. **Python 3.11+** installed
4. **Docker** (for AgentCore deployment)
5. **Bedrock AgentCore CLI** installed:
   ```bash
   pip install bedrock-agentcore
   ```

## Quick Start (Fresh AWS Account)

### Step 1: Setup Environment
```bash
# Configure AWS region (optional, defaults to us-east-1)
export AWS_REGION=us-east-1

# Copy and configure environment template
cp .env.template .env
# Edit .env with your S3 bucket and data path
```

### Step 2: Deploy the Agent
```bash
chmod +x deploy.sh
./deploy.sh
```

This will:
1. Install dependencies
2. Deploy agent to Bedrock AgentCore  
3. Setup IAM permissions automatically
4. Save agent ARN to `.env` file

**Note**: Deployment takes 5-10 minutes.

### Step 3: Test the Agent
```bash
agentcore invoke '{"prompt": "Show me the first 10 rows of customer data"}'
```

## Configuration

Edit `.env` file with your specific values:

```bash
# AWS Configuration
AWS_REGION=us-east-1
S3_BUCKET=my-customer-analytics-bucket-2024
S3_KEY=datasets/customer_behavior_data.csv

# Optional: Override default model
# MODEL_ID=us.anthropic.claude-3-7-sonnet-20250219-v1:0
```

### Example Values

**S3_BUCKET examples**:
- `customer-data-analytics-prod`
- `bt-customer-segmentation-2024`
- `telecom-behavior-analysis-bucket`

**S3_KEY examples**:
- `data/customer_data.csv`
- `datasets/2024/customer_behavior.csv`
- `raw-data/telecom_customers.csv`
- `analytics/customer_segments_input.csv`

## Manual Deployment Steps

If you prefer manual deployment or need to troubleshoot:

### 1. Initial Agent Deployment
```bash
source .env
agentcore configure -e segmentation_agent.py
agentcore launch
```

Note the execution role name from the output (e.g., `BedrockAgentCoreExecutionRole-xyz123`).

### 2. Setup S3 Permissions
```bash
export EXECUTION_ROLE_NAME="BedrockAgentCoreExecutionRole-xyz123"  # Use actual role from step 1
export S3_BUCKET="your-bucket-name"  # Or it will use value from .env
./setup-agent-permissions.sh
```

### 3. Run Web Interface (Optional)
```bash
cd webapp
./run.sh  # Uses environment variables from .env
```

## Project Structure

```
├── segmentation_agent.py      # Main agent implementation
├── setup-agent-permissions.sh # AWS permissions setup script
├── deploy.sh                  # Automated deployment script
├── .env.template              # Environment configuration template
├── requirements.txt           # Python dependencies
├── iam-policy.json           # IAM policy template
└── webapp/                   # Web interface
    ├── app.py
    ├── run.sh
    └── templates/
```

## Usage Examples

### Basic Customer Analysis
```bash
agentcore invoke '{"prompt": "Analyze customer demographics and show key insights"}'
```

### Segmentation Analysis
```bash
agentcore invoke '{"prompt": "Create customer segments based on behavior patterns and visualize the results"}'
```

### Data Exploration
```bash
agentcore invoke '{"prompt": "Show data quality metrics and missing value analysis"}'
```

## Troubleshooting

### Common Issues

**Permission Errors**: Ensure your execution role has the required permissions by running `./setup-agent-permissions.sh` with the correct role name.

**S3 Access Issues**: Verify your S3 bucket and key exist and are accessible from your AWS account.

**Agent Not Found**: Run `agentcore configure list` to see configured agents.

### Useful Commands

```bash
# Check agent status
agentcore status

# View agent logs
aws logs tail /aws/bedrock-agentcore/runtime/your-agent-name --follow

# Destroy agent resources
agentcore destroy

# List all configured agents
agentcore configure list
```

## Data Requirements

Your S3 CSV file should contain customer data with columns such as:
- Customer ID
- Demographics (age, gender, location)
- Behavioral metrics (purchase history, engagement)
- Transaction data
- Any other relevant customer attributes

The agent will automatically analyze the data structure and provide appropriate insights.

## Security

- All data processing happens within AWS secure environments
- S3 access is restricted to specified buckets only
- Agent execution uses least-privilege IAM roles
- No customer data is stored permanently in the agent

## Support

For issues related to:
- **AgentCore**: Check [AgentCore documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)
- **AWS Permissions**: Review IAM policies in `setup-agent-permissions.sh`
- **Data Issues**: Verify S3 bucket access and CSV format
