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
        """Возвращает валидную строку для инициализации экземпляра."""
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library.

        :param books: Список книг, по умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги, увеличенный на 1.

        :return: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.

        :raises ValueError: Если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


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
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1