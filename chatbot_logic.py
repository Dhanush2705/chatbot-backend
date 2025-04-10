import json
from rapidfuzz import fuzz

# Load the FAQ data
with open('faq_data.json', 'r') as f:
    faq_data = json.load(f)

def get_bot_response(msg):
    msg = msg.lower()
    best_score = 0
    best_match = None

    for question, response in faq_data.items():
        score = fuzz.token_sort_ratio(msg, question.lower())
        if score > best_score and score >= 60:  # You can adjust the threshold
            best_score = score
            best_match = response

    if best_match:
        return best_match
    else:
        return "I'm not sure about that. Could you please rephrase or ask something else?"
