# Object Oriented Programming

## Practical Example

In this example, we will use the concepts of **aggregation** among **entities**.

```python

class Author:

    def __init__(self, name: str, birth_year: str):
        self.name: str = name
        self.birth_year: str = birth_year

    def information(self) -> str:
        return f"{self.name} (born in {self.birth_year})"

class Book:

    def __init__(self, title: str, published_year: str, author: Author):
        self.title: str = title
        self.published_year: str = published_year
        self.author: Author = author

    def information(self) -> str:
        return f"{self.title} by {self.author.information()} in {self.published_year}"

author: Author = Author("Machado de Assis", 1839)

book_1: Book = Book("Dom Casmurro", 1900, author)
book_2: Book = Book("Quincas Borba", 1891, author)

print(book_1.information())
print(book_2.information())

```

In this example, the **book** aggregates (contains the reference) of the **author**.
