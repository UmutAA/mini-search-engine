from src.tokenizer import tokenize

def search(query: str, index: dict[str, dict[str, set[int]]], mode="or") -> set[str]:
    query_tokens = tokenize(query) 
    match mode:
        case "or":
            documents = set()
            for query_token in query_tokens:
                if query_token not in index:
                    continue

                for doc in index[query_token]:
                    documents.add(doc)

        case "and":
            if not query_tokens:
                return set()
            documents = index[query_tokens[0]]
            for query_token in query_tokens:
                if query_token not in index:
                    return set()
                documents &= index[query_token]
        case _:
            raise ValueError("Invalid Mode")
        
    if not documents:
        return set()
    return documents
