#AGENT WITH CREATED TOOL.

from dotenv import load_dotenv
load_dotenv()

from agno.models.groq import Groq
from agno.agent import Agent
from agno.tools.tavily import TavilyTools

#Created tool
def Fah_to_cel (temp_Fahrenheit: float):
    #Docstring
    """
    Convert temperature in Fahrenheit to Celsius.
    
    Args:
        temp_Fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted in Celsius degrees.
    """
    return (temp_Fahrenheit - 32) * 1.8 

#Structure of docstring
    #What the tool make

    #Args: All parameters of function in following model:
    # PARAMETER (TYPE): EXPLAINED WHAT IS

    #Explained return


agent = Agent(
    model = Groq(id="openai/gpt-oss-20b"),
    tools=[TavilyTools(), Fah_to_cel],
    debug_mode=True
)

agent.print_response("Use your tools to search which temperature in São Paulo (Brazil) in Fahrenheit and convert it to Celsius")