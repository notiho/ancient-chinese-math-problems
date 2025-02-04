"""
今有棋局，方一十九道。問：用棋幾何？
術曰：置一十九道，自相乘之，即得。
答曰： a 。
"""

"""
To solve this problem, we are given a chessboard with 19 rows and 19 columns (a Go board). The task is to calculate the total number of intersections (points) on the board. The formula is to multiply the number of rows by the number of columns.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Number of rows and columns
rows = 19
columns = 19

# Calculate the total number of intersections
a = rows * columns
#----- content ends here -----


"""


The value of `a` will be the total number of intersections on the board.
"""


"""
"""
