class Manufacturer:

    _id = 0
    name = ''
    abbreviation = ''

    def __init__(self, id, name, abbreviation):
        self._id = id
        self.name = name
        self.abbreviation = abbreviation


    @classmethod
    def init1(self, id, name):
        return self(id, name, '')

    @classmethod
    def init2(self, id, name, abbreviation):
        return self(id, name, abbreviation)

    def toObject(self):
        return self.__dict__