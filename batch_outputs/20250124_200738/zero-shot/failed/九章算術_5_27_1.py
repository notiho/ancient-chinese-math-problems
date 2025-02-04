"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the "冥谷" (a type of irregular prism) using the given method. The method involves doubling the lengths of the top and bottom sides, calculating their areas, summing them, and multiplying by the depth, then dividing by 6.

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

# Step 1: Double the top length and bottom length
double_top_length = 2 * top_length
double_bottom_length = 2 * bottom_length

# Step 2: Calculate the areas of the top and bottom
top_area = double_top_length * top_width
bottom_area = double_bottom_length * bottom_width

# Step 3: Sum the areas and multiply by the depth
volume = (top_area + bottom_area) * depth

# Step 4: Divide the result by 6
a = volume / 6

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the volume of the "冥谷" in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
