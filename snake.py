'''Module'''
import math


def spiral_print(end_row_index, end_column_index, array):
    '''

    :param end_row_index:
    :param end_column_index:
    :param a:
    :return:
    '''
    start_row_index = 0
    start_column_index = 0
    count = 0

    while start_row_index < end_row_index and start_column_index < end_column_index:

        # Print the first row from
        # the remaining rows
        for i in range(start_column_index, end_column_index):
            array[start_row_index][i] = count
            count += 1

        start_row_index += 1

        # Print the last column from
        # the remaining columns
        for i in range(start_row_index, end_row_index):
            array[i][end_column_index - 1] = count
            count += 1

        end_column_index -= 1

        # Print the last row from
        # the remaining rows
        if start_row_index < end_row_index:
            for i in range(end_column_index - 1, (start_column_index - 1), -1):
                array[end_row_index - 1][i] = count
                count += 1

            end_row_index -= 1

        # Print the first column from
        # the remaining columns
        if start_column_index < end_column_index:
            for i in range(end_row_index - 1, start_row_index - 1, -1):
                array[i][start_column_index] = count
                count += 1
            start_column_index += 1
    return array


def build_snake(strng: str) -> str:
    '''

    :param strng:
    :return:
    '''
    lngth = math.sqrt(len(strng))
    lngth = (int(lngth) + 1) if lngth % 1 > 0 else int(lngth)
    arr: list = [[] for _ in range(lngth)]
    for i in range(lngth):
        for j in range(lngth):
            arr[i].append('-')
    arr = spiral_print(lngth, lngth, arr)
    result_line = ''
    len_matrix = len(arr)
    for i in range(len_matrix):
        for j in range(len_matrix):
            if arr[i][j] < len(strng):
                result_line += strng[arr[i][j]]
            else:
                result_line += '.'
        result_line += '\n'
    return result_line[:-1]
