# 🎯 Customer Behavior Prediction & Segmentation

<div align="center">

![Customer Behavior Analytics](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge)
![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock_AgentCore-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge)

*AI-powered customer analytics platform for predicting behavior patterns and intelligent segmentation using Amazon Bedrock AgentCore*

**✅ Fully Portable** - Deploy to any AWS account and region with zero hardcoded values

</div>

---

## 📋 Overview

This repository contains two powerful AI agents built on Amazon Bedrock AgentCore that analyze customer data, predict behavior patterns, and provide actionable insights:

- **⚙️ Customer Behaviour Prediction Agent**: Automated ML pipeline for migration propensity prediction
- **🔍 Segmentation Agent**: Interactive customer analysis and segmentation

Both agents leverage Claude models powered by Amazon Bedrock for intelligent data analysis, feature generation, and predictive modeling.

## ⚠️ Portability Guarantee

This repository is **100% portable** across AWS accounts and regions:
- ✅ No hardcoded AWS account IDs
- ✅ No hardcoded regions (except as configurable defaults)
- ✅ No hardcoded S3 bucket names
- ✅ No hardcoded ARNs or absolute paths
- ✅ All values derived dynamically at deployment time
- ✅ `.env` and `.bedrock_agentcore.yaml` files excluded from git (generated locally)

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      Amazon Bedrock AgentCore                           │
├─────────────────────────────┬───────────────────────────────────────────┤
│  Customer Behaviour Prediction  │      Segmentation Agent               │
│  • Feature Generation           │      • Data Analysis                  │
│  • Glue ETL Pipelines           │      • Visualization                  │
│  • SageMaker Training           │      • Interactive Insights           │
│  • Propensity Modeling          │      • Code Interpretation            │
└─────────────────────────────┴───────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          AWS Services Layer                             │
├──────────────┬──────────────┬──────────────────┬────────────────────────┤
│  Amazon S3   │  AWS Glue    │  SageMaker       │  Amazon Bedrock        │
│  Data Lake   │  ETL Jobs    │  ML Training     │  Claude Models         │
└──────────────┴──────────────┴──────────────────┴────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                           Predictive Outcomes                           │
├──────────────┬──────────────┬──────────────────┬────────────────────────┤
│ Post Migr.   │ Post Migr.   │  Spend Change    │  Customer Segment      │
│ Call Predict │ Churn Predict│  Prediction      │  Analysis              │
└──────────────┴──────────────┴──────────────────┴────────────────────────┘
```

## 📦 Prerequisites

Before deploying, ensure you have:

1. **AWS Account** with appropriate permissions
2. **AWS CLI** installed and configured:
   ```bash
   aws configure
   ```
3. **Python 3.11+** installed
4. **Docker** installed (for AgentCore container builds)
5. **Bedrock AgentCore CLI** installed:
   ```bash
   pip install bedrock-agentcore-starter-toolkit
   ```
6. **Bedrock Model Access** enabled:
   - Go to AWS Console → Amazon Bedrock → Model Access
   - Enable Claude 3.5 Sonnet and Claude 3.7 Sonnet models

---

## 🚀 Deployment Guide

Choose which agent to deploy:

---

## 🔍 Option A: Segmentation Agent (Simpler Setup)

The Segmentation Agent provides interactive customer data analysis and visualization.

### Step 1: Prepare Configuration

```bash
cd segmentation-agent
cp .env.template .env
```

Edit `.env`:

```bash
# Required: Your AWS region
AWS_REGION=us-east-1

# Required: S3 bucket containing customer data
S3_BUCKET=my-customer-data-bucket

# Required: Path to CSV file in bucket
S3_KEY=data/customer_data.csv

# Optional: Override default model
# MODEL_ID=us.anthropic.claude-3-7-sonnet-20250219-v1:0
```

### Step 2: Create S3 Bucket and Upload Data

```bash
# Set region
export AWS_REGION=us-east-1

# Create bucket
aws s3 mb s3://my-customer-data-bucket --region $AWS_REGION

# Generate sample data (optional)
cd ../data
export S3_BUCKET=my-customer-data-bucket
python3 generate_customer_data.py
cd ../segmentation-agent
```

### Step 3: Deploy

```bash
./deploy.sh
```

This will:
1. Validate `.env` configuration
2. Run `agentcore configure` and `agentcore launch`
3. Create IAM role automatically
4. Attach S3 permissions

**Expected output:**
```
✅ Deployment complete!

🧪 Test: agentcore invoke '{"prompt": "Show me the first 10 rows"}'
🌐 Web UI: cd webapp && ./run.sh
```

### Step 4: Test

```bash
# CLI test
agentcore invoke '{"prompt": "Show me the first 10 rows of customer data"}'

