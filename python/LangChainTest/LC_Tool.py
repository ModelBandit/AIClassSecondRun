from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4.1-nano", openai_api_key=key)


from langchain_core.tools import tool
from datetime import datetime
import pytz

@tool
def get_current_time(timezone:str,location:str)->str:
    """현재시간 반환 (이렇게 앞쪽에 설명안써주면 에러뜸)
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    location_and_local_time = f"{timezone} ({location}) 현재시각 {now}"
    print(location_and_local_time)
    return location_and_local_time

tools = [get_current_time,]
tool_dict = {"get_current_time":get_current_time,}

llm_with_tools = llm.bind_tools(tools)

messages = [
    SystemMessage("너는 사용자의 질문에 답변을 하기 위해 tools를 사용할 수 있다."),
    HumanMessage("부산은 지금 몇시야?")
]

response = llm_with_tools.invoke(messages)
# 원래대로면 content에 답변이 와야하지만 비어있음
messages.append(response)

for tool_call in response.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    print(tool_call["args"])
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)
print(messages)
print(llm_with_tools.invoke(messages))

