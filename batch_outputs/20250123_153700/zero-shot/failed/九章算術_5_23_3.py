"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will follow the ancient Chinese method described in the problem. The shape described is a frustum of a rectangular pyramid. The formula for the volume of such a frustum is given in the problem:

1. Double the upper length (袤) and add it to the lower length (袤), then double the lower length and add it to the upper length.
2. Multiply each result by its corresponding width (廣).
3. Add these two products together.
4. Multiply the sum by the height (高).
5. Divide the result by 6 to get the final volume.

Here is the Python code to compute the volume:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(2)  # 下廣 (2丈)
lower_length = Fraction(3)  # 下袤 (3丈)
upper_width = Fraction(3)  # 上廣 (3丈)
upper_length = Fraction(4)  # 上袤 (4丈)
height = Fraction(3)  # 高 (3丈)

# Step 1: Compute the doubled lengths and their sums
double_upper_length = 2 * upper_length
double_lower_length = 2 * lower_length

# Step 2: Multiply each by its corresponding width
upper_area = double_upper_length * lower_width
lower_area = double_lower_length * upper_width

# Step 3: Add the two areas together
total_area = upper_area + lower_area

# Step 4: Multiply by the height
volume = total_area * height

# Step 5: Divide by 6
a = volume / 6  # Volume in cubic 丈

# The answer is stored in the variable 'a'


"""


The variable `a` contains the volume of the frustum in cubic 丈.
"""


"""
Variable 'a' has wrong value. Expected: 26500, Actual: 17"""
