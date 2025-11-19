import streamlit as st
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

class AgentClient:
    def __init__(self):
        self.client = boto3.client('bedrock-agentcore', region_name=AWS_REGION)
        if 'session_id' not in st.session_state:
            st.session_state.session_id = f"webapp-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def invoke(self, prompt):
        payload = {"prompt": prompt, "session_id": st.session_state.session_id}
        try:
            response = self.client.invoke_agent_runtime(
                agentRuntimeArn=AGENT_ARN,
                runtimeSessionId=st.session_state.session_id + "0" * (33 - len(st.session_state.session_id)),
                payload=json.dumps(payload),
                qualifier="DEFAULT"
            )
            return json.loads(response['response'].read())
        except Exception as e:
            return {"error": str(e)}

def main():
    st.set_page_config(page_title="BT Migration Customer Behaviour Prediction Automation Agent", layout="wide")
    
    st.title("🚀 BT Migration Customer Behaviour Prediction Automation Agent")
    st.markdown("Build features for migration propensity models using AI")
    
    # Initialize client
    if 'client' not in st.session_state:
        st.session_state.client = AgentClient()
    
    # Initialize conversation history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar for S3 configuration
    with st.sidebar:
        st.header("📁 S3 Configuration")
        
        input_s3 = st.text_input(
            "Input S3 Path", 
            placeholder="s3://bucket/raw-data/",
            help="S3 prefix containing raw customer data"
        )
        
        output_s3 = st.text_input(
            "Output S3 Path", 
            placeholder="s3://bucket/features/",
            help="S3 prefix for engineered features"
        )
        
        st.header("🎯 Propensity Models")
        st.info("**Call Propensity**: Support contact likelihood\n\n**Churn Propensity**: Service cancellation likelihood\n\n**Spend Change**: Spending pattern changes")
        
        # Quick actions
        st.header("⚡ Quick Actions")
        if st.button("🔍 Explore S3 Data") and input_s3:
            prompt = f"Please explore the customer data at {input_s3}"
            response = st.session_state.client.invoke(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("🤖 Generate LLM Features"):
            prompt = "Generate feature suggestions using the LLM based on our data analysis"
            response = st.session_state.client.invoke(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("✅ Confirm Features"):
            prompt = "Confirm final feature list: top 3 LLM features per model + all user features + raw columns"
            response = st.session_state.client.invoke(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("⚙️ Create Glue Job") and output_s3:
            prompt = f"Create Glue job 'webapp-features-{datetime.now().strftime('%Y%m%d')}' outputting to {output_s3}"
            response = st.session_state.client.invoke(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("▶️ Run Glue Job"):
            prompt = f"Run Glue job 'webapp-features-{datetime.now().strftime('%Y%m%d')}'"
            response = st.session_state.client.invoke(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        # Model training with specific model selection
        st.subheader("🤖 Train ML Models")
        model_type = st.selectbox(
            "Select Model Type",
            ["churn", "call", "spend_change"],
            format_func=lambda x: {
                "churn": "Churn Propensity (cancellation likelihood)",
                "call": "Call Propensity (support contact likelihood)", 
                "spend_change": "Spend Change Propensity (spending pattern changes)"
            }[x]
        )
        
        if st.button("🚀 Train Selected Model") and output_s3 and model_type:
            prompt = f"Train {model_type} propensity model using features from {output_s3}"
            response = st.session_state.client.invoke(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Main chat interface
    st.header("💬 Conversation")
    
    # Display conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                response = message["content"]
                if "error" in response:
                    st.error(f"Error: {response['error']}")
                else:
                    # Extract text from content[0]["text"] if available
                    if "content" in response and len(response["content"]) > 0 and "text" in response["content"][0]:
                        st.markdown(response["content"][0]["text"])
                    else:
                        st.write(response.get("response", "No response"))
                    
                    # Show stage and data status
                    if "conversation_stage" in response:
                        st.caption(f"Stage: {response['conversation_stage']}")
                    
                    if "available_data" in response:
                        data = response["available_data"]
                        cols = st.columns(7)
                        cols[0].metric("S3 Explored", "✅" if data.get("s3_explored") else "❌")
                        cols[1].metric("LLM Features", "✅" if data.get("llm_features_generated") else "❌")
                        cols[2].metric("User Features", data.get("user_features_count", 0))
                        cols[3].metric("Final Features", data.get("final_features_count", 0))
                        cols[4].metric("Glue Jobs", data.get("glue_jobs_count", 0))
                        cols[5].metric("Jobs Running", data.get("jobs_running", 0))
                        cols[6].metric("Models Trained", data.get("models_trained", 0))
            else:
                st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about customer behaviour prediction..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Processing..."):
                response = st.session_state.client.invoke(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                if "error" in response:
                    st.error(f"Error: {response['error']}")
                else:
                    # Extract text from content[0]["text"] if available
                    if "content" in response and len(response["content"]) > 0 and "text" in response["content"][0]:
                        st.markdown(response["content"][0]["text"])
                    else:
                        st.write(response.get("response", "No response"))
                    
                    # Show stage and data status
                    if "conversation_stage" in response:
                        st.caption(f"Stage: {response['conversation_stage']}")
                    
                    if "available_data" in response:
                        data = response["available_data"]
                        cols = st.columns(7)
                        cols[0].metric("S3 Explored", "✅" if data.get("s3_explored") else "❌")
                        cols[1].metric("LLM Features", "✅" if data.get("llm_features_generated") else "❌")
                        cols[2].metric("User Features", data.get("user_features_count", 0))
                        cols[3].metric("Final Features", data.get("final_features_count", 0))
                        cols[4].metric("Glue Jobs", data.get("glue_jobs_count", 0))
                        cols[5].metric("Jobs Running", data.get("jobs_running", 0))
                        cols[6].metric("Models Trained", data.get("models_trained", 0))

if __name__ == "__main__":
    main()
