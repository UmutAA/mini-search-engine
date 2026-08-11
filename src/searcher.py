from tokenizer import tokenize

def search(query: str, index: dict[str, set[str]]) -> set[str]:
    documents = set()
    query_tokens = tokenize(query) 
    for query_token in query_tokens:
        if query_token not in index:
            continue
        
        for doc in index[query_token]:
            documents.add(doc)
    return documents
