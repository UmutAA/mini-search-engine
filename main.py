from pathlib import Path
from src.searcher import search
from src.indexer import open_docs, build_index

docs_path = Path(__file__).resolve().parent / "tests"

docs = open_docs(docs_path)
indices = build_index(docs)

query = input("Enter your query: ")

results = search(query, indices)
print(results)
