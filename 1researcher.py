#Agent with internet search tool.

from dotenv import load_dotenv
load_dotenv()

from agno.models.groq import Groq

from agno.agent import Agent

#Tool
from agno.tools.tavily import TavilyTools

agent = Agent(
    model = Groq(id="openai/gpt-oss-20b"),
    tools=[TavilyTools()],
    debug_mode=True #Make the agent show the process.
)

agent.print_response("Use your tools to search what is Agno framework")