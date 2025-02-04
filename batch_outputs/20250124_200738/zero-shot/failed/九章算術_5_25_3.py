"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the "盤池" (a trapezoidal prism). The formula provided in the problem states that we need to calculate the average of the top and bottom areas, then multiply by the depth, and finally divide by 6 to get the result.

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
top_length = Fraction(8 * 10)  # Convert from 丈 to 尺 (1 丈 = 10 尺)
top_width = Fraction(6 * 10)   # Convert from 丈 to 尺
bottom_length = Fraction(6 * 10)  # Convert from 丈 to 尺
bottom_width = Fraction(4 * 10)   # Convert from 丈 to 尺
depth = Fraction(2 * 10)  # Convert from 丈 to 尺

# Step 1: Calculate the area of the top and bottom
top_area = top_length * top_width
bottom_area = bottom_length * bottom_width

# Step 2: Add the areas together
total_area = top_area + bottom_area

# Step 3: Multiply by the depth
volume = total_area * depth

# Step 4: Divide by 6
a = volume / 6

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the volume of the "盤池" in cubic 尺 (尺³).
"""


"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 24000"""