# Web interface
cd webapp && ./run.sh
# Open http://localhost:8501
```

---

## ⚙️ Option B: Customer Behavior Prediction Agent (Full ML Pipeline)

### ⚠️ CRITICAL: Deployment Order

**You MUST follow this exact sequence:**

1. **FIRST**: `./deploy.sh` (creates agent and IAM role)
2. **WAIT**: 15 minutes for IAM propagation
3. **THEN**: `./setup_iam.sh` (attaches Glue/SageMaker policies)
4. **WAIT**: 15 minutes for policy propagation
5. **FINALLY**: Test the agent

### Step 1: Deploy Agent

```bash
cd customer-behavior-pred-seg
./deploy.sh
```

**Interactive prompts:**
```
When agentcore configure asks:
• Execution Role: Press ENTER (auto-create)
• ECR Repository: Press ENTER (auto-create)
• Requirements: Press ENTER (use requirements.txt)
• OAuth: Type 'no'
• Request Headers: Type 'no'
• Memory: Type 's' (skip)
```

This will:
1. Run `make_portable.py` to remove hardcoded values
2. Install dependencies
3. Run `agentcore configure` (creates agent config)
4. Run `agentcore launch` (deploys agent + creates IAM role)
5. Create `.env` with agent ARN

**Expected output:**
```
✅ Deployment Complete!

📋 Agent ARN: arn:aws:bedrock-agentcore:REGION:ACCOUNT:runtime/enhanced_feature_agent-xxxxx
✅ Environment variables saved to .env
```

### Step 2: ⏰ WAIT 15 Minutes

**Critical!** IAM roles need time to propagate.

```bash
echo "Waiting for IAM propagation..."
sleep 900  # 15 minutes
```

### Step 3: Setup IAM Permissions

```bash
./setup_iam.sh
```

This will:
1. Verify agent is deployed
2. Create `FeatureEngineeringAgentPolicy`
3. Create `GlueServiceRole` for ETL
4. Create `SageMakerExecutionRole` for training
5. Attach policies to AgentCore role
6. Create S3 bucket: `feature-engineering-{ACCOUNT_ID}`

**Expected output:**
```
✅ IAM Setup Complete!

🚨 CRITICAL: Wait 15 minutes before testing!

📋 Summary:
   • Policy: arn:aws:iam::ACCOUNT:policy/FeatureEngineeringAgentPolicy
   • Glue Role: arn:aws:iam::ACCOUNT:role/GlueServiceRole
   • SageMaker Role: arn:aws:iam::ACCOUNT:role/SageMakerExecutionRole
   • S3 Bucket: s3://feature-engineering-ACCOUNT
```

### Step 4: Generate Sample Data

Generate customer data and upload to S3:

```bash
cd ../data
export S3_BUCKET=feature-engineering-$(aws sts get-caller-identity --query Account --output text)
python3 generate_customer_data.py
cd ../customer-behavior-pred-seg
```

This will:
- Generate 10,000 synthetic customer records with realistic propensity patterns
- Upload data to `s3://feature-engineering-{ACCOUNT_ID}/raw-data/`
- Create timestamped CSV files to avoid conflicts

### Step 5: ⏰ WAIT Another 15 Minutes

Policy attachments also need propagation time.

```bash
sleep 900  # 15 minutes
```

### Step 6: Test Agent

```bash
# Run web interface
./run_webapp.sh
# Open http://localhost:8501

# Or test via CLI
agentcore invoke '{"prompt": "Explore data at s3://my-bucket/data/"}'
```

**Example workflows:**
```bash
# 1. Explore data
"Explore data at s3://my-bucket/customer-data/"

# 2. Generate features
"Generate features for churn prediction"

# 3. Create Glue ETL job
"Create Glue job to process features"

# 4. Train model
"Train churn propensity model using SageMaker"
```

---

## 📁 Repository Structure

```
.
├── README.md                        # This file
├── .gitignore                       # Excludes generated files
│
├── segmentation-agent/              # Interactive analysis agent
│   ├── .env.template                # Config template
│   ├── deploy.sh                    # Main deployment
│   ├── setup-agent-permissions.sh   # S3 permissions
│   ├── segmentation_agent.py        # Agent code
│   ├── iam-policy.json              # Policy template
│   └── webapp/                      # Web interface
│       ├── app.py
│       └── run.sh
│
├── customer-behavior-pred-seg/      # ML pipeline agent
│   ├── deploy.sh                    # Step 1: Deploy
│   ├── setup_iam.sh                 # Step 2: IAM setup
│   ├── enhanced_feature_agent.py    # Agent code
│   ├── make_portable.py             # Remove hardcoded values
│   ├── iam-policy.json              # Policy template
│   ├── webapp.py                    # Web interface
│   └── run_webapp.sh                # Launch webapp
│
└── data/                            # Sample data
    ├── generate_customer_data.py    # Data generator
    └── customer_propensity_data_*.csv
```

---

## 🔐 Security & IAM

