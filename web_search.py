import os
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[DuckDuckGo()],
    search = True,
    news = True,
    description = "You are an assistant doing web search",
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    debug_mode = True
)
web_agent.print_response("What is CEO of TESLA? and tell me about it in briefly", stream=True)
