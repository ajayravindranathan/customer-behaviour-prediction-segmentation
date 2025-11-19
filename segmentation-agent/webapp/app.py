import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import boto3
import os
import subprocess

st.set_page_config(page_title="Customer Segmentation Agent", layout="wide")

# Initialize session state with environment variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "s3_uri" not in st.session_state:
    s3_bucket = os.environ.get('S3_BUCKET', '')
    s3_key = os.environ.get('S3_KEY', 'data/customer_data.csv')
    if s3_bucket and s3_key:
        st.session_state.s3_uri = f"s3://{s3_bucket}/{s3_key}"
    else:
        st.session_state.s3_uri = ""

def parse_s3_uri(s3_uri):
    """Parse S3 URI into bucket and key components"""
    if not s3_uri or not s3_uri.startswith('s3://'):
        return None, None
    
    # Remove s3:// prefix and split on first /
    path = s3_uri[5:]  # Remove 's3://'
    if '/' not in path:
        return path, None
    
    bucket, key = path.split('/', 1)
    return bucket, key

def invoke_agent(prompt, s3_bucket=None, s3_key=None):
    """Invoke the segmentation agent using agentcore CLI"""
    import subprocess
    import json
    import re
    
    try:
        payload = {"prompt": prompt}
        if s3_bucket:
            payload["s3_bucket"] = s3_bucket
        if s3_key:
            payload["s3_key"] = s3_key
            
        result = subprocess.run([
            'agentcore', 'invoke', 
            json.dumps(payload)
        ], capture_output=True, text=True, check=True, cwd="../")
        
        # Extract JSON from the response section
        output = result.stdout
        response_match = re.search(r'Response:\s*(\{.*\})\s*$', output, re.DOTALL)
        if response_match:
            json_str = response_match.group(1).strip()
            json_str = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_str)
            response_data = json.loads(json_str)
            return response_data
        else:
            return {"result": {"content": [{"text": "No JSON response found in output"}]}}
            
    except subprocess.CalledProcessError as e:
        return {"result": {"content": [{"text": f"Error invoking agent: {e.stderr}"}]}}
    except json.JSONDecodeError as e:
        return {"result": {"content": [{"text": f"Error parsing JSON response: {e}"}]}}
    except Exception as e:
        return {"result": {"content": [{"text": f"Unexpected error: {str(e)}"}]}}

def extract_chart_data_with_claude(response_text):
    """Use Claude 3.7 to extract chart-relevant data from agent response"""
    try:
        aws_region = os.environ.get('AWS_REGION', 'us-east-1')
        bedrock = boto3.client('bedrock-runtime', region_name=aws_region)
        
        prompt = f"""
        Analyze the following customer segmentation analysis and extract structured data for creating charts.
        
        Response text:
        {response_text}
        
        Extract and return ONLY a JSON object with the following structure:
        {{
            "chart_type": "bar|pie|line|scatter",
            "title": "Chart title",
            "data": [
                {{"label": "Category1", "value": 123, "percentage": 45.2}},
                {{"label": "Category2", "value": 456, "percentage": 54.8}}
            ],
            "x_axis": "X-axis label",
            "y_axis": "Y-axis label",
            "insights": ["Key insight 1", "Key insight 2"]
        }}
        
        Focus on extracting:
        - Customer counts by location/geography
        - Percentages and proportions
        - Churn rates by category
        - Spending amounts by segment
        - Any numerical data suitable for visualization
        
        Return only valid JSON, no other text.
        """
        
        response = bedrock.invoke_model(
            modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "messages": [{"role": "user", "content": prompt}]
            })
        )
        
        result = json.loads(response['body'].read())
        claude_response = result['content'][0]['text']
        
        # Clean up the response to extract just the JSON
        claude_response = claude_response.strip()
        
        # Find JSON object in the response
        start_idx = claude_response.find('{')
        end_idx = claude_response.rfind('}') + 1
        
        if start_idx != -1 and end_idx > start_idx:
            json_str = claude_response[start_idx:end_idx]
            return json.loads(json_str)
        else:
            st.error("No valid JSON found in Claude response")
            return None
        
    except json.JSONDecodeError as e:
        st.error(f"JSON parsing error: {e}")
        return None
    except Exception as e:
        st.error(f"Error extracting chart data with Claude: {e}")
        return None

