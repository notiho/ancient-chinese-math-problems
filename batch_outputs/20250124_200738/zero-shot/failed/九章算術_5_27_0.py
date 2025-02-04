"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will compute the volume of the "冥谷" (a type of irregular prism) using the given method. The formula involves doubling the lengths of the top and bottom sides, multiplying by their respective widths, summing the results, and then multiplying by the depth. Finally, we divide the result by 6 to get the volume.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
top_width = Fraction(2 * 10)  # 2丈 = 20尺
top_length = Fraction(7 * 10)  # 7丈 = 70尺
bottom_width = Fraction(8)  # 8尺
bottom_length = Fraction(4 * 10)  # 4丈 = 40尺
depth = Fraction(6 * 10 + 5)  # 6丈5尺 = 65尺

# Calculations
top_area = (2 * top_length) * top_width
bottom_area = (2 * bottom_length) * bottom_width
combined_area = top_area + bottom_area
volume = (combined_area * depth) / 6

# Answer
a = volume  # Volume in cubic 尺
#----- content ends here -----


"""


The variable `a` will contain the volume of the "冥谷" in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
