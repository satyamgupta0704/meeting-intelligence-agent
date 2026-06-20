import os
import json
from google import genai
from dotenv import load_dotenv

# 1. Dynamically find and load the .env file from the backend/ directory
script_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(script_dir)
load_dotenv(os.path.join(backend_dir, ".env"))

# 2. Initialize the Gemini client using the key we just loaded
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_brief(
    company,
    research_data
):

    prompt = f"""
You are a meeting intelligence agent.

Company:
{company}

Research:
{json.dumps(research_data)}

Generate valid JSON only.

Schema:

{{
  "company_overview":"",
  "recent_activity":"",
  "tech_signals":"",
  "pain_points":"",
  "talking_points":[
    "",
    "",
    ""
  ]
}}

Rules:

- Plain English
- No markdown
- No explanation
- Return JSON only
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text