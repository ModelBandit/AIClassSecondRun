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

# print(with_message_history)

config2 = {"configurable": {"session_id":"abc2"}}

response = with_message_history.invoke(
    [HumanMessage(content="내 이름은 비니거야")],
    config=config2,
)
print(response.content)

config3 = {"configurable": {"session_id":"abc3"}}

response = with_message_history.invoke(
    [HumanMessage(content="내 이름은 발사믹이야")],
    config=config3,
)
print(response.content)

response = with_message_history.invoke(
    [HumanMessage(content="내 이름이 뭐지?")],
    config=config2,
)
print(response.content)

response = with_message_history.invoke(
    [HumanMessage(content="내 이름이 뭐지?")],
    config=config3,
)
print(response.content)

print(config2)
print(config3)
