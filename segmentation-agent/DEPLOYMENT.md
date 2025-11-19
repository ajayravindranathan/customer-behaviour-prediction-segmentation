# Deployment Guide

## Prerequisites
- AWS CLI configured with appropriate permissions
- Python 3.11+
- AgentCore CLI installed (`pip install bedrock-agentcore`)

## Configuration

### 1. Environment Variables
Copy `.env.template` to `.env` and update values:
```bash
cp .env.template .env
```

Required variables:
- `AWS_REGION`: AWS region for deployment (e.g., us-east-1)
- `S3_BUCKET`: S3 bucket name containing customer data
- `S3_KEY`: Path to CSV file in S3 bucket

### 2. Setup Permissions
Update the execution role name in `setup-agent-permissions.sh`:
```bash
EXECUTION_ROLE_NAME="your-agentcore-execution-role"
```

Set S3 bucket and run:
```bash
export S3_BUCKET=your-customer-data-bucket
./setup-agent-permissions.sh
```

### 3. Deploy Agent
```bash
# Load environment variables
source .env

# Configure agent
agentcore configure -e segmentation_agent.py

# Deploy to AWS
agentcore launch
```

### 4. Test Agent
```bash
# Test with sample payload
agentcore invoke '{"prompt": "Show me the first 10 rows of customer data"}'
```

### 5. Run Webapp (Optional)
```bash
cd webapp
export AWS_REGION=us-east-1
export S3_BUCKET=your-customer-data-bucket
export S3_KEY=data/customer_data.csv
./run.sh
```

## Fresh Account Deployment Checklist
- [ ] Create S3 bucket for customer data
- [ ] Upload customer data CSV to S3
- [ ] Update `.env` with your values
- [ ] Update execution role name in setup script
- [ ] Run setup-agent-permissions.sh
- [ ] Configure agent: `agentcore configure -e segmentation_agent.py`
- [ ] Deploy agent: `agentcore launch`
- [ ] Test agent with sample invocation

## Useful Commands
```bash
# Check agent status
agentcore status

# List configured agents
agentcore configure list

# Destroy agent resources
agentcore destroy

# View agent logs
aws logs tail /aws/bedrock-agentcore/runtime/your-agent-name --follow
```
