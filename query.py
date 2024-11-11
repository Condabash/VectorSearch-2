# Query Data #

# Import Packages
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from mongo import collection
import env as e

# Variables
model = "gpt-4o-mini"

# Get Env Variables
openai_api_key = e.openai_api_key  # OpenAI API Key

# Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Vector Store
vectorStore = MongoDBAtlasVectorSearch(collection, embeddings)


# Query Data Function
def query_data(query):
    # Similarity Search For Query
    docs = vectorStore.similarity_search(query, k=1)

    # First Doc Page Content
    data = docs[0].page_content

    # OpenAI LLM Instance
    llm = OpenAI(api_key=openai_api_key, model=model, temperature=0)

    # Retriever Instance
    retriever = vectorStore.as_retriever()

    # QA Chain Instance
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # LLM Answer
    answer = ga.run(query)

    # Return Data and Answer
    return data, answer
