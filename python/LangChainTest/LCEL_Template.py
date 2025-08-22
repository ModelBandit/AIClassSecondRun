from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"))

from langchain_core.prompts import ChatPromptTemplate

SystemMessage = content="너는 {story}에 나오는 {character_a}고 그 캐릭터에 맞게 사용자와 대화해."
HumanMessage = content="나는 {character_b}. 나와 {activity}하러 가는건 어때?"
messages_template=ChatPromptTemplate(
    [
        ("system", SystemMessage),
        ("user", HumanMessage),
    ]
)

result = messages_template.invoke(
    {
        "story":"미녀와 야수",
        "character_a":"미녀",
        "character_b":"야수",
        "activity":"저녁식사",
    }
)

print(result)


from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
chain = messages_template|model|parser
print(chain.invoke(
    {
        "story":"미녀와 야수",
        "character_a":"미녀",
        "character_b":"야수",
        "activity":"저녁식사",
    }))