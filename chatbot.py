import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# Load queries
queries = [
    "How do I track my order?",
    "My discount code is not working.",
    "How can I return a product?",
    "When will my order be delivered?",
    "I received a damaged item. What should I do?",
    "Can I cancel my order?",
    "How do I change my delivery address?",
    "Where can I see my order history?",
    "Do you offer cash on delivery?",
    "How do I contact customer support?",
    "Why was my payment declined?",
    "Can I exchange a product?",
    "How long does shipping take?",
    "Do you provide refunds?",
    "How do I apply a coupon code?",
    "Is there a warranty on products?",
    "What if my order is delayed?",
    "Can I reorder a previous item?",
    "How do I update my account details?",
    "Do you ship internationally?"
]

def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Error: {e}"

# Load templates
with open("prompts/zero_shot_template.txt", "r") as f:
    zero_template = f.read()

with open("prompts/one_shot_template.txt", "r") as f:
    one_template = f.read()

# Write results
with open("eval/results.md", "w", encoding="utf-8") as file:
    file.write("| Query | Method | Response | Relevance | Coherence | Helpfulness |\n")
    file.write("|-------|--------|----------|-----------|-----------|-------------|\n")

    for q in queries:
        zero_prompt = zero_template.replace("{query}", q)
        one_prompt = one_template.replace("{query}", q)

        zero_response = query_ollama(zero_prompt)
        one_response = query_ollama(one_prompt)

        file.write(f"| {q} | Zero-Shot | {zero_response} |  |  |  |\n")
        file.write(f"| {q} | One-Shot | {one_response} |  |  |  |\n")