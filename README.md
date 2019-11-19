# py_snake

Create a function that for given string returns square matrix in such order:
from left to right; then from top to bottom; then from right to left and then from bottom to top.

For instance, for string "ABCDEFGHI":

ABC  
HID  
GFE

If length of string is not enough for square matrix building, add dots (".") to the end of string.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest`

`flake8 snake`

`pylint snake`

`mypy snake.py`