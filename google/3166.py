from collections import Counter


class Wordle:
    def __init__(self, secret):
        self.secret = secret
        self.ch2pos = dict(zip(secret, range(len(secret))))

    def scoreWord(self, inputWord):
        ch2pos = dict(self.ch2pos)
        score = []
        for i, (ch1, ch2) in enumerate(zip(inputWord, self.secret)):
            if ch1 == ch2:
                score.append('G')
                del ch2pos[ch1]
            elif ch1 in ch2pos:
                if inputWord[ch2pos[ch1]] == ch1:
                    score.append('R')
                else:
                    score.append('Y')
                    del ch2pos[ch1]
            else:
                score.append('R')
        return ''.join(score)


class WordleWithRep:
    def __init__(self, secret):
        self.secret = secret
        self.chCounter = Counter(secret)

    def scoreWord(self, inputWord):
        chCounter = Counter(self.chCounter)
        score = [''] * len(self.secret)
        for i, (ch1, ch2) in enumerate(zip(inputWord, self.secret)):
            if ch1 == ch2:
                score[i] = 'G'
                chCounter[ch1] -= 1
            elif ch1 not in chCounter:
                score[i] = 'R'
        for i, (ch1, ch2) in enumerate(zip(inputWord, score)):
            if not ch2:
                if chCounter[ch1] > 0:
                    score[i] = 'Y'
                    chCounter[ch1] -= 1
                else:
                    score[i] = 'R'
        return ''.join(score)

    def vaidateGuess(self, guesses):
        chCounter = Counter()
        correctPos2Ch = dict()
        for guess in guesses:
            for pos, ch in correctPos2Ch.items():
                if not guess[pos] == ch:
                    return False
            guessCounter = Counter(guess)
            for ch, count in chCounter.items():
                if guessCounter[ch] < count:
                    return False
            score = self.scoreWord(guessCounter)
            for i, ch in enumerate(score):
                if ch == 'G':
                    correctPos2Ch[i] = guess[i]
            gyCounter = Counter(j for i, j in zip(score, guess) if i == 'G' or i == 'Y')
            for ch, count in gyCounter.items():
                chCounter[ch] = count
        return True
