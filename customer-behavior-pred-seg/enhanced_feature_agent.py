"""
Enhanced Feature Engineering Agent for Telecom Customer Migration Propensity Models

This agent:
1. Accesses S3 data directly for exploration
2. Allows users to suggest new features during conversation
3. Uses LLM to generate features dynamically
4. Creates Glue jobs with confirmed feature list

Deployed on Amazon Bedrock AgentCore Runtime.
"""

import json
import boto3
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent, tool, ToolContext


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

app = BedrockAgentCoreApp()

class FeatureEngineeringState:
    """Maintains conversation state across interactions"""
    def __init__(self):
        self.raw_data_analysis = None
        self.llm_suggested_features = None
        self.user_suggested_features = []
        self.final_feature_list = []
        self.user_feedback = []
        self.conversation_stage = "initial"  # initial, s3_exploration, llm_features, user_features, confirmation, engineering
        self.s3_prefix = None
        self.features_output_path = None
        self.glue_jobs_created = []

# Global state instance
conversation_state = FeatureEngineeringState()

# Training job singleton to prevent concurrent training
_active_training_jobs = {}
_training_lock = False

@tool(context=True)
def explore_s3_data(s3_prefix: str, tool_context: ToolContext, sample_size: int = 1000) -> Dict[str, Any]:
    """
    Explore raw customer data from S3 prefix to understand structure and patterns.
    
    Args:
        s3_prefix: S3 prefix path (e.g., 's3://bucket/path/to/data/')
        sample_size: Number of records to sample for analysis (default: 1000)
    """
    try:
        # Store S3 prefix in conversation state
        conversation_state.s3_prefix = s3_prefix
        
        # Parse S3 path
        if not s3_prefix.startswith('s3://'):
            return {
                "status": "error",
                "content": [{"text": "S3 prefix must start with 's3://'. Example: 's3://my-bucket/data/'"}]
            }
        
        # Extract bucket and prefix
        s3_parts = s3_prefix.replace('s3://', '').split('/', 1)
        bucket = s3_parts[0]
        prefix = s3_parts[1] if len(s3_parts) > 1 else ''
        
        # Initialize S3 client
        s3_client = boto3.client('s3')
        
        # List objects in the prefix
        response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix, MaxKeys=10)
        
        if 'Contents' not in response:
            return {
                "status": "error",
                "content": [{"text": f"No files found in S3 prefix: {s3_prefix}"}]
            }
        
        # Find the first data file (CSV, JSON, or Parquet)
        data_file = None
        for obj in response['Contents']:
            key = obj['Key']
            if key.endswith(('.csv', '.json', '.parquet')):
                data_file = f"s3://{bucket}/{key}"
                break
        
        if not data_file:
            return {
                "status": "error",
                "content": [{"text": "No supported data files (.csv, .json, .parquet) found in the S3 prefix"}]
            }
        
        # Read and analyze the data file
        if data_file.endswith('.csv'):
            df = pd.read_csv(data_file, nrows=sample_size)
        elif data_file.endswith('.json'):
            df = pd.read_json(data_file, lines=True, nrows=sample_size)
        elif data_file.endswith('.parquet'):
            df = pd.read_parquet(data_file)
            if len(df) > sample_size:
                df = df.sample(n=sample_size)
        
        # Perform comprehensive data analysis
        analysis = {
            "s3_location": data_file,
            "total_sample_records": len(df),
            "columns": list(df.columns),
            "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "missing_values": {col: int(count) for col, count in df.isnull().sum().items()},
            "numeric_columns": df.select_dtypes(include=['number']).columns.tolist(),
            "categorical_columns": df.select_dtypes(include=['object']).columns.tolist(),
            "date_columns": df.select_dtypes(include=['datetime']).columns.tolist(),
            "sample_statistics": {
                col: {
                    "mean": float(df[col].mean()) if pd.api.types.is_numeric_dtype(df[col]) else None,
                    "std": float(df[col].std()) if pd.api.types.is_numeric_dtype(df[col]) else None,
                    "unique_values": int(df[col].nunique()),
                    "sample_values": [str(val) for val in df[col].dropna().head(5).tolist()]
                } for col in df.columns
            }
        }
        
        # Store analysis in conversation state
        conversation_state.raw_data_analysis = analysis
        conversation_state.conversation_stage = "s3_exploration"
        
        return {
            "status": "success",
            "content": [
                {"text": f"Successfully explored S3 data from {data_file}. Analyzed {analysis['total_sample_records']} sample records with {len(analysis['columns'])} columns."},
                {"json": analysis}
            ]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error exploring S3 data: {str(e)}"}]
        }

