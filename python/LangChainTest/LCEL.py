from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"))

from langchain_core.messages import HumanMessage, SystemMessage

messages=[
    SystemMessage(content="너는 미녀와 야수에 나오는 미녀고 이름은 벨이야. 그 캐릭터에 맞게 사용자와 대화해."),
    HumanMessage(content="나는 잘난 개스톤. 벨 나와 식사하고 가는건 어때?")
]

result = model.invoke(messages)

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

# msg = parser.invoke(result)
# print(msg)

chain = model|parser
print(chain.invoke(messages))