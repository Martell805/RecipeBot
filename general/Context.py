class Context:
    """
    Класс, который позволяет сохранять данные между вызовами функций
    """
    def __init__(self):
        self.dict = dict()

    def get_attribute(self, key):
        """
        Возвращает значение аттрибута по ключу
        :param key: Ключ атрибута
        :return: Значение атрибута
        """
        return self.dict[key]

    def set_attribute(self, key, value):
        """
        Изменяет и возвращает значение аттрибута по ключу
        :param key: Ключ атрибута
        :param value: Значение атрибута
        :return: Значение атрибута
        """
        self.dict[key] = value
        return self.dict[key]

    def delete_attribute(self, key):
        """
        Удаляет и возвращает значение аттрибута по ключу
        :param key: Ключ атрибута
        :return: Значение атрибута
        """
        value = self.dict[key]
        del self.dict[key]
        return value

    def __getitem__(self, key):
        """
        Возвращает значение аттрибута по ключу
        :param key: Ключ атрибута
        :return: Значение атрибута
        """
        return self.dict[key]

    def __setitem__(self, key, value):
        """
        Изменяет значение аттрибута по ключу
        :param key: Ключ атрибута
        :param value: Значение атрибута
        :return: Значение атрибута
        """
        self.dict[key] = value
