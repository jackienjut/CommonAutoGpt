from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool , tool
import calendar
import dateutil.parser as parser
from datetime import date
from langchain import hub
import json


search = SerpAPIWrapper(serpapi_api_key = "b1ff9aabdc216571761fec93cb536b7e3dbf8a59b77365f887edbd80a387d2ad")
tools = [
    Tool.from_function(
        func=search.run,
        name = "search",
        description="useful for when you need to answer the question"
    )
]

@tool("weekday")
def weekday(date_str: str) -> str:
    """Convert date to weekday name"""
    d = parser.parse(date_str)
    return calendar.day_name[d.weekday()]

tools += [weekday]

prompt = hub.pull("hwchase17/react")

print(prompt.template)