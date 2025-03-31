# code/llm.py
import os
import json

from prompts import Prompts

from agno.models.google import Gemini
from agno.models.ollama import Ollama
from agno.models.groq import Groq
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
# This import is now safe
from agents import PathologyAgent, GeneticAgent, RadiologyAgent, LaboratoryAgent, ReportAnalyzerAgent

prompts = Prompts()

class LLM:
    def __init__(self):
        # Initialize the model once here
        self.model = Groq(api_key=os.environ.get("GROQ_API_KEY"), id="llama-3.2-1b-preview") # Changed model ID as llama-3.3 isn't listed typically

    def get_last_response(self, response):
        # Handle different response types
        if hasattr(response, 'messages') and response.messages:
            last_message = response.messages[-1]
            if hasattr(last_message, 'content'):
                # Try to parse JSON if it's a string that looks like JSON
                try:
                    if isinstance(last_message.content, str) and last_message.content.strip().startswith('['):
                        parsed_content = json.loads(last_message.content)
                        return json.dumps(parsed_content, indent=2)
                except:
                    pass # Ignore parsing errors, return original content
                return last_message.content
        return str(response) # Fallback


    def agent(self):
        instruction = prompts.get_prompt()

        # Instantiate tools and pass the initialized model
        tools_list = [
            DuckDuckGoTools(), 
            # Assuming ReportAnalyzerAgent also needs the model
            ReportAnalyzerAgent(model=self.model), 
            PathologyAgent(model=self.model), 
            GeneticAgent(model=self.model), 
            RadiologyAgent(model=self.model), 
            LaboratoryAgent(model=self.model)
        ]

        new_agent = Agent(
            name="Web Agent",
            model=self.model, # The main agent uses the model directly
            tools=tools_list, # Pass the initialized tools
            markdown=True,
            read_tool_call_history=True,
            tool_call_limit=3, # Adjust as needed
            add_history_to_messages=True,
            num_history_responses=3, # Adjust as needed
            description="AI Copilot Agent", # Add a description if desired
            instructions=instruction,
            reasoning=False, # Set to True to see detailed reasoning if needed
            debug_mode=False
        )
        return new_agent