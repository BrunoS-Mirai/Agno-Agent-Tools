from dotenv import load_dotenv
load_dotenv()

from agno.models.groq import Groq
from agno.agent import Agent

#Tool.
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model = Groq(id="openai/gpt-oss-20b"),
    tools=[YFinanceTools()],

    #Will be "added" to prompt automatically.
    instructions="Use tables to display the final information. Do not include any other text"
)

agent.print_response("Use your tools to display the current stock prices for the following: Itaú, Santander, Banco do Brasil, and Nubank", stream=True)
#stream=True make the agent show the response while he builds.