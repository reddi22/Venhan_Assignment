class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# Example usage
book1 = Book("Geetanjali", "Rabindranath Tagore", 500)
print(book1)  # Output: Title: Geetanjali, Author: Rabindranath Tagore, Pages: 500