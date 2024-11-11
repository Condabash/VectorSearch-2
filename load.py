# Load Data #

# Note: Run This Python Script Only Once

# Import Packages
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from mongo import collection
import nltk
import env as e

# Download NLTK Data
nltk.download("punkt")  # Sentence Tokenizer
nltk.download("punkt_tab")  # Word Tokenizer

# Get Env Variables
openai_api_key = e.openai_api_key  # OpenAI API Key

# Directory Loader
loader = DirectoryLoader(path="./data", glob="./*.txt", show_progress=True)

# Load Data
data = loader.load()

# Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Vector Store
vectorStore = MongoDBAtlasVectorSearch.from_documents(
    data, embeddings, collection=collection
)