def create_plotly_chart(chart_data):
    """Create Plotly chart from extracted data"""
    if not chart_data or 'data' not in chart_data:
        return None
    
    try:
        data = chart_data['data']
        chart_type = chart_data.get('chart_type', 'bar')
        title = chart_data.get('title', 'Customer Analysis')
        
        # Create DataFrame
        df = pd.DataFrame(data)
        
        # Ensure required columns exist
        if 'label' not in df.columns or 'value' not in df.columns:
            return None
        
        if chart_type == 'bar':
            # Handle missing percentage column
            text_labels = []
            for _, row in df.iterrows():
                value = row['value']
                percentage = row.get('percentage', 0)
                if percentage and percentage > 0:
                    text_labels.append(f"{value:,} ({percentage:.1f}%)")
                else:
                    text_labels.append(f"{value:,}")
            
            fig = go.Figure(data=[
                go.Bar(
                    x=df['label'],
                    y=df['value'],
                    text=text_labels,
                    textposition='outside',
                    marker_color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'][:len(df)]
                )
            ])
            
            fig.update_layout(
                title=title,
                xaxis_title=chart_data.get('x_axis', 'Category'),
                yaxis_title=chart_data.get('y_axis', 'Count'),
                plot_bgcolor='white',
                font=dict(size=12)
            )
            
        elif chart_type == 'pie':
            fig = go.Figure(data=[
                go.Pie(
                    labels=df['label'],
                    values=df['value'],
                    textinfo='label+percent',
                    textposition='outside'
                )
            ])
            
            fig.update_layout(title=title)
            
        else:  # Default to bar chart
            fig = px.bar(df, x='label', y='value', title=title)
        
        return fig
        
    except Exception as e:
        st.error(f"Error creating chart: {e}")
        return None

# UI Layout
st.title("🎯 Customer Segmentation Agent")
st.markdown("Chat with the AI agent to analyze customer data and generate insights with AI-powered visualizations.")

# Initialize session ID
if 'session_id' not in st.session_state:
    st.session_state.session_id = f"webapp-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

# S3 Configuration Sidebar
st.sidebar.header("📁 Data Source Configuration")
st.session_state.s3_uri = st.sidebar.text_input(
    "S3 URI", 
    value=st.session_state.s3_uri,
    help="S3 URI to the CSV file (e.g., s3://bucket-name/path/to/file.csv)",
    placeholder="s3://your-bucket/path/to/data.csv"
)

# Parse S3 URI for display
s3_bucket, s3_key = parse_s3_uri(st.session_state.s3_uri)

# Display agent status
st.sidebar.success(f"✅ Connected to Agent via CLI")
st.sidebar.text("Using agentcore invoke")
if s3_bucket and s3_key:
    st.sidebar.text(f"Data: {st.session_state.s3_uri}")
else:
    st.sidebar.warning("⚠️ Invalid S3 URI format")

# Chat interface
st.subheader("💬 Chat History")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "charts" in message:
            for i, chart in enumerate(message["charts"]):
                st.plotly_chart(chart, width='stretch', key=f"history_chart_{hash(str(message))}_{i}")
        if "insights" in message:
            with st.expander("📊 Key Insights"):
                for insight in message["insights"]:
                    st.write(f"• {insight}")

# Process any unprocessed user messages (from buttons or chat input)
if 'processed_count' not in st.session_state:
    st.session_state.processed_count = 0

# Check if there are new user messages to process
user_messages = [msg for msg in st.session_state.messages if msg["role"] == "user"]
if len(user_messages) > st.session_state.processed_count:
    # Get the latest unprocessed user message
    latest_user_msg = user_messages[-1]
    prompt = latest_user_msg["content"]
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing data..."):
            s3_bucket, s3_key = parse_s3_uri(st.session_state.s3_uri)
            response = invoke_agent(prompt, s3_bucket, s3_key)
            
            # Extract content from the response
            if isinstance(response.get("result"), dict) and "content" in response["result"]:
                content_list = response["result"]["content"]
                if content_list and isinstance(content_list, list):
                    content = content_list[0].get("text", "No response")
                else:
                    content = "No response content found"
            else:
                content = str(response.get("result", "No response"))
            
            st.write(content)
            
            # Extract chart data using Claude
            with st.spinner("Generating visualization..."):
                chart_data = extract_chart_data_with_claude(content)
                
                charts = []
                insights = []
                
                if chart_data:
                    # Create Plotly chart
                    fig = create_plotly_chart(chart_data)
                    if fig:
                        charts.append(fig)
                        st.plotly_chart(fig, width='stretch', key=f"chart_{len(st.session_state.messages)}")
                    
                    # Display insights
                    if 'insights' in chart_data:
                        insights = chart_data['insights']
                        with st.expander("📊 Key Insights"):
                            for insight in insights:
                                st.write(f"• {insight}")
                else:
                    st.info("No chart data could be extracted from the response.")
            
            # Save message with charts and insights
            message_data = {
                "role": "assistant", 
                "content": content,
                "timestamp": datetime.now().isoformat()
            }
            if charts:
                message_data["charts"] = charts
            if insights:
                message_data["insights"] = insights
            
            st.session_state.messages.append(message_data)
            st.session_state.processed_count = len(user_messages)

# Chat input
if prompt := st.chat_input("Ask about customer segmentation, churn analysis, or insights..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# Sidebar with sample questions
st.sidebar.title("📊 Sample Questions")
sample_questions = [
    "Create a graph of customers by location",
    "Show me customer churn analysis",
    "What are the key customer segments?",
    "Analyze spending patterns by demographics",
    "Which factors predict customer churn?"
]

for question in sample_questions:
    if st.sidebar.button(question, key=f"sample_{hash(question)}"):
        st.session_state.messages.append({"role": "user", "content": question})
        st.rerun()

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Session info
st.sidebar.markdown("---")
st.sidebar.text(f"Session: {st.session_state.session_id}")
st.sidebar.text("🤖 Powered by Claude 3.7 + AgentCore")
