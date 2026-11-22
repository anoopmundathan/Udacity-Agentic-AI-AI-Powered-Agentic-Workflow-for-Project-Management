from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
augmented_agent_response = augmented_agent.respond(prompt)

print(augmented_agent_response)

# Knowledge used: the agent relies on the LLM's general pre-trained knowledge (that Paris is the
# capital of France); no extra knowledge is supplied.
# Effect of the persona: the system prompt makes the model adopt the college professor role and
# follow its rule, so the answer starts with "Dear students," and is phrased as a lecture, while
# the factual content stays the same as with a direct prompt.
