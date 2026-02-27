import re

def extract_score(text):
    # Look for any number between 0–100 near the word score
    match = re.search(r"(score|readiness)[^0-9]*(\d{1,3})", text, re.IGNORECASE)

    if match:
        score = int(match.group(2))
        if 0 <= score <= 100:
            return score

    return None