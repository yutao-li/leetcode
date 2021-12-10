def function(A: list):
    A.sort()
    if len(A) <= 4:
        return 0
    else:
        return min(A[-1] - A[3], A[-2] - A[2], A[-3] - A[1], A[-4] - A[0])
