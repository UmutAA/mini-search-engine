from typing import List
from pathlib import Path
from collections import defaultdict
from tokenizer import tokenize

def open_docs() -> dict[str, List[str]]:
    documents = {}
    base_dir = Path(__file__).resolve().parent.parent # Get projects absolute directory
    path = base_dir / "tests" # Access txt files' directory
    try:
        for file_path in path.glob("*.txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                tokens = tokenize(text) # Tokenize string
                documents[file_path.name] = tokens # Add tokens to the document dictionary

    except FileNotFoundError:
        print("Error: File Not Found")

    except Exception as e:
        print(f"Error: {e}")

    return documents

def build_index(documents: dict[str,List[str]]) -> dict[str, set[str]]:
    index = defaultdict(set)
    for document, tokens in documents.items():
        for token in tokens:
            index[token].add(document)
    return index
