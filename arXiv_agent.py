import os
import streamlit as st
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.llms import OpenAI
import time
import pyperclip as pc
from datetime import datetime

# Streamlit sidebar for API key and model selection
st.sidebar.title("API Key & Model Selection")
model_choice = st.sidebar.selectbox("Choose a Provider:", ["Google AI", "OpenAI"])
api_key = st.sidebar.text_input("Enter your API key:")

if model_choice == "Google AI":
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    else:
        st.warning("Please provide a Google AI API key.")
        st.stop()
elif model_choice == "OpenAI":
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        st.warning("Please provide an OpenAI API key.")
        st.stop()

# Model selection within each provider
if model_choice == "Google AI":
    google_model_choice = st.sidebar.selectbox("Choose a Google AI Model:", ["gemini-1.5-pro","gemini-1.0-pro"])  # Add more Google models if needed
    llm = ChatGoogleGenerativeAI(
        model=google_model_choice,
        temperature=0,
        max_tokens=500,
        timeout=None,
        max_retries=2,
    )
elif model_choice == "OpenAI":
    openai_model_choice = st.sidebar.selectbox("Choose an OpenAI Model:", ["gpt-3.5-turbo", "text-davinci-003"])  # Add more OpenAI models if needed
    llm = OpenAI(temperature=0, model_name=openai_model_choice)

# Load tools and prompt
tools = load_tools(["arxiv"])
prompt = hub.pull("hwchase17/react")

# Create Langchain agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# Streamlit interface and processing
st.title("ARXIV Assistant : ")

INSTRUCTIONS = "Your answer should have citations from the Papers that you referred."
user_query = st.text_input("Ask me about Anything and I will answer with credible sources :")

if st.button("Ask"):
    with st.spinner("Thinking... 🧠"):
        t1 = datetime.now()
        result = agent_executor.invoke(
            {
                "input": user_query + INSTRUCTIONS,
            },return_only_outputs=True
        )
        
        # Display in a text area
        st.write(result["output"])
        time_taken = datetime.now() - t1
        # datetime(time_taken)
        st.success(f"Fetched results in {time_taken.seconds}:{time_taken.microseconds} Seconds.")

    
            