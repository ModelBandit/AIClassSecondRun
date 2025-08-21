from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("OPENAI_API_KEY")
model =ChatOpenAI(model="gpt-4.1-nano", openai_api_key=key)
store = {}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

with_message_history = RunnableWithMessageHistory(model, get_session_history)

config = {"configurable": {"session_id":"abc2"}}

response = with_message_history.invoke(
    [HumanMessage(content="내 이름은 이성용이야")],
    config=config,
)
print(response.content)

for r in with_message_history.stream(
    [HumanMessage(content="내가 어느나라 사람인지 맞춰보고, 그 나라의 문화에 대해 말해봐")],
    config=config
):
    print(r.content, end='|')