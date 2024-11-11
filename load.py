# Load Data #

# Note: Run This Python Script Only Once

# Import Packages
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from mongo import collection
import env as e

# Get Env Variables
openai_api_key = e.openai_api_key  # OpenAI API Key

# Loader Params
path = "./data"
glob = "./*.txt"
progress = True

# Directory Loader
loader = DirectoryLoader(path=path, glob=glob, show_progress=progress)

# Load Data
data = loader.load()

# Generate Embeddings
embeddings = OpenAIEmbeddings(api_key=openai_api_key)

# Vector Store
vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection)
