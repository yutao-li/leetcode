from typing import Callable


def filterByPredicate(array, predicate: Callable):
    n = len(array)
    left = 0
    right = n - 1
    while left <= right:
        if predicate(array[left]):
            left += 1
        elif not predicate(array[right]):
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]
            right -= 1
            left += 1
    return array[:left]


def filterByPredicateInOrder(array, predicate: Callable):
    n = len(array)
    toIndex = 0
    while toIndex < n and predicate(array[toIndex]):
        toIndex += 1
    fromIndex = toIndex + 1
    while fromIndex < n:
        if not predicate(array[fromIndex]):
            fromIndex += 1
        elif predicate(array[toIndex]):
            toIndex += 1
        else:
            array[fromIndex], array[toIndex] = array[toIndex], array[fromIndex]
            fromIndex += 1
            toIndex += 1
    return array[:toIndex]
