from pathlib import Path
from src.searcher import search
from src.indexer import open_docs, build_index

docs_path = Path(__file__).resolve().parent / "tests"

docs = open_docs(docs_path)
index = build_index(docs)

print("------ Search Engine ------")
while True:
    print("To exit type 'exit'")
    query = input("Enter your query: ")

    if query.lower().strip() == "exit":
        break

    if not query.strip():
        print("Query cannot be empty")
        continue

    mode = input("Enter your query mode (or/and/phrase): ").lower().strip()
    try:
        results = search(query, index, mode)
    except ValueError:
        print("Error: Unknown Mode. Please enter a valid mode (or/and/phrase).\n")
        continue

    if not results:
        print("No result found\n")
    else:
        print(f"{results}\n")