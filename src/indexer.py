from pathlib import Path
from collections import defaultdict
from src.tokenizer import tokenize

def open_docs(docs_path) -> dict[str, list[str]]:
    documents = {}
    try:
        for file_path in docs_path.glob("*.txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                tokens = tokenize(text) # Tokenize string
                documents[file_path.name] = tokens # Add tokens to the document dictionary

    except FileNotFoundError:
        print("Error: File Not Found")

    except Exception as e:
        print(f"Error: {e}")

    return documents

def build_index(documents: dict[str,list[str]]) -> dict[str, dict[str, set[int]]]:
    index = defaultdict(lambda: defaultdict(set))
    for document, tokens in documents.items():
        for position, token in enumerate(tokens):
            index[token][document].add(position)

    return index
