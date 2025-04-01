import redis
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_redis import RedisChatMessageHistory
from dotenv import load_dotenv
import os

# loading the key
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model='gpt-4o-mini')

human_template = f"{{question}}"
print(human_template)

prompt_template = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="history"),
        ('human', human_template)
    ]
)


chain = prompt_template | model

redis_client = redis.Redis(host='localhost', port=6379)

def get_redis_history(session_id) -> BaseChatMessageHistory:
    return RedisChatMessageHistory(session_id=session_id, redis_client=redis_client)

chain_with_history = RunnableWithMessageHistory(
    chain, 
    get_session_history=get_redis_history,
    input_messages_key="question",
    history_messages_key='history'
)

while True:
    user_question = input('>>>>')
    result = chain_with_history.invoke(
        {'question': user_question},
        config={'configurable': {'session_id': 'Erfan'}}

    )
    print(result.content)