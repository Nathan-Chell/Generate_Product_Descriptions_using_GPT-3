import settings
import os
import openai


openai.organization = settings.Open_AI_Key
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
