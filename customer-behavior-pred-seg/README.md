# Customer Behaviour Prediction Agent

An AI-powered agent for automating customer migration related propensity analysis and feature engineering, designed to deploy on any fresh AWS account.

## Overview

This agent automates:
- Exploring customer data from S3
- Generating predictive features using AI
- Creating feature engineering pipelines with AWS Glue
- Training migration propensity models with SageMaker/AutoGluon

## Architecture

- **Runtime**: Amazon Bedrock AgentCore
- **Framework**: Strands Agents
- **Interface**: Streamlit web app
- **Processing**: AWS Glue, S3, SageMaker, AutoGluon Cloud
- **Region**: us-east-1 (configurable)

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

### Step 1: Deploy the Agent

This makes the code portable and deploys to Bedrock AgentCore:

```bash
chmod +x deploy.sh
./deploy.sh
```

This will:
1. Remove all hardcoded account IDs and regions
2. Install dependencies
3. Deploy agent to Bedrock AgentCore
4. Save agent ARN to `.env` file

**Note**: Deployment takes 5-10 minutes.

### Step 2: Setup IAM Roles and Policies

This creates all necessary IAM roles, policies, and S3 buckets:

```bash
chmod +x setup_iam.sh
./setup_iam.sh
```

This will create:
- `FeatureEngineeringAgentPolicy` - Custom IAM policy with all required permissions
- `GlueServiceRole` - Service role for AWS Glue jobs
- `SageMakerExecutionRole` - Execution role for SageMaker training
- S3 bucket: `feature-engineering-{ACCOUNT_ID}` for Glue scripts
- Updates AgentCore role (if exists) with required permissions

### Step 3: Run the Web Interface

```bash
chmod +x run_webapp.sh
./run_webapp.sh
```

Access the webapp at: http://localhost:8501

## Files

### Core Files
- `enhanced_feature_agent.py` - Main agent with tools for feature engineering
- `webapp.py` - Streamlit web interface
- `requirements.txt` - Agent dependencies
- `webapp_requirements.txt` - Webapp dependencies

### Deployment Files
- `.bedrock_agentcore.yaml.template` - AgentCore configuration template
- `iam-policy.json` - Portable IAM policy (no hardcoded accounts)
- `setup_iam.sh` - IAM setup script
- `deploy.sh` - Agent deployment script
- `run_webapp.sh` - Webapp launcher
- `make_portable.py` - Script to remove hardcoded values

### Generated Files
- `.bedrock_agentcore.yaml` - Generated during deployment
- `.env` - Environment variables (AGENT_ARN, AWS_REGION, etc.)

## Configuration

All configuration is dynamic and determined at deployment time:

- **AWS Region**: Set via `AWS_REGION` environment variable (default: us-east-1)
- **AWS Account**: Automatically detected via AWS CLI
- **Agent ARN**: Generated during deployment and saved to `.env`
- **S3 Buckets**: Created with account-specific names

## Manual Configuration (Optional)

If you need to set environment variables manually:

```bash
export AWS_REGION=us-east-1
export AGENT_ARN='arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/enhanced_feature_agent-xxxxx'
export GLUE_SCRIPT_BUCKET='feature-engineering-123456789012'
```

## Usage

### 1. Data Exploration
Point the agent to your S3 customer data:
```
Explore data at s3://my-bucket/customer-data/
```

### 2. Feature Generation
Let AI suggest features:
```
Generate feature suggestions using LLM
```

### 3. Add Custom Features
Suggest your own features during conversation:
```
Add feature: customer_tenure_months = days_since_signup / 30
```

### 4. Create Feature Pipeline
Confirm features and create Glue job:
```
Confirm final feature list and create Glue job outputting to s3://my-bucket/features/
```

### 5. Train Models
Train propensity models:
```
Train churn propensity model using features from s3://my-bucket/features/
```

## Propensity Models

The agent supports three migration propensity models:

1. **Call Propensity**: Likelihood of customers contacting support post-migration
2. **Churn Propensity**: Likelihood of customers canceling service post-migration
3. **Spend Change Propensity**: Likelihood of spending pattern changes post-migration

## IAM Permissions

The deployment creates roles with permissions for:

- ✅ S3 (read/write/delete)
- ✅ AWS Glue (jobs/databases/tables)
- ✅ SageMaker (training/inference)
- ✅ Bedrock (model invocation)
- ✅ CloudWatch Logs
- ✅ ECR (container access)
- ✅ VPC (networking)

## Troubleshooting

### IAM Role Not Found
```bash
# Re-run IAM setup after deployment
./setup_iam.sh
```

### Agent ARN Not Set
```bash
# Check .env file
cat .env

# Or manually set
export AGENT_ARN='your-agent-arn'
```

### Deployment Fails
```bash
# Check AWS credentials
aws sts get-caller-identity

# Check region
echo $AWS_REGION

# Verify IAM roles exist
aws iam get-role --role-name GlueServiceRole
```

### Webapp Connection Error
```bash
# Verify agent is deployed
agentcore list

# Check agent status
agentcore status enhanced_feature_agent
```

## Development

### Local Testing
```bash
# Activate virtual environment
source venv/bin/activate

# Run agent locally (for testing)
python enhanced_feature_agent.py
```

### Update Agent
```bash
# Make changes to enhanced_feature_agent.py
# Then redeploy
./deploy.sh
```

### View Logs
```bash
# View agent logs
agentcore logs enhanced_feature_agent

# Follow logs in real-time
agentcore logs enhanced_feature_agent --follow
```

## Clean Up

To remove all resources:

```bash
# Delete agent
agentcore destroy

# Delete IAM roles (manual)
aws iam delete-role --role-name GlueServiceRole
aws iam delete-role --role-name SageMakerExecutionRole

# Delete IAM policy
aws iam delete-policy --policy-arn arn:aws:iam::ACCOUNT_ID:policy/FeatureEngineeringAgentPolicy

# Delete S3 bucket
aws s3 rb s3://feature-engineering-ACCOUNT_ID --force
```

## Key Improvements for Fresh Account Deployment

1. ✅ **No Hardcoded Account IDs**: All account IDs dynamically detected
2. ✅ **No Hardcoded Regions**: Region configurable via environment variable
3. ✅ **No Hardcoded ARNs**: All ARNs constructed dynamically
4. ✅ **Portable IAM Policies**: Wildcards and dynamic role references
5. ✅ **Auto-Created Resources**: S3 buckets, roles, policies created automatically
6. ✅ **Environment-Based Config**: All config via environment variables
7. ✅ **Single-Command Deployment**: `./deploy.sh && ./setup_iam.sh`

## Support

For issues or questions:
1. Check CloudWatch Logs for agent errors
2. Verify IAM permissions are correctly set
3. Ensure AWS CLI is configured with correct credentials
4. Check that all required AWS services are available in your region
