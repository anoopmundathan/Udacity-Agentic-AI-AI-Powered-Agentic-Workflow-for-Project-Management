# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

direct_agent = DirectPromptAgent(openai_api_key)
direct_agent_response = direct_agent.respond(prompt)

print(direct_agent_response)

print(
    "\nKnowledge source: the DirectPromptAgent sends the prompt straight to the LLM with no system "
    "prompt, so the answer comes solely from the general knowledge learned by the gpt-4o-mini model "
    "during training."
)
