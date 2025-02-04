"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the side length of a square when given its perimeter in steps. Here's the solution:


"""


from fractions import Fraction

# Given length of the rope in steps
total_length = 5794  # in steps

# Divide the total length by 4 to find the side length in steps
a = Fraction(total_length, 4)

# The result is stored in variable 'a'
a  # This represents the side length of the square in steps


"""


The value of `a` will be `1448` steps.
"""


"""
"""
