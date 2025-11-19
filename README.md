# 🎯 Customer Behavior Prediction & Segmentation

<div align="center">

![Customer Behavior Analytics](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge)
![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock_AgentCore-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge)

<img src="./assets/customer-segmentation-banner.svg" alt="Customer Behavior Prediction" width="800"/>

*AI-powered customer analytics platform for predicting behavior patterns and intelligent segmentation using Amazon Bedrock AgentCore*

</div>

---

## 📋 Overview

This repository contains two powerful AI agents built on Amazon Bedrock AgentCore that analyze customer data, predict behavior patterns, and provide actionable insights for telecom customer management:

- **🔍 Segmentation Agent**: Interactive customer analysis and segmentation
- **⚙️ Feature Engineering Agent**: Automated ML pipeline for migration propensity prediction

Both agents leverage Claude 3.7 Sonnet for intelligent data analysis, feature generation, and predictive modeling.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Amazon Bedrock AgentCore                  │
│  ┌──────────────────────┐    ┌──────────────────────────┐  │
│  │ Segmentation Agent   │    │ Feature Engineering Agent│  │
│  │ • Data Analysis      │    │ • Feature Generation     │  │
│  │ • Visualization      │    │ • Glue ETL Pipelines     │  │
│  │ • Insights           │    │ • SageMaker Training     │  │
│  └──────────────────────┘    └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────────────────────────┐
        │         AWS Services Layer            │
        │  • S3 (Data Storage)                  │
        │  • Glue (ETL Processing)              │
        │  • SageMaker (ML Training)            │
        │  • Bedrock (LLM Inference)            │
        └───────────────────────────────────────┘
                            ↓
        ┌───────────────────────────────────────┐
        │      Customer Data & Analytics        │
        │  • Demographics                       │
        │  • Behavioral Patterns                │
        │  • Migration Propensity               │
        │  • Churn Prediction                   │
        └───────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- AWS Account with Bedrock access
- AWS CLI configured
- Python 3.11+
- Docker (for AgentCore deployment)

```bash
# Install AgentCore CLI
pip install bedrock-agentcore

# Verify AWS credentials
aws sts get-caller-identity
```

### Deploy Segmentation Agent

```bash
cd segmentation-agent
./deploy.sh
```

### Deploy Feature Engineering Agent

```bash
cd customer-behavior-pred-seg
./deploy.sh
./setup_iam.sh
./run_webapp.sh
```

Access the web interface at: http://localhost:8501

## 📊 Use Cases

### 1. Customer Segmentation
Analyze customer demographics, behavior patterns, and create actionable segments:
```bash
agentcore invoke '{"prompt": "Segment customers by engagement level and spending patterns"}'
```

### 2. Migration Propensity Prediction
Predict customer behavior during network migrations:
- **Call Propensity**: Likelihood of support contact
- **Churn Propensity**: Risk of service cancellation
- **Spend Change**: Expected spending pattern shifts

### 3. Automated Feature Engineering
Generate ML features using AI:
```
Generate feature suggestions for churn prediction using customer data at s3://my-bucket/data/
```

### 4. Data Quality Analysis
Explore and validate customer datasets:
```bash
agentcore invoke '{"prompt": "Analyze data quality and show missing value patterns"}'
```

## 📁 Repository Structure

```
.
├── segmentation-agent/              # Interactive segmentation agent
│   ├── segmentation_agent.py        # Main agent implementation
│   ├── deploy.sh                    # Deployment automation
│   ├── setup-agent-permissions.sh   # IAM setup
│   └── webapp/                      # Web interface
│
├── customer-behavior-pred-seg/      # Feature engineering agent
│   ├── enhanced_feature_agent.py    # ML pipeline agent
│   ├── webapp.py                    # Streamlit interface
│   ├── deploy.sh                    # Deployment script
│   └── setup_iam.sh                 # IAM configuration
│
└── data/                            # Sample datasets
    ├── customer_propensity_data_*.csv
    └── generate_customer_data.py    # Data generator
```

## 🎯 Key Features

### Segmentation Agent
- ✅ Real-time customer data analysis from S3
- ✅ AI-powered insights and recommendations
- ✅ Interactive visualizations
- ✅ Code interpretation for advanced analytics
- ✅ Web-based interface

### Feature Engineering Agent
- ✅ Automated feature generation with LLM
- ✅ AWS Glue ETL pipeline creation
- ✅ SageMaker/AutoGluon model training
- ✅ Migration propensity modeling
- ✅ Portable deployment (any AWS account)

## 🔐 Security & Permissions

Both agents use least-privilege IAM roles with permissions for:
- S3 bucket access (read/write)
- AWS Glue job execution
- SageMaker training
- Bedrock model invocation
- CloudWatch logging

All customer data remains within your AWS account and is never shared externally.

## 📈 Sample Data

The repository includes a data generator for testing:

```bash
cd data
python generate_customer_data.py
```

Generates synthetic customer data with:
- Demographics (age, geography, tenure)
- Product subscriptions (broadband, TV, voice)
- Behavioral metrics (contact frequency, engagement)
- Migration propensity indicators

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **AI/ML** | Amazon Bedrock (Claude 3.7 Sonnet) |
| **Runtime** | Bedrock AgentCore |
| **Framework** | Strands Agents |
| **ETL** | AWS Glue |
| **Training** | SageMaker, AutoGluon |
| **Storage** | Amazon S3 |
| **Interface** | Streamlit |
| **Language** | Python 3.11+ |

## 📖 Documentation

- [Segmentation Agent README](./segmentation-agent/README.md)
- [Feature Engineering Agent README](./customer-behavior-pred-seg/README.md)
- [AWS Bedrock AgentCore Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)

## 🔧 Troubleshooting

### Common Issues

**Permission Errors**
```bash
# Re-run IAM setup scripts
cd segmentation-agent && ./setup-agent-permissions.sh
cd customer-behavior-pred-seg && ./setup_iam.sh
```

**Agent Not Found**
```bash
# List deployed agents
agentcore configure list
agentcore status
```

**S3 Access Issues**
```bash
# Verify bucket access
aws s3 ls s3://your-bucket-name/
```

## 🤝 Contributing

This is an internal project for BT Networks customer behavior analysis. For questions or issues, please contact the development team.

## 📝 License

Internal use only - BT Networks

---

<div align="center">

**Built with ❤️ using Amazon Bedrock AgentCore**

[AWS Bedrock](https://aws.amazon.com/bedrock/) • [AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html) • [Strands Agents](https://github.com/awslabs/strands-agents)

</div>
