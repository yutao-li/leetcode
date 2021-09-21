from typing import List


class FileSystem:

    def __init__(self):
        self.root = dict()
        self.root[0] = dict()

    def ls(self, path: str) -> List[str]:
        path = path.split('/')[1:]
        cur = self.root
        if path[-1] == '':
            res = sorted(list(cur[0].keys()) + [k for k in cur.keys() if k != 0])
        else:
            for di in path[:-1]:
                cur = cur[di]
            if path[-1] in cur:
                cur = cur[path[-1]]
                res = sorted(list(cur[0].keys()) + [k for k in cur.keys() if k != 0])
            else:
                res = [path[-1]]
        return res

    def mkdir(self, path: str) -> None:
        path = path.split('/')[1:]
        cur = self.root
        for di in path:
            if di not in cur:
                cur[di] = dict()
                cur[di][0] = dict()
            cur = cur[di]

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath = filePath.split('/')[1:]
        cur = self.root
        for di in filePath[:-1]:
            cur = cur[di]
        cur = cur[0]
        if filePath[-1] in cur:
            cur[filePath[-1]] = cur[filePath[-1]] + content
        else:
            cur[filePath[-1]] = content

    def readContentFromFile(self, filePath: str) -> str:
        filePath = filePath.split('/')[1:]
        cur = self.root
        for di in filePath[:-1]:
            cur = cur[di]
        cur = cur[0]
        return cur[filePath[-1]]


# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.ls('/')
obj.mkdir('/a/b/c')
obj.ls('/a/b')
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
