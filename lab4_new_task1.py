class Vehicle:
    """Базовый класс для транспортных средств."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализация объекта Vehicle.

        Args:
            make: Производитель автомобиля.
            model: Модель автомобиля.
            year: Год выпуска автомобиля.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Vehicle."""
        return f'{self.year} {self.make} {self.model}'

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление объекта Vehicle."""
        return f'Vehicle(make={self.make!r}, model={self.model!r}, year={self.year})'


class Car(Vehicle):
    """Класс легковых автомобилей, наследующий от Vehicle."""

    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """Инициализация объекта Car.

        Args:
            make: Производитель автомобиля.
            model: Модель автомобиля.
            year: Год выпуска автомобиля.
            doors: Количество дверей.
        """
        super().__init__(make, model, year)  # Унаследованный конструктор
        self.__doors = doors  # Приватный атрибут для инкапсуляции

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Car с указанием количества дверей."""
        return f'{super().__str__()} с {self.__doors} дверями'

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление объекта Car."""
        return f'Car(make={self.make!r}, model={self.model!r}, year={self.year}, doors={self.__doors})'

    def get_doors(self) -> int:
        """Возвращает количество дверей в автомобиле.

        Returns:
            Количество дверей.

        Примечание:
            Данный метод необходим для получения количества дверей,
            так как атрибут __doors является приватным.
        """
        return self.__doors

    def set_doors(self, doors: int) -> None:
        """Устанавливает количество дверей в автомобиле.

        Args:
            doors: Новое количество дверей.

        Примечание:
            Данный метод позволяет изменить количество дверей лишь в том случае,
            если переданный аргумент является положительным числом.
        """
        if doors > 0:
            self.__doors = doors
        else:
            raise ValueError("Количество дверей должно быть положительным числом.")


if __name__ == "__main__":
    # Пример использования классов
    my_car = Car("Toyota", "Camry", 2022, 4)
    print(my_car)  # Выводит: 2022 Toyota Camry с 4 дверями
    print(repr(my_car))  # Формальное представление
    print(my_car.get_doors())  # Количество дверей
    my_car.set_doors(5)  # Установка нового значения
    print(my_car)  # Выводит: 2022 Toyota Camry с 5 дверями

