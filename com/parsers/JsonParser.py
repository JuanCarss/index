from json import loads


class JsonParser:

    @staticmethod
    def parse(jsonString):
        return loads(jsonString)