@tool(context=True)
def generate_llm_features(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Use LLM to generate feature suggestions based on the S3 data analysis.
    Requires prior S3 data exploration.
    """
    if not conversation_state.raw_data_analysis:
        return {
            "status": "error",
            "content": [{"text": "Please explore S3 data first using explore_s3_data tool."}]
        }
    
    analysis = conversation_state.raw_data_analysis
    
    # Use direct boto3 call to Claude 3.5 Sonnet
    bedrock_client = boto3.client('bedrock-runtime', region_name=AWS_REGION)
    
    system_prompt = """You are a senior data scientist specializing in telecom customer analytics and migration projects. 

Based on the provided S3 data analysis, generate specific, actionable features for predicting three post-migration outcomes:
1. Propensity for customers to call support post-migration
2. Propensity for customers to churn post-migration  
3. Propensity for customers to change their spending post-migration

For each feature, provide:
- feature_name: Clear, descriptive name
- description: What the feature measures
- formula: Exact mathematical formula using available columns
- source_columns: List of required columns from the data
- rationale: Why this feature is predictive for the specific outcome
- complexity: Low/Medium/High implementation complexity

Consider migration contexts:
- IT stack modernization
- End user device migrations  
- Network infrastructure transitions

Focus on features that can be calculated from the available data columns.
Provide 3-5 features per propensity model.

Also suggest 2-3 additional data sources that would significantly improve each model.

Return your response as a structured JSON object with proper escaping."""
    
    # Prepare data analysis summary for the LLM
    data_summary = {
        "s3_location": analysis["s3_location"],
        "total_sample_records": analysis["total_sample_records"],
        "available_columns": analysis["columns"],
        "numeric_columns": analysis["numeric_columns"],
        "categorical_columns": analysis["categorical_columns"],
        "date_columns": analysis["date_columns"],
        "column_statistics": analysis["sample_statistics"]
    }
    
    prompt = f"""
    Based on this telecom customer data from S3, generate specific features for three propensity models:

    DATA ANALYSIS:
    {json.dumps(data_summary, indent=2)}

    Generate features that can be calculated using the available columns. For each feature, provide the exact formula using column names from the data.

    Return a JSON structure with:
    {{
        "existing_data_features": {{
            "call_propensity": [list of feature objects],
            "churn_propensity": [list of feature objects], 
            "spend_change_propensity": [list of feature objects]
        }},
        "additional_data_recommendations": {{
            "call_propensity": [list of data source recommendations],
            "churn_propensity": [list of data source recommendations],
            "spend_change_propensity": [list of data source recommendations]
        }}
    }}

    Each feature object should have: feature_name, description, formula, source_columns, rationale, complexity.
    Each data source recommendation should have: data_source, description, rationale, implementation.
    """
    
    try:
        # Generate features using Claude 3.7 Sonnet inference profile
        response = bedrock_client.converse(
            modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
            messages=[{
                "role": "user",
                "content": [{"text": prompt}]
            }],
            system=[{"text": system_prompt}],
            inferenceConfig={
                "maxTokens": 4000,
                "temperature": 0.1
            }
        )
        
        # Extract response text
        response_text = response['output']['message']['content'][0]['text']
        
        # Extract JSON from the response
        import re
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            feature_suggestions = json.loads(json_match.group())
        else:
            # Fallback: try to parse the entire response as JSON
            feature_suggestions = json.loads(response_text)
        
        # Store LLM suggestions in conversation state
        conversation_state.llm_suggested_features = feature_suggestions
        conversation_state.conversation_stage = "llm_features"
        
        return {
            "status": "success",
            "content": [
                {"text": f"LLM generated features for all three propensity models based on your S3 data structure. You can now review these features and suggest additional ones."},
                {"json": feature_suggestions}
            ]
        }
        
    except json.JSONDecodeError as e:
        return {
            "status": "error", 
            "content": [{"text": f"Error parsing LLM response as JSON: {str(e)}. Raw response: {response_text[:500]}..."}]
        }
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error generating features with LLM: {str(e)}"}]
        }

@tool(context=True)
def add_user_suggested_feature(feature_name: str, description: str, formula: str, source_columns: List[str], 
                              target_model: str, rationale: str, tool_context: ToolContext) -> Dict[str, Any]:
    """
    Allow users to suggest additional features during the conversation.
    
    Args:
        feature_name: Name of the user-suggested feature
        description: Description of what the feature measures
        formula: Mathematical formula for the feature
        source_columns: List of required columns from the data
        target_model: Which model this feature targets (call_propensity, churn_propensity, spend_change_propensity)
        rationale: Why this feature would be useful for prediction
    """
    try:
        # Validate target model
        valid_models = ['call_propensity', 'churn_propensity', 'spend_change_propensity']
        if target_model not in valid_models:
            return {
                "status": "error",
                "content": [{"text": f"target_model must be one of: {', '.join(valid_models)}"}]
            }
        
        # Validate source columns exist in the data
        if conversation_state.raw_data_analysis:
            available_columns = conversation_state.raw_data_analysis['columns']
            missing_columns = [col for col in source_columns if col not in available_columns]
            if missing_columns:
                return {
                    "status": "error",
                    "content": [{"text": f"Source columns not found in data: {missing_columns}. Available columns: {available_columns}"}]
                }
        
        # Create user feature object
        user_feature = {
            "feature_name": feature_name,
            "description": description,
            "formula": formula,
            "source_columns": source_columns,
            "target_model": target_model,
            "rationale": rationale,
            "complexity": "User-defined",
            "suggested_by": "user",
            "timestamp": datetime.now().isoformat()
        }
        
        # Add to user suggested features
        conversation_state.user_suggested_features.append(user_feature)
        conversation_state.conversation_stage = "user_features"
        
        return {
            "status": "success",
            "content": [
                {"text": f"Successfully added user-suggested feature '{feature_name}' for {target_model} model. Total user features: {len(conversation_state.user_suggested_features)}"},
                {"json": {
                    "added_feature": user_feature,
                    "total_user_features": len(conversation_state.user_suggested_features),
                    "all_user_features": conversation_state.user_suggested_features
                }}
            ]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error adding user feature: {str(e)}"}]
        }

@tool(context=True)
def confirm_final_feature_list(confirmed_llm_features: List[str], tool_context: ToolContext, include_all_user_features: bool = True, 
                              include_raw_columns: List[str] = None) -> Dict[str, Any]:
    """
    Confirm the final list of features to be implemented, including LLM features, user features, and raw columns.
    
    Args:
        confirmed_llm_features: List of LLM-generated feature names to include
        include_all_user_features: Whether to include all user-suggested features (default: True)
        include_raw_columns: List of raw data columns to include as-is (optional)
    """
    try:
        if not conversation_state.llm_suggested_features:
            return {
                "status": "error",
                "content": [{"text": "No LLM features available. Please generate LLM features first."}]
            }
        
        final_features = []
        
        # Add confirmed LLM features
        llm_features = conversation_state.llm_suggested_features.get('existing_data_features', {})
        for model_type in ['call_propensity', 'churn_propensity', 'spend_change_propensity']:
            if model_type in llm_features:
                for feature in llm_features[model_type]:
                    if feature['feature_name'] in confirmed_llm_features:
                        feature['source'] = 'llm'
                        final_features.append(feature)
        
        # Add user-suggested features
        if include_all_user_features:
            for user_feature in conversation_state.user_suggested_features:
                user_feature['source'] = 'user'
                final_features.append(user_feature)
        
        # Add raw columns as pass-through features
        if include_raw_columns:
            for col in include_raw_columns:
                if conversation_state.raw_data_analysis and col in conversation_state.raw_data_analysis['columns']:
                    raw_feature = {
                        "feature_name": col,
                        "description": f"Raw column: {col}",
                        "formula": col,  # Pass-through
                        "source_columns": [col],
                        "rationale": "Raw data column included for model training",
                        "complexity": "Low",
                        "source": "raw_data"
                    }
                    final_features.append(raw_feature)
        
        # Store final feature list
        conversation_state.final_feature_list = final_features
        conversation_state.conversation_stage = "confirmation"
        
        # Prepare summary
        feature_summary = {
            "total_features": len(final_features),
            "llm_features": len([f for f in final_features if f.get('source') == 'llm']),
            "user_features": len([f for f in final_features if f.get('source') == 'user']),
            "raw_columns": len([f for f in final_features if f.get('source') == 'raw_data']),
            "features_by_model": {
                "call_propensity": len([f for f in final_features if f.get('target_model') == 'call_propensity' or 'call_propensity' in str(f)]),
                "churn_propensity": len([f for f in final_features if f.get('target_model') == 'churn_propensity' or 'churn_propensity' in str(f)]),
                "spend_change_propensity": len([f for f in final_features if f.get('target_model') == 'spend_change_propensity' or 'spend_change_propensity' in str(f)])
            },
            "feature_list": final_features
        }
        
        return {
            "status": "success",
            "content": [
                {"text": f"Confirmed final feature list with {len(final_features)} features ready for Glue job creation."},
                {"json": feature_summary}
            ]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error confirming feature list: {str(e)}"}]
        }

@tool(context=True)
def create_glue_job_with_confirmed_features(job_name: str, s3_output_path: str, tool_context: ToolContext,
                                          glue_role_arn: str = None) -> Dict[str, Any]:
    """
    Create AWS Glue job with the confirmed feature list and deploy to AWS.
    
    Args:
        job_name: Name for the Glue job
        s3_output_path: S3 path where engineered features will be stored
        glue_role_arn: IAM role ARN for Glue job (optional, will use default if not provided)
    """
    try:
        # Store the feature engineering output path
        conversation_state.features_output_path = s3_output_path
        
        if not conversation_state.final_feature_list:
            return {
                "status": "error",
                "content": [{"text": "No confirmed features available. Please confirm feature list first."}]
            }
        
        if not conversation_state.s3_prefix:
            return {
                "status": "error",
                "content": [{"text": "No S3 data source available. Please explore S3 data first."}]
            }
        
        # Generate comprehensive Glue script
        script_content = generate_comprehensive_glue_script(
            conversation_state.final_feature_list,
            conversation_state.s3_prefix,
            s3_output_path
        )
        
        # Create Glue client
        glue_client = boto3.client('glue')
        
        # Get script bucket
        script_bucket = os.environ.get('GLUE_SCRIPT_BUCKET', f'feature-engineering-{get_aws_account_id()}')
        
        # Default role if not provided
        if not glue_role_arn:
            glue_role_arn = f'arn:aws:iam::{get_aws_account_id()}:role/GlueServiceRole'
        
        # Create Glue job definition
        job_definition = {
            'Name': job_name,
            'Role': glue_role_arn,
            'Command': {
                'Name': 'glueetl',
                'ScriptLocation': f's3://{script_bucket}/glue-scripts/{job_name}.py',
                'PythonVersion': '3'
            },
            'DefaultArguments': {
                '--job-language': 'python',
                '--enable-metrics': '',
                '--enable-continuous-cloudwatch-log': 'true',
                '--input_path': conversation_state.s3_prefix,
                '--output_path': s3_output_path,
                '--feature_count': str(len(conversation_state.final_feature_list))
            },
            'MaxRetries': 1,
            'Timeout': 120,
            'GlueVersion': '3.0',
            'WorkerType': 'G.1X',
            'NumberOfWorkers': 2
        }
        
        # Create S3 client to upload script
        s3_client = boto3.client('s3')
        
        # Upload script to S3
        script_key = f'glue-scripts/{job_name}.py'
        
        try:
            s3_client.put_object(
                Bucket=script_bucket,
                Key=script_key,
                Body=script_content.encode('utf-8'),
                ContentType='text/plain'
            )
        except Exception as e:
            return {
                "status": "error",
                "content": [{"text": f"Error uploading script to S3: {str(e)}"}]
            }
        
        # Actually create the Glue job
        try:
            response = glue_client.create_job(**job_definition)
            job_arn = response.get('Name', job_name)
        except Exception as e:
            return {
                "status": "error", 
                "content": [{"text": f"Error creating Glue job: {str(e)}"}]
            }
        
        # Job creation successful
        job_info = {
            "job_name": job_name,
            "job_arn": job_arn,
            "total_features": len(conversation_state.final_feature_list),
            "feature_breakdown": {
                "llm_generated": len([f for f in conversation_state.final_feature_list if f.get('source') == 'llm']),
                "user_suggested": len([f for f in conversation_state.final_feature_list if f.get('source') == 'user']),
                "raw_columns": len([f for f in conversation_state.final_feature_list if f.get('source') == 'raw_data'])
            },
            "input_path": conversation_state.s3_prefix,
            "output_path": s3_output_path,
            "script_content": script_content,
            "job_definition": job_definition,
            "status": "created",
            "created_at": datetime.now().isoformat()
        }
        
        conversation_state.glue_jobs_created.append(job_info)
        conversation_state.conversation_stage = "engineering"
        
        return {
            "status": "success",
            "content": [
                {"text": f"Successfully created Glue job '{job_name}' with {len(conversation_state.final_feature_list)} confirmed features."},
                {"json": job_info}
            ]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error creating Glue job: {str(e)}"}]
        }

@tool(context=True)
def run_glue_job(job_name: str, tool_context: ToolContext) -> Dict[str, Any]:
    """
    Start a previously created AWS Glue job.
    
    Args:
        job_name: Name of the Glue job to run
    """
    try:
        glue_client = boto3.client('glue')
        
        # Check if job exists in our conversation state
        job_info = None
        for job in conversation_state.glue_jobs_created:
            if job['job_name'] == job_name:
                job_info = job
                break
        
        if not job_info:
            return {
                "status": "error",
                "content": [{"text": f"Job '{job_name}' not found in conversation history. Please create the job first."}]
            }
        
        # Start the job run
        job_run_response = glue_client.start_job_run(
            JobName=job_name,
            Arguments={
                '--input_path': job_info['input_path'],
                '--output_path': job_info['output_path'],
                '--feature_count': str(job_info['total_features'])
            }
        )
        
        job_run_id = job_run_response['JobRunId']
        
        # Update job info with run details
        job_info['job_run_id'] = job_run_id
        job_info['status'] = 'running'
        job_info['started_at'] = datetime.now().isoformat()
        
        return {
            "status": "success",
            "content": [
                {"text": f"Successfully started Glue job '{job_name}'."},
                {"text": f"Job run ID: {job_run_id}"},
                {"text": f"Monitor progress: aws glue get-job-run --job-name {job_name} --run-id {job_run_id}"},
                {"json": {"job_name": job_name, "job_run_id": job_run_id, "status": "running"}}
            ]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error starting Glue job: {str(e)}"}]
        }

@tool(context=True)
def test_autogluon_availability(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Test if AutoGluon Cloud is available and properly installed.
    """
    try:
        # Test basic imports
        import sys
        import pkg_resources
        
        # Check if autogluon.cloud is installed
        try:
            import autogluon.cloud
            autogluon_cloud_version = autogluon.cloud.__version__
            autogluon_cloud_available = True
            autogluon_cloud_error = None
        except ImportError as e:
            autogluon_cloud_available = False
            autogluon_cloud_error = str(e)
            autogluon_cloud_version = None
        
        # Check if TabularCloudPredictor is available
        try:
            from autogluon.cloud import TabularCloudPredictor
            tabular_predictor_available = True
            tabular_predictor_error = None
        except ImportError as e:
            tabular_predictor_available = False
            tabular_predictor_error = str(e)
        
        # Get list of installed packages
        installed_packages = [pkg.project_name for pkg in pkg_resources.working_set]
        autogluon_packages = [pkg for pkg in installed_packages if 'autogluon' in pkg.lower()]
        
        result = {
            "python_version": sys.version,
            "autogluon_cloud_available": autogluon_cloud_available,
            "autogluon_cloud_version": autogluon_cloud_version,
            "autogluon_cloud_error": autogluon_cloud_error,
            "tabular_predictor_available": tabular_predictor_available,
            "tabular_predictor_error": tabular_predictor_error,
            "autogluon_packages": autogluon_packages,
            "total_packages": len(installed_packages)
        }
        
        return {
            "status": "success",
            "content": [
                {"text": f"AutoGluon availability test completed."},
                {"json": result}
            ]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error testing AutoGluon availability: {str(e)}"}]
        }

@tool(context=True)
def train_propensity_models(model_type: str, features_s3_path: str = None, tool_context: ToolContext = None, 
                          models_output_path: str = None,
                          time_limit: int = 120) -> Dict[str, Any]:
    """
    Train a single propensity model using AutoGluon Cloud TabularCloudPredictor with streaming progress updates.
    
    Args:
        model_type: Which propensity model to train - must be one of: "churn", "call", "spend_change"
        features_s3_path: S3 path to the engineered features (optional, uses raw data if not provided)
        models_output_path: S3 path where trained models will be stored
        time_limit: Training time limit in seconds (default: 120)
    """
    global _active_training_jobs, _training_lock
    
    _training_lock = True
    try:
        import pandas as pd
        from autogluon.cloud import TabularCloudPredictor
        from sklearn.model_selection import train_test_split
        import boto3
        import os
        import time
        
        # Track this training job
        job_id = f"{model_type}_{int(time.time())}"
        _active_training_jobs[model_type] = job_id
        
        # Set the correct region for the S3 bucket
        os.environ['AWS_DEFAULT_REGION'] = 'eu-west-1'
        
        # Validate model type
        valid_models = {
            "churn": {"name": "churn_propensity", "target": "churn_after_migration"},
            "call": {"name": "call_propensity", "target": "number_of_calls_post_migration"},
            "spend_change": {"name": "spend_change_propensity", "target": "change_in_spend"}
        }
        
        if model_type not in valid_models:
            return {
                "status": "error",
                "content": [{"text": f"Invalid model_type '{model_type}'. Must be one of: {list(valid_models.keys())}"}]
            }
        
        model_config = valid_models[model_type]
        model_name = model_config["name"]
        target_column = model_config["target"]
        
        # Stream progress update
        print(f"🚀 Starting {model_name} training pipeline...")
        
        # Use engineered features from conversation state if available
        if not features_s3_path:
            if conversation_state.features_output_path:
                features_s3_path = conversation_state.features_output_path
            else:
                # Use dynamic bucket name
                bucket_name = os.environ.get('GLUE_SCRIPT_BUCKET', f'feature-engineering-{get_aws_account_id()}')
                features_s3_path = f"s3://{bucket_name}/features/"
        
        # Set default models output path if not provided
        if not models_output_path:
            bucket_name = os.environ.get('GLUE_SCRIPT_BUCKET', f'feature-engineering-{get_aws_account_id()}')
            models_output_path = f"s3://{bucket_name}/models/"
        
        print(f"📊 Loading data from: {features_s3_path}")
        
        # Load and prepare data
        try:
            if features_s3_path.endswith('/'):
                # Load from features directory - try CSV first, then parquet
                try:
                    csv_path = features_s3_path + "features_csv/"
                    data = pd.read_csv(csv_path)
                    print(f"✅ Loaded engineered features from CSV: {csv_path}")
                except:
                    parquet_path = features_s3_path + "features/"
                    data = pd.read_parquet(parquet_path)
                    print(f"✅ Loaded engineered features from Parquet: {parquet_path}")
            elif features_s3_path.endswith('.parquet'):
                data = pd.read_parquet(features_s3_path)
            else:
                data = pd.read_csv(features_s3_path)
        except:
            # Fallback to raw data
            print("📊 Falling back to raw data...")
            bucket_name = os.environ.get('GLUE_SCRIPT_BUCKET', f'feature-engineering-{get_aws_account_id()}')
            # Use the same bucket but raw-data path
            if conversation_state.s3_prefix:
                data = pd.read_csv(conversation_state.s3_prefix)
            else:
                raise Exception("No feature data or raw data path available. Please run feature engineering first.")
        
        print(f"✅ Loaded data: {len(data)} rows, {len(data.columns)} columns")
        
        # Check if target column exists
        if target_column not in data.columns:
            return {
                "status": "error",
                "content": [{"text": f"Target column '{target_column}' not found in data. Available columns: {list(data.columns)}"}]
            }
        
        print(f"🎯 Training {model_name} model for target: {target_column}")
        
        try:
            # Split data for this model
            if target_column == "churn_after_migration":
                # Binary classification - stratify
                train_data, test_data = train_test_split(data, test_size=0.2, random_state=42, stratify=data[target_column])
            else:
                # Regression - no stratification
                train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            
            print(f"📈 Data split: {len(train_data)} train, {len(test_data)} test")
            
            # Remove target from test data for prediction
            test_features = test_data.drop(columns=[target_column])
            
            # Configure predictor
            predictor_init_args = {"label": target_column}
            predictor_fit_args = {"train_data": train_data, "time_limit": time_limit}
            
            # Train model with TabularCloudPredictor
            model_output_path = f"{models_output_path}{model_name}/"
            
            # Configure AWS session with explicit region
            aws_region = os.environ.get('AWS_REGION', 'us-east-1')
            boto3.setup_default_session(region_name=aws_region)
            
            # Initialize TabularCloudPredictor
            cloud_predictor = TabularCloudPredictor(cloud_output_path=model_output_path)
            
            print(f"🔄 Starting model training (time limit: {time_limit}s)...")
            # Fit the model
            cloud_predictor.fit(predictor_init_args=predictor_init_args, predictor_fit_args=predictor_fit_args)
            print(f"✅ Model training completed successfully")
            
            # Get model performance
            try:
                leaderboard = cloud_predictor.leaderboard()
                print(f"📊 Model leaderboard for {model_name}:")
                print(leaderboard.head())
                leaderboard_dict = leaderboard.to_dict() if leaderboard is not None else None
            except Exception as e:
                print(f"⚠️ Could not generate leaderboard: {e}")
                leaderboard_dict = None
            
            # Deploy and run real-time predictions
            try:
                print(f"🚀 Deploying {model_name} model for real-time inference...")
                print("⏳ Waiting for endpoint creation (this may take a few minutes)...")
                cloud_predictor.deploy()
                print(f"✅ Inference endpoint deployed successfully")
                
                # Limit to 300 test records as requested
                test_limit = min(300, len(test_features))
                test_features_limited = test_features.head(test_limit)
                test_data_limited = test_data.head(test_limit)
                
                print(f"🔮 Running individual predictions for {model_name} ({test_limit} records):")
                
                individual_predictions = []
                for idx, (_, row) in enumerate(test_features_limited.iterrows()):
                    # Convert row to DataFrame for prediction
                    single_record = pd.DataFrame([row])
                    prediction = cloud_predictor.predict_real_time(single_record)
                    individual_predictions.append(prediction[0] if hasattr(prediction, '__len__') else prediction)
                    
                    # Print results for first 10 records with features
                    if idx < 10:
                        actual_value = test_data_limited.iloc[idx][target_column]
                        print(f"Record {idx+1:3d}: Actual={actual_value:8.3f}, Predicted={individual_predictions[-1]:8.3f}")
                        
                        # Print all features for this record
                        feature_str = ", ".join([f"{col}={row[col]:.3f}" if pd.api.types.is_numeric_dtype(row[col]) else f"{col}={row[col]}" 
                                               for col in test_features_limited.columns])
                        print(f"         Features: {feature_str}")
                        print()
                    
                    # Stream progress updates every 50 records
                    elif (idx + 1) % 50 == 0:
                        progress_pct = ((idx + 1) / test_limit) * 100
                        print(f"📊 Progress: {idx + 1}/{test_limit} records ({progress_pct:.1f}%)")
                
                print(f"✅ Individual predictions completed: {len(individual_predictions)} predictions")
                
                cloud_predictor.cleanup_deployment()
                print(f"🧹 Cleaned up deployment for {model_name}")
                
                # Use individual predictions for final results
                predictions = individual_predictions
                
                # Merge predictions with original test data (includes all features + target)
                test_data_with_predictions = test_data_limited.copy()
                test_data_with_predictions[f'{target_column}_predicted'] = predictions
                
                # Save merged results to S3 model folder
                s3_client = boto3.client('s3')
                bucket_name = model_output_path.replace('s3://', '').split('/')[0]
                results_key = '/'.join(model_output_path.replace('s3://', '').split('/')[1:]) + 'test_results_with_predictions.csv'
                
                local_file = f"/tmp/test_results_{model_name}.csv"
                test_data_with_predictions.to_csv(local_file, index=False)
                s3_client.upload_file(local_file, bucket_name, results_key)
                
                results_s3_path = f"s3://{bucket_name}/{results_key}"
                print(f"💾 Saved test results with predictions to {results_s3_path}")
                
            except Exception as e:
                print(f"⚠️ Real-time prediction failed: {e}")
                predictions = None
                test_data_with_predictions = None
                test_limit = 0
            
            training_result = {
                "model_name": model_name,
                "model_type": model_type,
                "target": target_column,
                "output_path": model_output_path,
                "train_size": len(train_data),
                "test_size": len(test_data),
                "predictions_tested": test_limit,
                "leaderboard": leaderboard_dict,
                "predictions_count": len(predictions) if predictions is not None else 0,
                "results_s3_path": results_s3_path if predictions is not None else None,
                "status": "completed"
            }
            
        except Exception as e:
            print(f"❌ Error training {model_name}: {str(e)}")
            training_result = {
                "model_name": model_name,
                "model_type": model_type,
                "target": target_column,
                "error": str(e),
                "status": "failed"
            }
        
        # Summary
        summary = {
            "model_trained": model_name,
            "model_type": model_type,
            "target_variable": target_column,
            "models_output_path": models_output_path,
            "time_limit": time_limit,
            "training_result": training_result,
            "data_info": {
                "source": features_s3_path,
                "rows": len(data),
                "columns": len(data.columns)
            }
        }
        
        if training_result["status"] == "completed":
            return {
                "status": "success",
                "content": [
                    {"text": f"✅ {model_name.replace('_', ' ').title()} model trained successfully!"},
                    {"text": f"🎯 Target Variable: {target_column}"},
                    {"text": f"📊 Training Data: {training_result['train_size']} records"},
                    {"text": f"🧪 Test Data: {training_result['test_size']} records"},
                    {"text": f"🔮 Predictions: {training_result['predictions_count']} individual predictions on {training_result.get('predictions_tested', 0)} test records"},
                    {"text": f"💾 Model saved to: {training_result['output_path']}"},
                    {"text": f"📁 Results saved to: {training_result.get('results_s3_path', 'N/A')}"},
                    {"json": summary}
                ]
            }
        else:
            return {
                "status": "error",
                "content": [
                    {"text": f"❌ Failed to train {model_name.replace('_', ' ').title()} model"},
                    {"text": f"Error: {training_result.get('error', 'Unknown error')}"},
                    {"json": summary}
                ]
            }
        
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"Error training model: {str(e)}"}]
        }
    finally:
        # Always clean up singleton state
        _training_lock = False
        if model_type in _active_training_jobs:
            del _active_training_jobs[model_type]

