import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_next_question(history):
    """
    history format:
    [
        {"role": "user", "message": "..."},
        {"role": "assistant", "message": "..."}
    ]
    """
    formatted_history = ""

    for msg in history:
        role = msg["role"].upper()
        message = msg["message"]
        formatted_history += f"{role}: {message}\n"

    prompt = f"""
You are an AI website requirement assistant.

Collect structured website requirements strictly under these categories:

1. Website Type(Analzye the website if mentioned)
2. Target Audience(Ask if it is for B2B or B2C)
3. Pages Required (What kind of pages required and how to design each)
4. Design Level (Low / Medium / High)
5. Frontend Technology
6. Backend Technology
7. Database
8. Authentication Required
9. Payment Integration
10. Hosting Preference

Rules:
- Ask ONLY one question at a time.
- Ask ONLY for missing fields.
- Do NOT repeat answered fields.
- No extra discussion.
- If all fields collected, respond exactly:
REQUIREMENTS_COMPLETE

Conversation so far:
{formatted_history}

Ask the next required question:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()

def extract_structured_requirements(history):

    formatted_history = ""

    for msg in history:
        formatted_history += f"{msg['role'].upper()}: {msg['message']}\n"

    prompt = f"""
Convert the following conversation into structured JSON.

Return ONLY valid JSON.
No explanation.

Conversation:
{formatted_history}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()
