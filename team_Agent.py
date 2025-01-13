from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name = "web_Agent",
    model = Groq(id='llama-3.3-70b-versatile'),
    tools =[DuckDuckGo],
    instructions = ['Always include sources'],
    show_tools_class = True,
    markdown = True,
)

finanace_agent = Agent(
  name ='fianace_agent',
  role ='Get finanacial data', 
  model = Groq(id='llama-3.3-70b-versatile'),
  tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
  show_tool_calls= True,
  markdown = True,
  instructions = ['Show tables to display data']
    )
agent_team = Agent(
    team = [web_agent, finanace_agent],
    model = Groq(id='llama-3.3-70b-versatile'),
    instructions = ['Always include Sources', 'Use Tables to display data'],
    show_tool_calls= True,
    markdown = True
)

agent_team.print_response("Summarize and compare analyst recomandations and share the latest news NVDIA", stream = True)

