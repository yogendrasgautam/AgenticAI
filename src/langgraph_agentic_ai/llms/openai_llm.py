import os
from langchain_openai import ChatOpenAI
import streamlit as st

class OpenAiLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key=self.user_controls_input['OPENAI_API_KEY']
            selected_openai_model=self.user_controls_input['selected_openai_model']
            if openai_api_key=='' and os.environ["GROQ_API_KEY"] =='':
                st.error("Please Enter the Groq API KEY")
            print("Open AI API Key:", openai_api_key)
            print("Selected Model:", selected_openai_model)
            if not openai_api_key:
                raise ValueError("OpenAI API key is missing.")
            if not selected_openai_model:
                raise ValueError("Selected OpenAI model is missing.")
            llm = ChatOpenAI(api_key=openai_api_key, model=selected_openai_model)

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
        return llm