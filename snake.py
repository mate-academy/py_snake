"""Snake build matrix module"""
import math


def build_snake(text: str) -> str:
    """Snake build matrix function"""
    size = len(text)**0.5
    size = int(math.ceil(size))
    if size < 2:
        return text
    result = []  # type: list
    #  Заполняем матрицу точками
    for coord_x in range(size):
        result.append([])
        for _ in range(size):
            result[coord_x].append(".")
    #  Заполняем матрицу значениями
    division_size = size // 2
    if size % 2 != 0 and len(text) == size**2:
        result[division_size][division_size] = text[-1]
    koef = 0
    text_index = 0
    for prhod in range(division_size):
        try:
            # Заполнение верхней горизонтальной матрицы
            for i in range(size - koef):
                result[prhod][i + prhod] = text[text_index]
                text_index += 1
            # Заполнение правой вертикальной матрицы
            for i in range(prhod + 1, size - prhod):
                result[i][-prhod - 1] = text[text_index]
                text_index += 1
            # Заполнение нижней горизонтальной матрицы
            for i in range(prhod + 1, size - prhod):
                result[-prhod - 1][-i - 1] = text[text_index]
                text_index += 1
            # Заполнение левой вертикальной матрицы
            for i in range(prhod + 1, size - (prhod + 1)):
                result[-i - 1][prhod] = text[text_index]
                text_index += 1
            koef += 2
        except IndexError:
            break
    #  превращаем матрицу в строку
    result_text = ""
    for result_index in range(size):
        for mini_result in result[result_index]:
            result_text += mini_result
        result_text += "\n"
    return result_text[:-1]
