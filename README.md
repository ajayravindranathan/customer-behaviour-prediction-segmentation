# 🎯 Customer Behavior Prediction & Segmentation

<div align="center">

![Customer Behavior Analytics](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge)
![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock_AgentCore-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge)


*AI-powered customer analytics platform for predicting behavior patterns and intelligent segmentation using Amazon Bedrock AgentCore*

</div>

---

## 📋 Overview

This repository contains two powerful AI agents built on Amazon Bedrock AgentCore that analyze customer data, predict behavior patterns, and provide actionable insights to aid customer migrations:

- **⚙️ Customer Behaviour Prediction Agent**: Automated ML pipeline for migration propensity
- **🔍 Segmentation Agent**: Interactive customer analysis and segmentation
 prediction

Both agents leverage Claude models powered by Amazon Bedrock for intelligent data analysis, feature generation, and predictive modeling.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      Amazon Bedrock AgentCore                           │
├─────────────────────────────────┬───────────────────────────────────────┤
│  Customer Behaviour Prediction  │      Segmentation Agent               │
│  • Feature Generation           │      • Data Analysis                  │
│  • Glue ETL Pipelines           │      • Visualization                  │
│  • SageMaker Training           │      • Interactive Insights           │
│  • Propensity Modeling          │      • Code Interpretation            │
└─────────────────────────────────┴───────────────────────────────────────┘
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

## 🚀 Quick Start

### Prerequisites

- AWS Account with Bedrock access
- AWS CLI configured
- Python 3.11+


## 📁 Repository Structure

```
.
├── customer-behavior-pred-seg/      # Feature engineering agent
│   ├── enhanced_feature_agent.py    # ML pipeline agent
│   ├── webapp.py                    # Streamlit interface
│   ├── deploy.sh                    # Deployment script
│   └── setup_iam.sh                 # IAM configuration
│
├── segmentation-agent/              # Interactive segmentation agent
│   ├── segmentation_agent.py        # Main agent implementation
│   ├── deploy.sh                    # Deployment automation
│   ├── setup-agent-permissions.sh   # IAM setup
│   └── webapp/                      # Web interface
│
└── data/                            # Sample datasets
    ├── customer_propensity_data_*.csv
    └── generate_customer_data.py    # Data generator
```

## 🎯 Key Features

### Customer Behaviour Prediction Agent
- ✅ Automated feature generation with LLM
- ✅ AWS Glue ETL pipeline creation
- ✅ SageMaker/AutoGluon model training
- ✅ Migration propensity modeling
- ✅ Portable deployment (any AWS account)

### Segmentation Agent
- ✅ Real-time customer data analysis from S3
- ✅ AI-powered insights and recommendations
- ✅ Interactive visualizations
- ✅ Code interpretation for advanced analytics
- ✅ Web-based interface

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
| **Agentic AI** | Amazon Bedrock |
| **Runtime** | Bedrock AgentCore |
| **Framework** | Strands Agents |
| **ETL** | AWS Glue |
| **Training** | SageMaker, AutoGluon |
| **Storage** | Amazon S3 |
| **Interface** | Streamlit |
| **Language** | Python 3.11+ |

## 📖 Documentation

- [Customer Behaviour Prediction Agent README](./customer-behavior-pred-seg/README.md)
- [Segmentation Agent README](./segmentation-agent/README.md)
- [AWS Bedrock AgentCore Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)

## 🔧 Troubleshooting

### Common Issues

**Permission Errors**
```bash
# Re-run IAM setup scripts
cd customer-behavior-pred-seg && ./setup_iam.sh
cd segmentation-agent && ./setup-agent-permissions.sh
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

---

<div align="center">

**Built with ❤️ using Amazon Bedrock AgentCore and Kiro CLI**

[AWS Bedrock](https://aws.amazon.com/bedrock/) • [AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html) • [Strands Agents](https://github.com/awslabs/strands-agents)

</div>
