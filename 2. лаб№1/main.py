# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
import doctest

class Coin:
    def _init_(self, denomination: float, material: str):
        """
        Создание и подготовка к работе объекта "Монета"

        :param denomination: Номинал монеты
        :param material: Материал монеты

        Примеры:
        >>> coin = Coin(10, "gold")  # инициализация экземпляра класса
        """
        if not isinstance(denomination, (int, float)) or denomination <= 0:
            raise ValueError("Номинал монеты должен быть положительным числом.")
        if not isinstance(material, str):
            raise TypeError("Материал монеты должен быть строкой.")

        self.denomination = denomination
        self.material = material

    def flip(self) -> str:
        """
        Функция подбрасывания монеты, возвращает "орел" или "решка".

        Примеры:
        >>> coin = Coin(10, "gold")
        >>> result = coin.flip()  # результат "орел" или "решка"
        """
        import random
        return random.choice(["орел", "решка"])

    def describe(self) -> str:
        """
        Возвращает описание монеты.

        Примеры:
        >>> coin = Coin(10, "gold")
        >>> coin.describe()
        'Монета номиналом 10 из материала gold'
        """
        return f"Монета номиналом {self.denomination} из материала {self.material}"


class RemoteControl:
    def _init_(self, brand: str, number_of_buttons: int, battery_type: str):
        """
        Создание и подготовка к работе объекта "Пульт"

        :param brand: Бренд пульта
        :param number_of_buttons: Количество кнопок
        :param battery_type: Тип батареек

        Примеры:
        >>> remote = RemoteControl("Samsung", 15, "AA")
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой.")
        if not isinstance(number_of_buttons, int) or number_of_buttons <= 0:
            raise ValueError("Количество кнопок должно быть положительным числом.")
        if not isinstance(battery_type, str):
            raise TypeError("Тип батареек должен быть строкой.")

        self.brand = brand
        self.number_of_buttons = number_of_buttons
        self.battery_type = battery_type

    def change_channel(self, channel_number: int) -> str:
        """
        Смена канала на заданный номер.

        :param channel_number: Номер канала

        Примеры:
        >>> remote = RemoteControl("Samsung", 15, "AA")
        >>> remote.change_channel(5)
        'Канал переключен на 5 с помощью пульта Samsung'
        """
        if not isinstance(channel_number, int) or channel_number <= 0:
            raise ValueError("Номер канала должен быть положительным числом.")
        return f"Канал переключен на {channel_number} с помощью пульта {self.brand}"

    def check_battery(self) -> str:
        """
        Проверка типа батареек.

        Примеры:
        >>> remote = RemoteControl("Samsung", 15, "AA")
        >>> remote.check_battery()
        'Батарейки типа AA нуждаются в проверке.'
        """
        return f"Батарейки типа {self.battery_type} нуждаются в проверке."


class Telegram:
    def _init_(self, username: str, chat_count: int, is_premium: bool):
        """
        Создание и подготовка к работе объекта "Telegram"

        :param username: Имя пользователя
        :param chat_count: Количество чатов
        :param is_premium: Статус премиум пользователя

        Примеры:
        >>> tg_user = Telegram("@user123", 25, False)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not isinstance(chat_count, int) or chat_count < 0:
            raise ValueError("Количество чатов должно быть неотрицательным числом.")
        if not isinstance(is_premium, bool):
            raise TypeError("Премиум статус должен быть логическим значением.")

        self.username = username
        self.chat_count = chat_count
        self.is_premium = is_premium

    def send_message(self, recipient: str, message: str) -> str:
        """
        Отправка сообщения другому пользователю.

        :param recipient: Имя получателя
        :param message: Текст сообщения

        Примеры:
        >>> tg_user = Telegram("@user123", 25, False)
        >>> tg_user.send_message("@friend456", "Hello!")
        'Сообщение отправлено @friend456: Hello!'
        """
        if not isinstance(recipient, str) or not isinstance(message, str):
            raise TypeError("Получатель и сообщение должны быть строками.")
        return f"Сообщение отправлено {recipient}: {message}"

    def upgrade_to_premium(self) -> str:
        """
        Улучшение аккаунта до премиум.

        Примеры:
        >>> tg_user = Telegram("@user123", 25, False)
        >>> tg_user.upgrade_to_premium()
        'Теперь вы премиум пользователь!'
        """
        if not self.is_premium:
            self.is_premium = True
            return "Теперь вы премиум пользователь!"
        return "Вы уже являетесь премиум пользователем."

if _name_ == "_main_":
    doctest.testmod()  # тестирование примеров, которые находятся в документации