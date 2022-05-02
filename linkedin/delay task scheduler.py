from threading import Lock, Thread
from typing import Callable
from time import time, sleep
from heapq import heappush, heappop
from collections import deque


class DelayTask:
    def __init__(self, shard: int = 1):
        def scan(shard):
            while True:
                if self.q[shard] and self.q[shard][0][0] <= time():
                    with self.lock[shard]:
                        task = heappop(self.q[shard])[1]
                    if not task:
                        return
                    th = Thread(target=task)
                    th.start()
                    while self.running[shard] and not self.running[shard][0].is_alive():
                        self.running[shard].popleft()
                    self.running[shard].append(th)

        self.q = [[] for _ in range(shard)]
        self.running = [deque() for _ in range(shard)]
        self.lock = [Lock() for _ in range(shard)]
        self.shard = shard
        self.scanners = []
        for i in range(shard):
            th = Thread(target=scan, args=(i,))
            th.start()
            self.scanners.append(th)

    def addTask(self, task: Callable, delay: int):
        ts = time() + delay
        i = hash(task) % self.shard
        with self.lock[i]:
            heappush(self.q[i], (ts, task))

    def shutdown(self):
        for i in range(self.shard):
            with self.lock[i]:
                heappush(self.q[i], (float('-inf'), None))
        for th in self.scanners:
            th.join()
        for q in self.running:
            while q:
                th = q.pop()
                th.join()


dt = DelayTask(10)
f = lambda: print(time())
for _ in range(10):
    dt.addTask(f, 1)
sleep(5)
dt.shutdown()
