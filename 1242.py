from collections import deque
from typing import List
from threading import Thread, Lock
from concurrent import futures


class HtmlParser(object):
    """
    This is HtmlParser's API interface.
    You should not implement it, or speculate about its implementation
    """

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


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def parse(url: str):
            subUrls = []
            for u in htmlParser.getUrls(url):
                if u[7:(u + '/').find('/', 7)] == domain:
                    with seenLock:
                        if u not in seen:
                            seen.add(u)
                            subUrls.append(u)
            threads = []
            for u in subUrls:
                t = Thread(target=parse, args=(u,))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()

        seenLock = Lock()
        seen = {startUrl}
        domain = startUrl[7:(startUrl + '/').find('/', 7)]
        t = Thread(target=parse, args=(startUrl,))
        t.start()
        t.join()
        return list(seen)


class Solution1:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        return list(seen)


inp = [["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/",
        "http://news.google.com", "http://news.yahoo.com/us"]
    , [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]
    , "http://news.yahoo.com/news/topics/"]
parser = HtmlParser(inp[0], inp[1])
res = Solution().crawl(inp[2], parser)
print(res)
