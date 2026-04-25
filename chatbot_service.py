import os
from dotenv import load_dotenv
import google.generativeai as genai
from groq import Groq

# Load environment variables
load_dotenv()

# Configure APIs
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# System prompt
SYSTEM_PROMPT = """
You are KrishiMitra Kerala, an AI farming assistant for Kerala farmers.

Rules:
- Detect the user's language automatically.
- If the user speaks in Malayalam, ALWAYS reply in Malayalam.
- If the user speaks in English, reply in simple English.

- Give short, clear, practical farming advice.
- Focus on Kerala crops: coconut, banana, paddy, rubber, pepper, cardamom, tapioca, vegetables.
- Avoid unsafe pesticide recommendations.
- For serious plant diseases, suggest consulting Krishi Bhavan or a local agriculture officer.
- If the question is not farming-related, still answer briefly and politely.
"""

# Detect Malayalam vs English
def detect_language(text: str) -> str:
    return "ml-IN" if any('\u0D00' <= ch <= '\u0D7F' for ch in text) else "en-IN"


# Build AI prompt
def build_prompt(message, lang, district=None, crop=None):
    return f"""
{SYSTEM_PROMPT}

Farmer details:
District: {district or "Not provided"}
Crop: {crop or "Not provided"}
Preferred language: {lang}

Farmer question:
{message}

Give the best useful answer.
"""


# Groq (Primary)
def try_groq(prompt):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )
    return response.choices[0].message.content


# Gemini (Fallback)
def try_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


# Local fallback (no API)
def fallback_reply(message, lang):
    msg = message.lower()

    if "banana" in msg or "yellow" in msg or "വാഴ" in message:
        reply = """
Banana leaf yellowing may happen due to nutrient deficiency, excess water, or root disease.

Suggested actions:
1. Check soil moisture.
2. Avoid overwatering.
3. Add compost or organic manure.
4. Remove badly affected leaves.
5. If spreading fast, consult Krishi Bhavan.
"""
    elif "rain" in msg or "spray" in msg:
        reply = """
If rain is expected, avoid spraying pesticide or fertilizer.

Spray only when there is no rain for at least 6–8 hours.
Also avoid spraying during strong wind or peak sunlight.
"""
    else:
        reply = """
I can help with crop care, fertilizer, irrigation, pest symptoms, and Kerala farming advice.

Please mention crop name, district, and symptom for better guidance.
"""

    return reply


# Main function
def get_farming_reply(message: str, language: str = "auto", district: str = None, crop: str = None):
    lang = detect_language(message) if language == "auto" else language
    prompt = build_prompt(message, lang, district, crop)

    # 1. Try Groq first
    try:
        reply = try_groq(prompt)
        return {
            "reply": reply,
            "language": lang,
            "status": "success_groq"
        }
    except Exception as e:
        print("Groq Error:", e)

    # 2. Try Gemini second
    try:
        reply = try_gemini(prompt)
        return {
            "reply": reply,
            "language": lang,
            "status": "success_gemini"
        }
    except Exception as e:
        print("Gemini Error:", e)

    # 3. Local fallback
    return {
        "reply": fallback_reply(message, lang),
        "language": lang,
        "status": "fallback"
    }