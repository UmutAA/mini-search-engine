from src.tokenizer import tokenize

def search(query: str, index: dict[str, dict[str, set[int]]], mode="phrase") -> set[str]:
    query_tokens = tokenize(query) 
    match mode:
        case "or":
            documents = set()

            for query_token in query_tokens:
                if query_token not in index:
                    continue

                documents.update(index[query_token])

        case "and":
            if not query_tokens:
                return set()

            if query_tokens[0] not in index:
                return set()
            
            documents = set(index[query_tokens[0]])

            for query_token in query_tokens[1:]:
                if query_token not in index:
                    return set()
                
                documents &= set(index[query_token])

        case "phrase":
            return phrase_search(query,index)
        case _:
            raise ValueError("Invalid Mode")
        
    if not documents:
        return set()
    return documents


def phrase_search(query: str, index: dict[str, dict[str, set[int]]]) -> set[str]:
    if not query:
        return set()
    
    query_tokens = tokenize(query)

    for token in query_tokens:
        if token not in index:
            return set()
            
    documents = set()

    for doc in index[query_tokens[0]].keys():

        for pos in index[query_tokens[0]][doc]:
            phrase_found = True

            for i in range(1, len(query_tokens)):
                next_token = query_tokens[i]

                if doc not in index[next_token]:
                    phrase_found = False
                    break

                expected_pos = pos + i
                if expected_pos not in index[query_tokens[i]][doc]:
                    phrase_found = False
                    break

            if phrase_found:
                documents.add(doc)
                break

    return documents