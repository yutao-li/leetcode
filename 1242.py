"""
This is HtmlParser's API interface.
You should not implement it, or speculate about its implementation
"""
from typing import List


class HtmlParser(object):
    def __init__(self, urls, edges):
        self.urls = urls
        self.url2pos = dict(zip(urls, range(len(urls))))
        self.adj = [[] for _ in range(len(urls) + 1)]
        for i, j in edges:
            self.adj[i].append(j)

    def getUrls(self, url):
        """
        :type url: str
        :rtype List[str]
        """
        return [self.urls[i] for i in self.adj[self.url2pos[url]]]


from threading import Thread, Lock, active_count
from queue import Queue


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        seen = {startUrl}
        domain = startUrl[7:(startUrl + '/').find('/', 7)]
        todo = Queue()
        for i in htmlParser.getUrls(startUrl):
            if i[7:(i + '/').find('/', 7)] == domain:
                todo.put(i)
                seen.add(i)
        seen_lock = Lock()
        init = active_count()

        def th(url):
            for i in htmlParser.getUrls(url):
                if i[7:(i + '/').find('/', 7)] == domain:
                    with seen_lock:
                        if i not in seen:
                            seen.add(i)
                            todo.put(i)

        while True:
            # print(active_count())
            if not todo.empty():
                Thread(target=th, args=(todo.get(),)).start()
                # print(active_count())
            elif active_count() == init:
                break

        return list(seen)


inp = [["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/",
        "http://news.google.com", "http://news.yahoo.com/us"]
    , [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]
    , "http://news.yahoo.com/news/topics/"]
parser = HtmlParser(inp[0], inp[1])
res = Solution().crawl(inp[2], parser)
print(len(res))
