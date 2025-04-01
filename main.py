from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# Allow frontend or tools to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def root():
    return {"message": "OutbackAI is running!"}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are OutbackAI, an expert assistant for fencing, Shopify, Facebook marketing, and Xero."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=1000,
    )

    return {"reply": response["choices"][0]["message"]["content"]}
