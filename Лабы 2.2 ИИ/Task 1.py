class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book.

        :param id_: Идентификатор книги, должен быть целым числом.
        :param name: Название книги, должно быть строкой.
        :param pages: Количество страниц в книге, должно быть положительным целым числом.

        :raises ValueError: Если количество страниц <= 0.
        :raises TypeError: Если id_ не int, name не str, или pages не int.
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть целым числом.")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """Возвращает строку формата: Книга "название_книги"."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """Возвращает строку для инициализации экземпляра."""
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


# База данных книг
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # Проверяем метод str

    print(list_books)  # Проверяем метод repr


