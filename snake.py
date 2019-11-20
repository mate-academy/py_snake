"""module for sqrt and ceil"""
import math


def matrix_to_string(main_list):
    """converts matrix to string"""
    output = ""
    for sub_list in main_list:
        for element in sub_list:
            output += element
        output += "\n"
    return output.rstrip("\n")


def build_snake(string: str) -> str:
    """build snake"""
    # calculate size of matrix
    square_size = math.ceil(math.sqrt(len(string)))
    matrix: list = []
    # create matrix and fill it with dots
    for i in range(square_size):
        matrix.append([])
        for j in range(square_size):
            matrix[i].append(".")

    # loop trough matrix
    index_track = 0
    for iter_num in range(square_size):
        # from left to right
        for i in range(square_size - iter_num*2):
            matrix[iter_num][i + iter_num] = string[index_track]
            index_track += 1
            # added to avoid IndexError: string index out of range
            if index_track >= len(string):
                return matrix_to_string(matrix)
        # from top to bot
        for j in range(iter_num + 1, square_size - iter_num):
            matrix[j][square_size - iter_num - 1] = string[index_track]
            index_track += 1
            if index_track >= len(string):
                return matrix_to_string(matrix)
        # from right to left
        for k in range(iter_num + 1, square_size - iter_num):
            matrix[square_size - iter_num - 1][-k - 1] = string[index_track]
            index_track += 1
            if index_track >= len(string):
                return matrix_to_string(matrix)
        # from bot to top
        for i in range(iter_num + 1, square_size - (iter_num + 1)):
            matrix[-i - 1][iter_num] = string[index_track]
            index_track += 1
            if index_track >= len(string):
                return matrix_to_string(matrix)

    return matrix_to_string(matrix)
