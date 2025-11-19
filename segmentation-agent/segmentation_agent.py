import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from bedrock_agentcore.tools.code_interpreter_client import CodeInterpreter
from strands import Agent, tool
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp
import json
import boto3
from typing import Dict, Any

# Initialize Code Interpreter with configurable region
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
code_client = CodeInterpreter(AWS_REGION)

def load_s3_data(bucket: str = None, key: str = None) -> str:
    """Load customer data from S3 and return as string"""
    try:
        s3 = boto3.client('s3')
        # Use provided parameters or environment variables
        bucket = bucket or os.environ.get('S3_BUCKET')
        key = key or os.environ.get('S3_KEY', 'data/customer_data.csv')
        
        obj = s3.get_object(Bucket=bucket, Key=key)
        return obj['Body'].read().decode('utf-8')
    except Exception as e:
        print(f"Error loading S3 data: {e}")
        return ""

def call_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function to invoke sandbox tools"""
    response = code_client.invoke(tool_name, arguments)
    for event in response["stream"]:
        return json.dumps(event["result"])

def setup_sandbox_data(bucket: str = None, key: str = None):
    """Load S3 data and write to sandbox environment"""
    # Load customer data from S3
    data_file_content = load_s3_data(bucket, key)
    
    if not data_file_content:
        return False
        return False
    
    # Prepare files for sandbox environment
    files_to_create = [{
        "path": "customer_data.csv",
        "text": data_file_content
    }]
    
    # Write files to sandbox
    writing_files = call_tool("writeFiles", {"content": files_to_create})
    print("Writing files result:")
    print(writing_files)
    
    # Verify files were created
    listing_files = call_tool("listFiles", {"path": ""})
    print("\nFiles in sandbox:")
    print(listing_files)
    
    return True

# System prompt following the sample pattern
SYSTEM_PROMPT = """You are a customer segmentation analyst. Use the execute_python tool to analyze customer data and create visualizations.

Key Guidelines:
1. The customer data is available as 'customer_data.csv' in the sandbox
2. Use pandas for data analysis and plotly for visualizations
3. Always execute code to validate your analysis
4. Provide clear insights and recommendations

Available tool: execute_python - Run Python code in the sandbox environment."""

@tool
def execute_python(code: str, description: str = "") -> str:
    """Execute Python code in the sandbox for customer segmentation analysis."""
    
    if description:
        code = f"# {description}\n{code}"
    
    print(f"\nGenerated Code: {code}")
    
    try:
        # Execute code using Code Interpreter client
        response = code_client.invoke("executeCode", {
            "code": code,
            "language": "python",
            "clearContext": False
        })
        
        # Process the streaming response
        result = None
        for event in response["stream"]:
            result = event["result"]
            break  # Take the first result
        
        if result:
            # Extract the actual output from the result
            if result.get("isError", False):
                error_msg = "Error occurred during code execution"
                if "content" in result and result["content"]:
                    error_msg = result["content"][0].get("text", error_msg)
                return f"Error: {error_msg}"
            else:
                # Return successful output
                if "content" in result and result["content"]:
                    return result["content"][0].get("text", "Code executed successfully")
                elif "structuredContent" in result:
                    return result["structuredContent"].get("stdout", "Code executed successfully")
                else:
                    return "Code executed successfully"
        else:
            return "No result received from code execution"
            
    except Exception as e:
        return f"Error executing code: {str(e)}"

# Initialize model and agent following the sample pattern
model_id = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
model = BedrockModel(model_id=model_id)

agent = Agent(
    model=model,
    tools=[execute_python],
    system_prompt=SYSTEM_PROMPT,
    callback_handler=None
)

# AgentCore app setup
app = BedrockAgentCoreApp()

@app.entrypoint
def agent_invocation(payload, context):
    """Handler for agent invocation following the sample pattern"""
    try:
        # Start code interpreter session with extended timeout
        code_client.start(session_timeout_seconds=1200)
        
        # Get S3 parameters from payload
        s3_bucket = payload.get("s3_bucket")
        s3_key = payload.get("s3_key")
        
        # Setup sandbox data from S3
        if not setup_sandbox_data(s3_bucket, s3_key):
            return {"result": "Error: Could not load customer data from S3"}
        
        # Get user message
        user_message = payload.get("prompt", "Show me the first 10 rows of customer data")
        
        # Invoke agent synchronously
        result = agent(user_message)
        
        return {"result": result.message}
        
    except Exception as e:
        return {"result": f"Error processing request: {str(e)}"}
    finally:
        # Clean up code interpreter session
        try:
            code_client.stop()
        except:
            pass

if __name__ == "__main__":
    app.run()
