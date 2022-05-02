from collections import deque, defaultdict


class Offer:
    def __init__(self, type: str, name: str, quantity: int):
        self.type = type
        self.name = name
        self.quantity = quantity


def matchOffers(offers: [Offer]):
    buzzQueue = deque([[offer.name, offer.quantity] for offer in offers if offer.type == 'Buzz'])
    fizzQueue = deque([[offer.name, offer.quantity] for offer in offers if offer.type == 'Fizz'])
    match = defaultdict(int)
    while buzzQueue and fizzQueue:
        n1, q1 = fizzQueue[0]
        n2, q2 = buzzQueue[0]
        if q1 < q2:
            buzzQueue[0][1] -= q1
            fizzQueue.popleft()
        elif q1 > q2:
            fizzQueue[0][1] -= q2
            buzzQueue.popleft()
        else:
            buzzQueue.popleft()
            fizzQueue.popleft()
        match[n1, n2] += min(q1, q2)
    for (n1, n2), q in match.items():
        print("FizzBuzz! " + str(q) + " " + n1 + ":" + n2)


offers = [Offer('Fizz', 'Alice', 5), Offer('Buzz', 'Bob', 3), Offer('Buzz', 'Catherine', 4), Offer('Fizz', 'Alice', 4),
          Offer('Buzz', 'Bob', 2)]
matchOffers(offers)
