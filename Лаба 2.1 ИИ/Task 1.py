import doctest

class Furniture:

    def __init__(self, position_x: float, position_y: float):
        """
        Создание и подготовка к работе объекта "Мебель"

        :param position_x: начальное положение по оси Х
        :param position_y: начальное положение по оси Y

        Начальные координаты мебели расположены в точке (0, 0) и являются углом
        помещения, поэтому перемещать мебель в значении -x и -y невозможно.

        :raise ValueError: если position_x или position_y < 0
        :raise TypeError: если position_x или position_y не int или float

        Примеры:
        >>> f = Furniture(1.0, 1.0)  # инициализация экземпляра класса
        """

        if not isinstance(position_x, (int, float)):
            raise TypeError("Значение перемещения мебели должно быть типа int или float")
        if position_x < 0:
            raise ValueError("Перемещение по оси X должно быть >= 0")

        if not isinstance(position_y, (int, float)):
            raise TypeError("Значение перемещения мебели должно быть типа int или float")
        if position_y < 0:
            raise ValueError("Перемещение по оси Y должно быть >= 0")

        self.position_x = position_x
        self.position_y = position_y

    def move(self, new_x: float, new_y: float) -> str:

        """
        Метод, описывающий перемещение мебели в новые координаты.

        :param new_x: Новая координата X, должно быть числом.
        :param new_y: Новая координата Y, должно быть числом.
        :return: Строка, описывающая перемещение.

        >>> f = Furniture(1.0, 1.0)
        >>> f.move(2.0, 3.0)
        'Мебель перемещена в координаты (2.0, 3.0).'
        """

        self.position_x = new_x
        self.position_y = new_y
        return f'Мебель перемещена в координаты ({new_x}, {new_y}).'

class Tree:

    def __init__(self, species: str, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева, должен быть строкой.
        :param age: Возраст дерева, должен быть положительным целым числом.

        :raises ValueError: Если возраст не положительный.
        :raises TypeError: Если вид дерева не строка.

        Примеры:
        >>> t = Tree("дуб", 50)  # инициализация экземпляра класса
        """

        if not isinstance(species, str):
            raise TypeError("Название дерева должно быть в формате str.")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом.")

        self.species = species
        self.age = age

    def shed_leaves(self) -> str:
        """
        Метод, описывающий, как дерево сбрасывает листья.

        :return: Строка с описанием процесса.

        >>> t = Tree("дуб", 50)
        >>> t.shed_leaves()
        'Дерево сбрасывает листья осенью.'
        """
        return 'Дерево сбрасывает листья осенью.'

class SocialNetwork:

    def __init__(self, name: str, user_limit: int):

        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети, должно быть строкой.
        :param user_limit: Максимальное количество пользователей, должно быть положительным целым числом.

        :raises ValueError: Если пользовательский лимит не положительный.
        :raises TypeError: Если название не строка.

        Примеры:
        >>> sn = SocialNetwork("Facebook", 1000) # инициализация экземпляра класса
        """
        
        if user_limit <= 0:
            raise ValueError("Лимит пользователей должен быть положительным числом.")

        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть в формате str.")

        self.name = name
        self.user_limit = user_limit
        self.users = []  # Список пользователей

    def add_user(self, username: str) -> str:

        """
        Метод, описывающий добавление пользователя в социальную сеть.

        :param username: Имя пользователя, должен быть строкой.
        :return: Строка с сообщением о добавлении пользователя.

        :raises ValueError: Если количество пользователей превышает лимит.

        >>> sn = SocialNetwork("Facebook", 3)
        >>> sn.add_user("User123")
        'Пользователь User123 добавлен в сети Facebook.'
        >>> sn.add_user("User456")
        'Пользователь User456 добавлен в сети Facebook.'
        >>> sn.add_user("User789")
        'Пользователь User789 добавлен в сети Facebook.'
        >>> sn.add_user("User101")  # При добавлении четвертого пользователя будет ошибка
        'Ошибка: превышен лимит пользователей.'
        """

        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть в формате str.")

        if len(self.users) >= self.user_limit:
            return "Ошибка: превышен лимит пользователей."

        self.users.append(username)
        return f'Пользователь {username} добавлен в сети {self.name}.'


if __name__ == "__main__":
    # Проверка работоспособности экземпляров класса с помощью doctest
    doctest.testmod()


