from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k

import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

agent = Agent(
    model = Gemini(id="gemini-1.5-flash"),
    tools = [DuckDuckGo()],
    description = "You are senior Hindustan Times reaseacher writing an article on topic.",
    instruction = [
        "For a given topic search for top 5 links",
        "Then read each URL and extract the article text, if a URL isn't available ignore it.",
        "Analyse and prepare an Hindustan Times worthy article on the information."
    ],
    markdown = True,
    show_tool_calls = True,
    add_datetime_to_instructions = True,
)

agent.print_response("Trending Topic in India?", stream=True)