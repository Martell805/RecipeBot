class Context:
    """
    Class which stores all global variables and provides access to them
    """
    def __init__(self):
        self.dict = dict()

    def get_attribute(self, key):
        """
        Returns value for given key
        :param key: Attribute`s key
        :return: Attribute`s value
        """
        return self.dict[key]

    def set_attribute(self, key, value):
        """
        Changes or adds and returns value for given key
        :param key: Attribute`s key
        :param value: Attribute`s value
        :return: Attribute`s value
        """
        self.dict[key] = value
        return self.dict[key]

    def delete_attribute(self, key):
        """
        Deletes and returns value for given key
        :param key: Attribute`s key
        :param value: Attribute`s value
        :return: Attribute`s value
        """
        value = self.dict[key]
        del self.dict[key]
        return value

    def __getitem__(self, key):
        """
        Returns value for given key
        :param key: Attribute`s key
        :return: Attribute`s value
        """
        return self.dict[key]

    def __setitem__(self, key, value):
        """
        Changes or adds value for given key
        :param key: Attribute`s key
        :param value: Attribute`s value
        :return: Attribute`s value
        """
        self.dict[key] = value
