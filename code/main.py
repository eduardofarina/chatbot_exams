import time
import os
import pandas as pd

import streamlit as st
from streamlit_aux import Streamlit
from datetime import datetime

# start up streamlit config first
st_aux = Streamlit()

from llm import LLM
from prompts import Prompts

prompts = Prompts()
llm = LLM()

# --- Initialize Session State ---
if "history" not in st.session_state:
    st.session_state.history = []
if "processing" not in st.session_state:
    st.session_state.processing = False
if "agent" not in st.session_state:
    # Initialize the main agent responsible for handling chat and dispatching to tools
    st.session_state.agent = llm.agent() 
if "enable_tts" not in st.session_state:
    st.session_state.enable_tts = False # Default to text, enable on voice input

# --- UI Configuration ---
# Reduced height as other elements are removed
container_height = 600 

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ">>> Streamlit CHATBOT app reloading.")

# --- Main Chatbot Interface ---
st.subheader("🤖 Assistente de Laudos")

# Container for chat messages
with st.container(height=container_height):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Carregando mensagens do histórico.")
    # Display chat history
    for interaction in st.session_state.history:
        if interaction.get("user_message"):
            st.chat_message("user").write(interaction["user_message"])

        if interaction.get("assistant_message"):
            with st.chat_message("assistant"):
                st.write(interaction["assistant_message"])
               

    # Handle agent processing when a new message is submitted
    if st.session_state.processing:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Processing status is True")
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                max_try = 3
                current_try = 0
                assistant_message = "Sorry, I encountered an error." # Default error message
                reasoning = None # Default reasoning

                while current_try < max_try:
                    try:
                        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Running agent (Attempt {current_try + 1}/{max_try})...")
                        
                        # Get the last user message to send to the agent
                        last_user_message = ""
                        if st.session_state.history:
                             last_user_message = st.session_state.history[-1].get("user_message", "")
                        
                        if not last_user_message:
                             print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Error: No user message found in history to process.")
                             assistant_message = "Error: Could not find the message to process."
                             break # Exit loop if no message found

                        response = st.session_state["agent"].run(last_user_message)
                        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Agent run completed.")
                        
                        # Extract response and reasoning (assuming llm methods handle this)
                        assistant_message = llm.get_last_response(response) 
                        # If you want reasoning display, uncomment the line below 
                        # and ensure get_reasoning_messages exists and works
                        # reasoning = llm.get_reasoning_messages(response) 

                        # Process with speech if enabled for this interaction
                        if st.session_state.get("enable_tts", False):
                            print("TTS enabled. Converting response to speech...")
                            tts.convert_tts(assistant_message)
                            print("TTS conversion done.")

                        # Success, break the loop
                        break 

                    except Exception as e:
                        print(f"Error during agent processing (Attempt {current_try + 1}): {e}")
                        time.sleep(2) # Wait before retrying
                        current_try += 1
                        assistant_message = f"An error occurred: {e}" # Update error message
                        if current_try == max_try:
                            print(f"Max retries reached. Agent failed.")
                            # Keep the last error message
                        continue # Go to the next retry

                # Update history with the final result (message or error)
                if st.session_state.history: # Ensure history exists
                     st.session_state.history[-1]["assistant_message"] = assistant_message
                     # Uncomment if reasoning is used
                     # st.session_state.history[-1]["reasoning"] = reasoning
                
                st.session_state.processing = False # Mark processing as done
                st.session_state.enable_tts = False # Reset TTS flag for next interaction
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Processing finished. Rerunning.")
                st.rerun() # Rerun to display the new message

# --- Input Handling ---
if not st.session_state.processing:
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Ready for input.")
    
    # Text Input
    if prompt := st.chat_input("💬 Ask the AI Copilot..."):
        st.session_state.history.append({
            "user_message": prompt,
            "assistant_message": None,
            "reasoning": None
        })
        st.session_state.processing = True
        st.session_state.enable_tts = False # Text input defaults to no TTS output
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Text input received. Rerunning for processing.")
        st.rerun()
