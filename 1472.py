from typing import List


class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.stack[self.pos + 1:] = [url]
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos -= steps
        if self.pos < 0:
            self.pos = 0
        return self.stack[self.pos]

    def forward(self, steps: int) -> str:
        self.pos += steps
        if self.pos >= len(self.stack):
            self.pos = len(self.stack) - 1
        return self.stack[self.pos]


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)
