from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

#CREATING CHATBOT

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an ai assistant. Please try to answer the questions to the best of your abilities"),
    ("user", "Question:{question}")
])

#Streamlit Framework

st.title("A chatbot using the LLama2 model and Langchain Framework")
input_text = st.text_input("Search the topic you want")

#Ollama Api call
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

#Chaining

chain = prompt|llm|output_parser

if(input_text):
    st.write(chain.invoke({'question':input_text}))