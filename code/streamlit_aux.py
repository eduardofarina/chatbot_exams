# code/streamlit_aux.py
import streamlit as st
# You would need to ensure StreamlitWhisperApp is correctly defined or imported here
# from your_whisper_implementation import StreamlitWhisperApp 

class Streamlit:
    def __init__(self):
        # --- STREAMLIT PAGE CONFIG ---
        st.set_page_config(
            layout="wide", # Or "centered" if preferred for a chatbot
            page_title="AI Copilot Chat",
            initial_sidebar_state="collapsed"
        )
        
        # --- Initialize Voice Input Handler (if needed) ---
        # Make sure StreamlitWhisperApp is available
        # self.whisper_app = StreamlitWhisperApp() 
        print("Streamlit Aux Initialized (Page Config Set)")
