import openai, random
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

HOOKS = [
    "This just happened today.",
    "Nobody noticed this.",
    "This changes everything.",
    "This was not supposed to happen."
]

def generate_variations(topic):
    scripts = []
    for angle in ["why this matters", "what shocked people", "what happens next"]:
        hook = random.choice(HOOKS)
        prompt = f"""
        Start EXACTLY with: "{hook}"
        Topic: {topic}
        Angle: {angle}
        Under 45 seconds. Fast. Simple. End with curiosity.
        """
        res = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        scripts.append(res.choices[0].message.content.strip())
    return scripts
