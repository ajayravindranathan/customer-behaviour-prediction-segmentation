#!/usr/bin/env python3
"""
Script to make the feature engineering agent portable for deployment on fresh AWS accounts.
Removes hardcoded account IDs, regions, and ARNs.
"""

import re
import os

def get_aws_config():
    """Get AWS account ID and region dynamically"""
    return """
# Get AWS account and region dynamically
import os
AWS_REGION = os.environ.get('AWS_REGION', os.environ.get('AWS_DEFAULT_REGION', 'us-east-1'))
AWS_ACCOUNT_ID = None

def get_aws_account_id():
    global AWS_ACCOUNT_ID
    if AWS_ACCOUNT_ID is None:
        try:
            sts = boto3.client('sts', region_name=AWS_REGION)
            AWS_ACCOUNT_ID = sts.get_caller_identity()['Account']
        except Exception:
            AWS_ACCOUNT_ID = 'UNKNOWN'
    return AWS_ACCOUNT_ID
"""

def fix_enhanced_feature_agent():
    """Fix hardcoded values in enhanced_feature_agent.py"""
    
    with open('enhanced_feature_agent.py', 'r') as f:
        content = f.read()
    
    # Add AWS config at the top after imports
    import_section_end = content.find('app = BedrockAgentCoreApp()')
    if import_section_end != -1:
        content = content[:import_section_end] + get_aws_config() + '\n' + content[import_section_end:]
    
    # Fix hardcoded region in bedrock-runtime client calls
    content = re.sub(
        r"boto3\.client\('bedrock-runtime',\s*region_name='us-east-1'\)",
        "boto3.client('bedrock-runtime', region_name=AWS_REGION)",
        content
    )
    
    # Fix hardcoded Glue role ARN
    content = re.sub(
        r"glue_role_arn = 'arn:aws:iam::727710292016:role/GlueServiceRole'",
        "glue_role_arn = f'arn:aws:iam::{get_aws_account_id()}:role/GlueServiceRole'",
        content
    )
    
    # Fix hardcoded S3 bucket for Glue scripts
    content = re.sub(
        r"script_bucket = 'bt-customer-segmentation'",
        "script_bucket = os.environ.get('GLUE_SCRIPT_BUCKET', f'feature-engineering-{get_aws_account_id()}')",
        content
    )
    
    # Fix ScriptLocation in Glue job definition
    content = re.sub(
        r"'ScriptLocation': f's3://bt-customer-segmentation/glue-scripts/\{job_name\}\.py'",
        "'ScriptLocation': f's3://{script_bucket}/glue-scripts/{job_name}.py'",
        content
    )
    
    with open('enhanced_feature_agent.py', 'w') as f:
        f.write(content)
    
    print("✅ Fixed enhanced_feature_agent.py")

def fix_webapp():
    """Fix hardcoded values in webapp.py"""
    
    with open('webapp.py', 'r') as f:
        content = f.read()
    
    # Replace hardcoded ARN and region with environment variables
    new_header = '''import streamlit as st
import boto3
import json
import os
from datetime import datetime

# Agent configuration - dynamically determined
AWS_REGION = os.environ.get('AWS_REGION', os.environ.get('AWS_DEFAULT_REGION', 'us-east-1'))
AGENT_ARN = os.environ.get('AGENT_ARN', '')

if not AGENT_ARN:
    st.error("⚠️ AGENT_ARN environment variable not set. Please set it before running the webapp.")
    st.info("Example: export AGENT_ARN='arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/enhanced_feature_agent-xxxxx'")
    st.stop()
'''
    
    # Find the end of imports and replace the config section
    lines = content.split('\n')
    new_lines = []
    skip_until_class = False
    
    for i, line in enumerate(lines):
        if i == 0 and line.startswith('import'):
            new_lines.append(new_header)
            skip_until_class = True
        elif skip_until_class and line.startswith('class AgentClient'):
            skip_until_class = False
            new_lines.append(line)
        elif not skip_until_class:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Fix REGION references
    content = content.replace('region_name=REGION', 'region_name=AWS_REGION')
    
    with open('webapp.py', 'w') as f:
        f.write(content)
    
    print("✅ Fixed webapp.py")

if __name__ == '__main__':
    print("Making feature engineering agent portable...")
    fix_enhanced_feature_agent()
    fix_webapp()
    print("\n✅ All files updated successfully!")
    print("\nNext steps:")
    print("1. Set up IAM roles: ./setup_iam.sh")
    print("2. Deploy agent: ./deploy.sh")
    print("3. Run webapp: ./run_webapp.sh")
