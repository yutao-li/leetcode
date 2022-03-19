# add cat (chasing rat) and dog (chasing cat), distributed system, malicious user


class PlayerInterface:
    characters = {"cat", "dog", "rat", "cheese"}

    def __init__(self, character):
        assert character in PlayerInterface.characters, "invalid character"

    def move(self, direction: int):
        assert 0 <= direction < 4, "invalid move."

    def getMap(self) -> [[str, int, int]]:
        pass


class GameInterface:
    def __init__(self):
        self.ID = 0
        self.id2pos = {}

    def createNewUser(self) -> int:
        self.ID += 1
        return self.ID

    def checkCollision(self, x: int, y: int):
        pass

    def move(self, id: int, direction: int):
        pass
