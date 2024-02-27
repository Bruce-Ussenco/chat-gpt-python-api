import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"

print("")

#content = "Say this is a test!"
content = input("Ask something to Chat GPT:\n")
data = {
    "model": model_id,
    "messages": [{"role": "user", "content": content}]
}
data = json.dumps(data)

request = requests.post(link, headers=headers, data=data)
response = request.json()
text_response = response["choices"][0]["message"]["content"]

#print(request.text)

print("")
print("Output:")
print("-" * 30)
print(text_response)
print("-" * 30)
print("")

