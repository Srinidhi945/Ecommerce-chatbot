from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from ecommbot.ingest import ingestdata
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_redis import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os
from ecommbot.ingest import ingestdata

load_dotenv()

# TEMPLATE
PRODUCT_BOT_TEMPLATE = """
You are a helpful ecommerce assistant that answers user queries based on product reviews and titles.

CONTEXT:
{context}

QUESTION: {question}

YOUR ANSWER:
"""

# Clean wrapper to ensure only string is passed
def unwrap_question(input_):
    question = input_.get("question", "")
    if isinstance(question, list) and question:
        return question[0]
    elif isinstance(question, str):
        return question
    else:
        return str(question)

# Chain builder function
def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})
    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3,
    )

    chain = (
        {
            "context": lambda x: retriever.invoke(unwrap_question(x)),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    # Attach memory support
    def build_chain(session_id: str):
        redis_url = os.getenv("REDIS_URL")
        history = RedisChatMessageHistory(session_id=session_id, redis_url=redis_url)

        return RunnableWithMessageHistory(
            chain,
            lambda _: history,
            input_messages_key="question",
            history_messages_key="history",
            configurable_fields=["session_id"],
        )

    return build_chain





if __name__=='__main__':
    vstore = ingestdata("done")
    chain  = generation(vstore)
    print(chain.invoke("can you tell me the best bluetooth buds?"))
    
    
    
    