def generate_comprehensive_glue_script(final_features: List[Dict], input_s3_path: str, output_s3_path: str) -> str:
    """Generate comprehensive AWS Glue PySpark script based on confirmed feature list"""
    
    # Separate features by type
    llm_features = [f for f in final_features if f.get('source') == 'llm']
    user_features = [f for f in final_features if f.get('source') == 'user']
    raw_columns = [f for f in final_features if f.get('source') == 'raw_data']
    
    # Generate feature engineering code
    feature_code = ""
    
    # Add LLM-generated features
    for feature in llm_features:
        feature_code += f"""
    # LLM Feature: {feature['feature_name']} - {feature['description']}
    if all(col in df.columns for col in {feature['source_columns']}):
        try:
            feature_df = feature_df.withColumn(
                '{feature['feature_name']}',
                {convert_formula_to_spark(feature.get('formula', feature['feature_name']))}
            )
            print(f"Successfully created LLM feature: {feature['feature_name']}")
        except Exception as e:
            print(f"Error creating LLM feature {feature['feature_name']}: {{e}}")
    """
    
    # Add user-suggested features
    for feature in user_features:
        feature_code += f"""
    # User Feature: {feature['feature_name']} - {feature['description']}
    if all(col in df.columns for col in {feature['source_columns']}):
        try:
            feature_df = feature_df.withColumn(
                '{feature['feature_name']}',
                {convert_formula_to_spark(feature.get('formula', feature['feature_name']))}
            )
            print(f"Successfully created user feature: {feature['feature_name']}")
        except Exception as e:
            print(f"Error creating user feature {feature['feature_name']}: {{e}}")
    """
    
    # Raw columns are passed through as-is
    raw_column_names = [f['feature_name'] for f in raw_columns]
    
    script_template = f"""
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.window import Window
import boto3

# Get job arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input_path', 'output_path', 'feature_count'])

# Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

print(f"Starting feature engineering job: {{args['JOB_NAME']}}")
print(f"Input path: {{args['input_path']}}")
print(f"Output path: {{args['output_path']}}")
print(f"Expected features: {{args['feature_count']}}")

# Read input data from S3
try:
    # Try different file formats
    input_path = args['input_path']
    if input_path.endswith('/'):
        # Read all files in directory
        df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path + "*.csv")
    else:
        # Read specific file
        if input_path.endswith('.csv'):
            df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)
        elif input_path.endswith('.json'):
            df = spark.read.json(input_path)
        elif input_path.endswith('.parquet'):
            df = spark.read.parquet(input_path)
        else:
            # Default to CSV
            df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)
    
    print(f"Successfully loaded data with {{df.count()}} records and {{len(df.columns)}} columns")
    print(f"Columns: {{df.columns}}")
    
except Exception as e:
    print(f"Error reading input data: {{e}}")
    raise e

def engineer_features(df):
    \"\"\"Engineer all confirmed features for propensity models\"\"\"
    
    print("Starting feature engineering...")
    feature_df = df
    
    # Convert data types for numeric operations
    numeric_cols = []
    for col in df.columns:
        if df.schema[col].dataType in [IntegerType(), LongType(), FloatType(), DoubleType()]:
            numeric_cols.append(col)
    
    print(f"Numeric columns identified: {{numeric_cols}}")
    
    # Convert date columns
    date_cols = []
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            try:
                feature_df = feature_df.withColumn(col, F.to_date(F.col(col)))
                date_cols.append(col)
            except:
                pass
    
    print(f"Date columns processed: {{date_cols}}")
    
    # Feature engineering code (LLM + User features)
    {feature_code}
    
    # Add raw columns (pass-through)
    raw_columns = {raw_column_names}
    for col in raw_columns:
        if col in df.columns and col not in feature_df.columns:
            feature_df = feature_df.withColumn(f"raw_{{col}}", F.col(col))
    
    print(f"Final feature count: {{len(feature_df.columns)}}")
    print(f"Final columns: {{feature_df.columns}}")
    
    return feature_df

# Apply feature engineering
try:
    engineered_df = engineer_features(df)
    
    # Add metadata columns
    engineered_df = engineered_df.withColumn("feature_engineering_timestamp", F.current_timestamp())
    engineered_df = engineered_df.withColumn("job_name", F.lit(args['JOB_NAME']))
    
    print("Feature engineering completed successfully")
    
except Exception as e:
    print(f"Error during feature engineering: {{e}}")
    raise e

# Write results to S3
try:
    output_path = args['output_path']
    
    # Write as Parquet for better performance
    engineered_df.write.mode('overwrite').option("compression", "snappy").parquet(output_path + "/features/")
    
    # Also write as CSV for easy inspection
    engineered_df.write.mode('overwrite').option("header", "true").csv(output_path + "/features_csv/")
    
    print(f"Successfully wrote engineered features to {{output_path}}")
    
    # Write feature metadata
    feature_metadata = {{
        "job_name": args['JOB_NAME'],
        "input_path": args['input_path'],
        "output_path": output_path,
        "feature_count": len(engineered_df.columns),
        "record_count": engineered_df.count(),
        "processing_timestamp": str(F.current_timestamp()),
        "features": {{
            "llm_generated": {len(llm_features)},
            "user_suggested": {len(user_features)},
            "raw_columns": {len(raw_columns)}
        }}
    }}
    
    # Convert metadata to DataFrame and write
    metadata_df = spark.createDataFrame([feature_metadata])
    metadata_df.write.mode('overwrite').json(output_path + "/metadata/")
    
    print("Feature engineering job completed successfully")
    
except Exception as e:
    print(f"Error writing output: {{e}}")
    raise e

job.commit()
"""
    
    return script_template

