from collections import Counter, deque


def removeMinElementsFromList2(list1, list2, k):
    set1 = set(list1[:k])
    i = 0
    newList2 = []
    while len(newList2) < k and i < len(list2):
        if list2[i] not in set1:
            newList2.append(list2[i])
        i += 1
    newList2 += list2[i:]
    return newList2


def removeMinElementsFromNList(lists, k, d):
    if not lists:
        return []
    if d < 1:
        return lists
    elementCounter = Counter()
    prevKWindows = deque()
    res = []
    for i, iList in enumerate(lists):
        curList = []
        pos = 0
        while len(curList) < k and pos < len(iList):
            if iList[pos] in elementCounter:
                curList.append(iList[pos])
            pos += 1
        res.append(curList + iList[pos:])
        prevKWindows.append(curList)
        elementCounter.update(curList)
        if i >= d:
            elementCounter -= Counter(prevKWindows.popleft())
    return res


list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 1, 1, 2, 4, 5, 6, 1]
list3 = [3, 1, 1, 2, 4, 5, 6, 1, 1, 2, 3, 4, 5, 6]
print(removeMinElementsFromList2(list1, list2, 1))
print(removeMinElementsFromList2(list1, list2, 2))
print(removeMinElementsFromNList([list1, list2, list3], 3, 2))
