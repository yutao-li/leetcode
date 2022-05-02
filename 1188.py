from threading import Condition, Lock
from concurrent.futures import ThreadPoolExecutor


# deque is not allowed since it's thread safe by its own.
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.revStack = []
        self.lock = Lock()
        self.produceCv = Condition(self.lock)
        self.consumeCv = Condition(self.lock)

    def enqueue(self, element: int) -> None:
        with self.produceCv:
            self.produceCv.wait_for(lambda: len(self.stack) + len(self.revStack) < self.capacity)
            self.stack.append(element)
            self.consumeCv.notify()

    def dequeue(self) -> int:
        with self.consumeCv:
            self.consumeCv.wait_for(lambda: self.revStack or self.stack)
            if not self.revStack:
                self.revStack = self.stack[::-1]
                self.stack = []
            res = self.revStack.pop()
            self.produceCv.notify()
        return res

    def size(self) -> int:
        return len(self.stack) + len(self.revStack)


bbq = BoundedBlockingQueue(3)
res = []
with ThreadPoolExecutor(1) as producer, ThreadPoolExecutor(2) as consumer:
    tasks = [consumer.submit(bbq.dequeue) for _ in range(3)] + [producer.submit(bbq.enqueue, 0) for _ in range(4)]
    for t in tasks:
        res.append(t.result())
        print(res)
