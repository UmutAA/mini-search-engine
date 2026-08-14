from typing import List
import re

def tokenize(text: str) -> List[str]:
    lowercase_text = text.lower()
    clean_text = re.sub(r"[^\w\s]", " ", lowercase_text)
    tokens = clean_text.split()

    return tokens
