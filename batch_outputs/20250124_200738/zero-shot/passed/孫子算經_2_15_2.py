"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves dividing the length of a rope (索) into a square shape, and the answer is given in steps (步). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given length of the rope in steps
length = 5794  # in steps

# Step 1: Divide the length by 4
a = Fraction(length, 4)

# The answer is the number of steps
a  # This is the answer in steps
#----- content ends here -----


"""


The solution variable `a` will contain the value of the number of steps.
"""


"""
"""
