from collections import Counter
from functools import cache


class Stack:
    def __init__(self, height, color):
        self.height = height
        self.color = color


class BabylonGame:
    def __init__(self):
        self.state = [Stack(1, color) for color in range(4) for _ in range(3)]

    def getStacks(self):
        return self.state

    def move(self, stack1, stack2):
        pass


class Player:
    def __init__(self, game):
        self.game = game

    def canWin(self):
        def convertStacksToUniqueState(stacks):
            return tuple(sorted(Counter(stacks).items()))

        def convertUniqueStateToStacks(state):
            return [i for i, j in state for _ in range(j)]

        def possibleNextStates(state):
            stacks = convertUniqueStateToStacks(state)
            n = len(stacks)
            newStates = set()
            for i in range(n):
                for j in range(i + 1, n):
                    h1, c1 = stacks[i]
                    h2, c2 = stacks[j]
                    if h1 == h2 or c1 == c2:
                        newStacks = list(stacks)
                        newStacks.pop(j)
                        newStacks.pop(i)
                        state1 = convertStacksToUniqueState(newStacks + [(h1 + h2, c1)])
                        state2 = convertStacksToUniqueState(newStacks + [(h1 + h2, c2)])
                        newStates.add(state1)
                        newStates.add(state2)
            return newStates

        @cache
        def deduce(state, myTurn):  # True => win, False => lose
            nextStates = possibleNextStates(state)
            if not nextStates:
                return not myTurn
            if myTurn:
                return any(deduce(state1, not myTurn) for state1 in nextStates)
            else:
                return not any(not deduce(state1, not myTurn) for state1 in nextStates)

        stacks = [(s.height, s.color) for s in self.game.getStacks()]
        state = convertStacksToUniqueState(stacks)
        return deduce(state, True)


game = BabylonGame()
playerFirst = Player(game)
print(playerFirst.canWin())
