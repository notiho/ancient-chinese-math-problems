"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a "冥谷" (a type of irregular prism). The solution is based on the method described in the problem. Here's the Python code to compute the value of the unknown `a`:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(2 * 10)  # Convert 2丈 to 尺 (1丈 = 10尺)
top_length = Fraction(7 * 10)  # Convert 7丈 to 尺
bottom_width = Fraction(8)  # 8尺
bottom_length = Fraction(4 * 10)  # Convert 4丈 to 尺
depth = Fraction(6 * 10 + 5)  # Convert 6丈5尺 to 尺

# Step 1: Double the top length and use the bottom length as is
double_top_length = 2 * top_length
bottom_length_as_is = bottom_length
top_area = double_top_length * top_width

# Step 2: Double the bottom length and use the top length as is
double_bottom_length = 2 * bottom_length
top_length_as_is = top_length
bottom_area = double_bottom_length * bottom_width

# Step 3: Add the two areas together
total_area = top_area + bottom_area

# Step 4: Multiply by the depth
volume = total_area * depth

# Step 5: Divide by 6
a = volume / 6

# The result is stored in variable `a` in 尺³ (cubic 尺)


"""


The variable `a` now contains the volume of the "冥谷" in cubic 尺 (尺³).
"""


"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
