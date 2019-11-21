"""module docstring"""
import math


class Snake:
    """class fgfd"""
    def __init__(self, input_string):
        """f fdoc"""
        self.final_string = ""
        self.square_side_length = 0
        self.square_side_length_init = 0
        self.hor = -1
        self.vert = 0
        self.number = 0
        self.some_string = input_string


    def upside_move(self, square):
        """func docstring"""
        while self.vert >= 0 and square[self.vert - 1][self.hor] is None:
            self.vert -= 1
            square[self.vert][self.hor] = self.final_string[self.number]
            self.number += 1
        self.square_side_length = self.square_side_length - 1

    def left_move(self, square):
        """def docstring"""
        while self.number < len(self.final_string) \
                and square[self.vert][self.hor - 1] is None:
            self.hor -= 1
            square[self.vert][self.hor] = \
                self.final_string[self.number]
            self.number += 1
            if self.hor == 0 or square[self.vert][self.hor - 1] is not None:
                self.upside_move(square)

    def resolve(self):
        """ function docstring"""
        the_square = []
        final_string_dots = ""
        final_string_length = 0
        self.final_string = self.some_string
        self.square_side_length = int(math.sqrt(len(self.some_string)))

        if self.square_side_length ** 2 < len(self.some_string):
            self.square_side_length = self.square_side_length // 1 + 1

        final_string_length = self.square_side_length ** 2
        final_string_dots = final_string_length - len(self.some_string)
        if final_string_dots > 0:
            self.final_string += "." * final_string_dots

        self.square_side_length_init = self.square_side_length

        the_square = [[None] * self.square_side_length for i in range(self.square_side_length)]
        # filling the horizontal cells of the square to the right
        while self.number < len(self.final_string):
            self.hor += 1
            the_square[self.vert][self.hor] = self.final_string[self.number]
            self.number += 1
            if self.hor == self.square_side_length_init - 1 \
                    or the_square[self.vert][self.hor + 1] is not None:
                self.square_side_length -= 1
                # filling the vertical cells of the square downside
                for i in range(self.square_side_length):
                    if self.number != len(self.final_string) \
                            or the_square[self.vert + 1][self.hor] is None:
                        self.vert += 1
                        the_square[self.vert][self.hor] = \
                            self.final_string[self.number]
                        self.number += 1
                        if self.vert == self.square_side_length_init - 1 \
                                or the_square[self.vert + 1][self.hor] is not None:
                            self.left_move(the_square)
        result = ""
        for i in range(self.square_side_length_init):
            result += "".join(the_square[i])
            if i < self.square_side_length_init - 1:
                result += "\n"

        return result


def build_snake(some_string):
    """func docstring"""
    snake = Snake(some_string)
    return snake.resolve()
