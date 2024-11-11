# Env #

# Import Packages
import os
from dotenv import load_dotenv, find_dotenv

# Load Env
load_dotenv(find_dotenv())

# Get Env Variables

# MongoDB URI
mongo_uri = os.getenv("MONGO_URI")

# MongoDB Database
mongo_db = os.getenv("MONGO_DB")

# MongoDB Collection
mongo_collection = os.getenv("MONGO_COLLECTION")

# OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Print Env Variables
# print("MongoDB URI:", mongo_uri)
# print("MongoDB Database:", mongo_db)
# print("MongoDB Collection:", mongo_collection)
# print("OpenAI API Key:", openai_api_key)
