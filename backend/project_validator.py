import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_and_generate_execution_guide(full_code_text, session_id):

    prompt = f"""
You are a senior software architect and DevOps engineer.

Analyze the following full-stack project code:

{full_code_text}

Perform the following:

1. Detect frontend, backend, and database technologies.
2. Check if integrations between frontend and backend are correct.
3. Detect potential runtime errors.
4. Detect outdated or risky packages.
5. Identify authentication setup steps (OAuth, JWT, Google login etc).
6. Identify payment setup steps (Stripe, Razorpay etc).
7. Identify environment variables required.
8. Identify database setup steps.
9. Identify build steps.
10. Provide exact terminal commands to run frontend and backend.
11. Provide deployment steps (local + production).
12. Provide security warnings if any.

Return the result in structured markdown:

# PROJECT VALIDATION REPORT
# TECHNOLOGY STACK
# INTEGRATION CHECK
# REQUIRED ENV VARIABLES
# LOCAL DEVELOPMENT SETUP (STEP BY STEP)
# AUTHENTICATION SETUP (STEP BY STEP)
# PAYMENT GATEWAY SETUP (STEP BY STEP)
# DATABASE SETUP (STEP BY STEP)
# BUILD & RUN COMMANDS
# PRODUCTION DEPLOYMENT STEPS
# POTENTIAL ERRORS & FIXES
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    report = response.text.strip()

    folder = f"generated_projects/{session_id}"
    os.makedirs(folder, exist_ok=True)

    report_path = os.path.join(folder, "EXECUTION_GUIDE.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    return report_path