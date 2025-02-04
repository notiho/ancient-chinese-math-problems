"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a trapezoidal prism (盤池). The formula provided in the problem involves doubling the lengths of the top and bottom dimensions, multiplying by their respective widths, summing the results, and then multiplying by the depth. Finally, the result is divided by 6.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
top_length = Fraction(6 * 10)  # Convert from 丈 to 尺 (1 丈 = 10 尺)
top_width = Fraction(8 * 10)   # Convert from 丈 to 尺
bottom_length = Fraction(4 * 10)  # Convert from 丈 to 尺
bottom_width = Fraction(6 * 10)   # Convert from 丈 to 尺
depth = Fraction(2 * 10)  # Convert from 丈 to 尺

# Calculation
top_area = (2 * top_length) * top_width
bottom_area = (2 * bottom_length) * bottom_width
sum_areas = top_area + bottom_area
volume = (sum_areas * depth) / 6

# Assign the result to variable 'a'
a = volume

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the volume of the trapezoidal prism in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 48000"""
