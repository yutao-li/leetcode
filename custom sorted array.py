def moves(a):
    left = 0
    right = len(a) - 1
    move = 0
    while left < right:
        if a[left] % 2:
            left += 1
        elif a[right] % 2 == 0:
            right -= 1
        else:
            move += 1
            left += 1
            right -= 1
    return move
