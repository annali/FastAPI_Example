from tkinter.scrolledtext import example

from pydantic import BaseModel

class BookInput(BaseModel):
    id_:int
    title:str
    author:str
    year:int
    genre:str
    isbn:str

    class Config:
        json_schema_extra = {
            "example": {
                "id_":1,
                "title":"Book Title",
                "author":"<NAME>",
                "year":2012,
                "genre":"Science Fiction",
                "isbn":"978-7-5033-7012-9"
            }
        }

class BookOutput(BookInput):
    id_:int
    title:str
    author:str
    year:int
    genre:str
    isbn:str
    class Config:
        json_schema_extra = {
            "example": {
                "id_":1,
                "title":"Book Title",
                "author":"<NAME>",
                "year":2012,
                "genre":"Science Fiction",
                "isbn":"978-7-5033-7012-9"
            }
        }

if __name__ == '__main__':
    books = Book(id_=1, \
                 title="One Hundred Years of Solitude",\
                 author="Gabriel García Márquez",year=1234,\
                 genre="Magical Realism",isbn="978-7-5399-1578-7")
    # for book in books:
    #     print(book)
    # print(books)
    print(books.model_dump())
    print(books.model_dump_json())
    print(books.title)