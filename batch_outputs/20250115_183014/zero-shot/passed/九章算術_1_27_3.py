"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a slanted (trapezoidal) field. Here's the Python code:


"""


from fractions import Fraction

# Given values
正廣 = 65  # 正廣 (width) in steps
一畔從 = 100  # One side length in steps
一畔從_2 = 72  # Other side length in steps

# Calculation
并兩邪 = 一畔從 + 一畔從_2  # Sum of the two slanted sides
并兩邪而半之 = Fraction(并兩邪, 2)  # Average of the two slanted sides
a = 并兩邪而半之 * 正廣  # Area in steps^2

# Convert to 畝 (assuming 1 畝 = 240 steps^2 as per ancient Chinese units)
a = a / 240

# Result
a  # Area in 畝


"""


The variable `a` will hold the area of the field in 畝.
"""


"""
"""