def convert_formula_to_spark(formula: str) -> str:
    """Convert mathematical formula to PySpark SQL expression using Claude 3.7 Sonnet"""
    if not formula or formula.strip() == "":
        return "F.lit(None)"
    
    # Simple column reference
    if formula.replace('_', '').replace(' ', '').isalnum():
        return f"F.col('{formula.strip()}')"
    
    try:
        # Use Claude 3.7 Sonnet to convert formula
        bedrock = boto3.client('bedrock-runtime', region_name=AWS_REGION)
        
        prompt = f"""Convert this mathematical formula to a PySpark SQL expression using pyspark.sql.functions (imported as F):

Formula: {formula}

Rules:
- Use F.col('column_name') for column references
- Use F.when().otherwise() for conditional logic
- Use standard operators: +, -, *, /, %, ==, !=, <, >, <=, >=
- Use F.lit() for literal values
- Use parentheses for proper precedence
- Return only the PySpark expression, no explanation

Example conversions:
- "age + 5" → "F.col('age') + 5"
- "if status == 'active' then 1 else 0" → "F.when(F.col('status') == 'active', 1).otherwise(0)"
- "calls / tenure" → "F.col('calls') / F.col('tenure')"

PySpark expression:"""

        response = bedrock.invoke_model(
            modelId='us.anthropic.claude-3-7-sonnet-20250219-v1:0',
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 200,
                "temperature": 0,
                "messages": [{"role": "user", "content": prompt}]
            })
        )
        
        result = json.loads(response['body'].read())
        spark_expression = result['content'][0]['text'].strip()
        
        # Clean up the response
        if spark_expression.startswith('```'):
            spark_expression = spark_expression.split('\n')[1:-1]
            spark_expression = '\n'.join(spark_expression)
        
        return spark_expression.strip()
        
    except Exception as e:
        print(f"Error converting formula with Claude: {e}")
        # Fallback to simple column reference
        return f"F.col('{formula.strip()}')"