### Segmentation Agent Permissions
- S3: Read/write to specified bucket
- Bedrock: Invoke Claude models
- Logs: CloudWatch logging
- Code Interpreter: Python execution

### Prediction Agent Permissions
- S3: Full access to feature-engineering bucket
- Glue: Create/run ETL jobs
- SageMaker: Create/run training jobs
- Bedrock: Invoke Claude models
- IAM: PassRole for Glue/SageMaker
- Logs: CloudWatch logging

All roles use **least-privilege** principles.

---

## 🧹 Cleanup

### Remove Segmentation Agent

```bash
cd segmentation-agent
agentcore delete
aws s3 rb s3://my-customer-data-bucket --force

ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws iam delete-policy --policy-arn arn:aws:iam::$ACCOUNT:policy/CustomerSegmentationAgentPolicy
```

### Remove Prediction Agent

```bash
cd customer-behavior-pred-seg
agentcore delete

ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws s3 rb s3://feature-engineering-$ACCOUNT --force

# Detach policies
aws iam detach-role-policy --role-name GlueServiceRole \
  --policy-arn arn:aws:iam::$ACCOUNT:policy/FeatureEngineeringAgentPolicy
aws iam detach-role-policy --role-name SageMakerExecutionRole \
  --policy-arn arn:aws:iam::$ACCOUNT:policy/FeatureEngineeringAgentPolicy

# Delete roles
aws iam delete-role --role-name GlueServiceRole
aws iam delete-role --role-name SageMakerExecutionRole

# Delete policy
aws iam delete-policy --policy-arn arn:aws:iam::$ACCOUNT:policy/FeatureEngineeringAgentPolicy
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Agentic AI** | Amazon Bedrock AgentCore |
| **LLM** | Claude 3.5 Sonnet, Claude 3.7 Sonnet |
| **ETL** | AWS Glue |
| **ML Training** | Amazon SageMaker + AutoGluon |
| **Storage** | Amazon S3 |
| **Interface** | Streamlit |
| **Language** | Python 3.11+ |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Permission Denied** | Wait 15 minutes for IAM propagation |
| **Bucket Not Found** | Create: `aws s3 mb s3://bucket-name --region $AWS_REGION` |
| **Model Access Denied** | Enable Bedrock models in AWS Console |
| **Agent Not Found** | Run: `agentcore status --verbose` |
| **Glue Job Failed** | Check CloudWatch: `/aws-glue/jobs/error` |
| **Wrong deployment order** | For Prediction Agent: deploy.sh FIRST, then setup_iam.sh |

### Segmentation Agent Issues

```bash
# Verify bucket access
aws s3 ls s3://my-customer-data-bucket/

# Re-attach S3 permissions
export S3_BUCKET=my-bucket
./setup-agent-permissions.sh

# Check agent status
agentcore status --verbose
```

### Prediction Agent Issues

```bash
# Verify IAM roles exist
aws iam get-role --role-name GlueServiceRole
aws iam get-role --role-name SageMakerExecutionRole

# Check S3 bucket
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws s3 ls s3://feature-engineering-$ACCOUNT/

# Verify agent deployment
agentcore status --verbose
cat .bedrock_agentcore.yaml
```

---

## ❓ FAQ

**Q: Can I deploy to any AWS region?**  
A: Yes! Set `AWS_REGION` before deployment. Ensure Bedrock is available in your region.

**Q: Do I need to modify code?**  
A: No. All configuration is via environment variables.

**Q: What if I already have IAM roles?**  
A: Scripts check for existing roles and skip creation.

**Q: Can I use my own S3 buckets?**  
A: Yes. Set `S3_BUCKET` in `.env` files.

**Q: Why the 15-minute waits?**  
A: AWS IAM changes take time to propagate globally. Skipping waits causes permission errors.

**Q: What's the deployment order for Prediction Agent?**  
A: **deploy.sh → wait 15min → setup_iam.sh → wait 15min → test**

**Q: Is my data secure?**  
A: Yes. All data stays in your AWS account.

---

## ✅ Portability Verification

This repository guarantees portability:

- ✅ **No hardcoded account IDs** - Derived via `aws sts get-caller-identity`
- ✅ **No hardcoded regions** - From `AWS_REGION` environment variable
- ✅ **No hardcoded buckets** - From `.env` or dynamically generated
- ✅ **No hardcoded ARNs** - Constructed dynamically
- ✅ **No absolute paths** - Relative or AgentCore-generated
- ✅ **Generated files excluded** - `.env` and `.bedrock_agentcore.yaml` in `.gitignore`

---

## 📖 Additional Documentation

- [Segmentation Agent Details](./segmentation-agent/README.md)
- [Prediction Agent Details](./customer-behavior-pred-seg/README.md)
- [AWS Bedrock AgentCore Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)

---

<div align="center">

**Built with ❤️ using Amazon Bedrock AgentCore**

[AWS Bedrock](https://aws.amazon.com/bedrock/) • [AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)

</div>
