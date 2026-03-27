import os
import random
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_architecture(requirements_json):

    design_style = random.choice([
        "modern premium ecommerce UI",
        "enterprise marketplace design",
        "luxury minimal commerce design",
        "high-scale marketplace architecture",
        "startup unicorn style commerce"
    ])

    prompt = f"""
You are a senior software architect.

Based on the following structured requirements:

{requirements_json}

Generate:

1. Production-level architecture
2. Folder structure
3. Frontend architecture
4. Backend architecture
5. Database schema
6. API route structure
7. Design system overview

Design style: {design_style}

Make it scalable, modular and real-world production grade.

Return in structured markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()


def generate_full_code(requirements_json):

    prompt = f"""
You are a senior full-stack engineer.

Generate production-ready code based on:

{requirements_json}

Requirements:
- Clean folder structure
- Modern UI (not basic)
- Real-world architecture
- Responsive design
- Authentication system
- Payment integration (if required)
- API layer
- Database models

Return separated sections:

FRONTEND_CODE:
BACKEND_CODE:
DATABASE_SCHEMA:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()