# Initialize the main agent with enhanced tools
feature_agent = Agent(
    name="EnhancedTelecomFeatureEngineer",
    tools=[
        explore_s3_data,
        generate_llm_features,
        add_user_suggested_feature,
        confirm_final_feature_list,
        create_glue_job_with_confirmed_features,
        run_glue_job,
        test_autogluon_availability,
        train_propensity_models
    ]
)

# Agent instructions to be used in invocations
AGENT_INSTRUCTIONS = """
You are an advanced feature engineering agent for telecom customer migration projects. 

Your capabilities include:
1. Direct S3 data exploration and analysis
2. LLM-powered dynamic feature generation based on actual data structure
3. Interactive feature suggestion collection from users
4. Comprehensive Glue job creation with confirmed feature lists
5. Glue job execution and monitoring
6. AutoGluon Cloud model training for propensity prediction

You focus on three key propensity models:
- Call propensity (likelihood to contact support post-migration)
- Churn propensity (likelihood to cancel service post-migration)  
- Spend change propensity (likelihood to change spending patterns post-migration)

WORKFLOW TOOLS:
- explore_s3_data: Analyze raw customer data from S3
- generate_llm_features: Create AI-generated features for propensity models
- add_user_suggested_feature: Add custom user-defined features
- confirm_final_feature_list: Finalize feature selection for engineering
- create_glue_job_with_confirmed_features: Create AWS Glue ETL job
- run_glue_job: Execute a previously created Glue job
- train_propensity_models: Train a single propensity model using AutoGluon Cloud (requires model_type: "churn", "call", or "spend_change")
  * "churn" = Churn Propensity Model (predicts churn_after_migration)
  * "call" = Call Propensity Model (predicts number_of_calls_post_migration) 
  * "spend_change" = Spend Change Propensity Model (predicts change_in_spend)

IMPORTANT: Only use the specific tool that the user requests. Do not automatically chain tools together.
- If user asks to "explore S3 data", only call explore_s3_data and show the data analysis
- If user asks to "generate features", only call generate_llm_features 
- If user asks to "add a feature", only call add_user_suggested_feature
- If user asks to "confirm features", only call confirm_final_feature_list
- If user asks to "create Glue job", only call create_glue_job_with_confirmed_features
- If user asks to "run Glue job", only call run_glue_job
- If user asks to "train models", ask which model type they want to train ("churn", "call", or "spend_change"), then call train_propensity_models with the specified model_type

Wait for explicit user requests before proceeding to the next step.
Be interactive and respond to what the user specifically asks for.
"""

