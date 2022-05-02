from typing import Callable
from threading import Semaphore, Barrier, Thread, Lock, Condition

INSERT = 0
COMBINE = 1


class H2O1:
    def __init__(self):
        self.lock = Lock()
        self.oCv = Condition(self.lock)
        self.hCv = Condition(self.lock)
        self.hRelease = Semaphore(0)
        self.oRelease = Semaphore(0)
        self.hNum = 0
        self.oNum = 0
        self.state = INSERT

    def combine(self):
        if self.hNum == 2 and self.oNum == 1:
            self.state = COMBINE
            self.hRelease.release(2)
            self.oRelease.release()

    def createNew(self):
        if self.hNum == 0 and self.oNum == 0:
            self.state = INSERT
            self.hCv.notify(2)
            self.oCv.notify()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.hCv:
            self.hCv.wait_for(lambda: self.hNum < 2 and self.state == INSERT)
            self.hNum += 1
            self.combine()
        self.hRelease.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        with self.hCv:
            self.hNum -= 1
            self.createNew()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.oCv:
            self.oCv.wait_for(lambda: self.oNum == 0 and self.state == INSERT)
            self.oNum = 1
            self.combine()
        self.oRelease.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        with self.oCv:
            self.oNum = 0
            self.createNew()


class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore()
        self.b = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h:
            self.b.wait()
            releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o:
            self.b.wait()
            releaseOxygen()


water = "OHOHOOHHOHHOOHHHHOOHOOHHOHHOOHHHOOHOHHOHHOHHHHHOHHHHHHHHHHHH"
ths = []
printH = lambda: print('H', end='')
printO = lambda: print('O', end='')
h2o = H2O()
for w in water:
    if w == 'H':
        th = Thread(target=h2o.hydrogen, args=(printH,))
    else:
        th = Thread(target=h2o.oxygen, args=(printO,))
    th.start()
    ths.append(th)
for t in ths:
    t.join()
