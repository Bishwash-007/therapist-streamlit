from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv('.env')
## Prompt template
prompt = ChatPromptTemplate(
    input_variables=["question"],
    messages=[
        ("system", 
         "You are a professional therapist. "
         "Respond to the user's queries with empathy, understanding, and professionalism. "
         "Provide thoughtful guidance, but do not give medical or psychiatric prescriptions. "
         "Encourage reflection and offer coping strategies where appropriate."),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title('Therapist demo with openAI API')
input_text = st.text_input('please unload your mind')



llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))