@app.entrypoint
async def agent_invocation(payload):
    """Enhanced handler for agent invocation with comprehensive state management"""
    user_message = payload.get("prompt", "Hello! I'm ready to help with feature engineering for your telecom migration propensity models. Let's start by exploring your S3 data.")
    
    # Extract session context
    session_id = payload.get("session_id", "default-session")
    
    # Check if training is in progress and user is requesting training
    global _training_lock, _active_training_jobs
    training_keywords = ["train", "training", "model", "propensity"]
    user_requesting_training = any(keyword in user_message.lower() for keyword in training_keywords)
    
    if user_requesting_training and (_training_lock or _active_training_jobs):
        active_jobs = list(_active_training_jobs.keys()) if _active_training_jobs else []
        return {
            "response": f"🚧 **Training In Progress**\n\nA model training job is currently running. Please wait for it to complete before starting a new training session.\n\n**Active Jobs:** {', '.join(active_jobs) if active_jobs else 'General training lock active'}\n\n**Current Status:** The existing training process is running and should not be interrupted. You can check the logs or wait for completion notification.\n\n**Available Actions:**\n- Check training progress in CloudWatch logs\n- Explore other features while waiting\n- Try again in a few minutes\n\nThe training typically takes 2-5 minutes depending on data size and model complexity.",
            "conversation_stage": conversation_state.conversation_stage,
            "session_id": session_id,
            "training_blocked": True,
            "active_training_jobs": active_jobs
        }
    
    # Add comprehensive conversation stage context
    stage_context = f"\n\nConversation Stage: {conversation_state.conversation_stage}"
    
    if conversation_state.conversation_stage == "s3_exploration" and conversation_state.raw_data_analysis:
        stage_context += f"\nS3 Data: {conversation_state.raw_data_analysis['total_sample_records']} records, {len(conversation_state.raw_data_analysis['columns'])} columns"
    elif conversation_state.conversation_stage == "llm_features" and conversation_state.llm_suggested_features:
        stage_context += f"\nLLM Features: Generated for 3 propensity models"
    elif conversation_state.conversation_stage == "user_features" and conversation_state.user_suggested_features:
        stage_context += f"\nUser Features: {len(conversation_state.user_suggested_features)} suggested"
    elif conversation_state.conversation_stage == "confirmation" and conversation_state.final_feature_list:
        stage_context += f"\nConfirmed Features: {len(conversation_state.final_feature_list)} total features"
    elif conversation_state.conversation_stage == "engineering" and conversation_state.glue_jobs_created:
        stage_context += f"\nGlue Jobs: {len(conversation_state.glue_jobs_created)} created"
    
    # Add available actions based on current stage
    if conversation_state.conversation_stage == "initial":
        stage_context += "\nNext: Use explore_s3_data to analyze your raw data"
    elif conversation_state.conversation_stage == "s3_exploration":
        stage_context += "\nNext: Use generate_llm_features to get AI-generated feature suggestions"
    elif conversation_state.conversation_stage == "llm_features":
        stage_context += "\nNext: Review LLM features and use add_user_suggested_feature to add your own"
    elif conversation_state.conversation_stage == "user_features":
        stage_context += "\nNext: Use confirm_final_feature_list to finalize your feature selection"
    elif conversation_state.conversation_stage == "confirmation":
        stage_context += "\nNext: Use create_glue_job_with_confirmed_features to build the data pipeline"
    elif conversation_state.conversation_stage == "engineering":
        stage_context += "\nNext: Use run_glue_job to execute feature engineering, then train_propensity_models for ML training (specify model_type: churn, call, or spend_change)"
    
    # Invoke the agent with enhanced context
    try:
        # Combine instructions with user message and context
        full_message = f"{AGENT_INSTRUCTIONS}\n\n{user_message}{stage_context}"
        
        result = await feature_agent.invoke_async(
            full_message,
            session_id=session_id
        )
        
        return {
            "response": result.message,
            "conversation_stage": conversation_state.conversation_stage,
            "session_id": session_id,
            "available_data": {
                "s3_explored": conversation_state.raw_data_analysis is not None,
                "llm_features_generated": conversation_state.llm_suggested_features is not None,
                "user_features_count": len(conversation_state.user_suggested_features),
                "final_features_count": len(conversation_state.final_feature_list),
                "glue_jobs_count": len(conversation_state.glue_jobs_created)
            }
        }
        
    except Exception as e:
        return {
            "error": f"Agent invocation failed: {str(e)}",
            "conversation_stage": conversation_state.conversation_stage,
            "session_id": session_id
        }

if __name__ == "__main__":
    app.run()
