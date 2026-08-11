from pathlib import Path
from tokenizer import tokenize

def open_docs():
    base_dir = Path(__file__).resolve().parent.parent
    path = base_dir / "tests"
    try:
        for file_path in path.glob("*.txt"):
            print(f"---{file_path}---")
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                tokens = tokenize(text)
                print(tokens)
            print("\n")

    except FileNotFoundError:
        print("Error: File Not Found")

    except Exception as e:
        print(f"Error: {e}")