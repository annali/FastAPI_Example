import json
from schema import BookInput,BookOutput


def load_book() ->list:
    with open('book.json') as f:
        books = json.load(f)
        return [BookInput(**book) for book in books]

def save_book(books:list[BookInput]):
    with open('book.json', 'w') as f:
        json.dump([book.model_dump() for book in books], f, indent=4)


print(load_book())