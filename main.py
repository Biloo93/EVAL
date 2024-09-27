from dotenv import load_dotenv
import os


load_dotenv()

groq_api_token = os.getenv("GROQ_API_TOKEN")

print(f"Votre clé API Groq : {groq_api_token}")
