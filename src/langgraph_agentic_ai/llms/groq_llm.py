import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls["GROQ_API_KEY"]
            selected_groq_model = self.user_controls["selecte_groq_model"]
            llm = ChatGroq(groq_api_key, selected_groq_model)

        except Exception as e:
            st.write(f"Error: {e}")
            
        return llm