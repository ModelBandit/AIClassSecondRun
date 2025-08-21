from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("OPENAI_API_KEY")
model =ChatOpenAI(model="gpt-4.1-nano", openai_api_key=key)
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

messages = [
    # {"role":"system", "content":"대충 이런저런 말"}
    SystemMessage("너는 비밀요원이고, 코드네임은 웬즈데이.")
]

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    messages.append(
        HumanMessage(user_input)
    )

    ai_response = model.invoke(messages)
    messages.append(
        ai_response
    )

    print("AI: " + ai_response.content)