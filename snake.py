"""Containing function
    build_snake(str)
"""

def build_snake(string: str) -> str:
    """Wraps given string into a square matrix"""
    if len(string) < 2:
        return string

    side = len(string) ** 0.5
    row = int(side) if side % 1 == 0 else int(side) + 1
    array = [['*'] * row for _ in range(row)]
    sent = list(string) + ['.'] * (row ** 2 - len(string))
    left = 0
    right = row
    res = ''

    while right - left >= 2:
        for j in range(left, right):
            i = left
            array[i][j] = sent.pop(0)

        for i in range(left + 1, right):
            j = right - 1
            array[i][j] = sent.pop(0)

        for j in range(right - 2, left - 1, -1):
            i = right - 1
            array[i][j] = sent.pop(0)

        for i in range(right - 2, left, -1):
            j = left
            array[i][j] = sent.pop(0)
        right -= 1
        left += 1

    if right - left == 1:
        array[left][left] = sent.pop(0)

    for i in range(row):
        for j in range(row):
            res += array[i][j]
        if i != row - 1:
            res += '\n'

    return res
