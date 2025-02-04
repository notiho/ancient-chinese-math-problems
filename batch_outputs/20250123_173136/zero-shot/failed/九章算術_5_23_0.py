"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a frustum (truncated prism) using the given dimensions. The formula for the volume of a frustum is provided in the problem statement. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(2)  # 下廣 (2丈)
lower_length = Fraction(3)  # 下袤 (3丈)
upper_width = Fraction(3)  # 上廣 (3丈)
upper_length = Fraction(4)  # 上袤 (4丈)
height = Fraction(3)  # 高 (3丈)

# Step 1: Calculate the area of the lower base and upper base
lower_area = lower_width * lower_length  # 下廣 * 下袤
upper_area = upper_width * upper_length  # 上廣 * 上袤

# Step 2: Add the areas of the lower base and upper base
sum_of_areas = lower_area + upper_area

# Step 3: Multiply the height by the sum of the areas
volume = (sum_of_areas * height) / Fraction(6)  # Divide by 6 as per the formula

# The result is in 丈^3, convert to 尺^3 (1丈 = 10尺, so 1丈^3 = 1000尺^3)
a = volume * Fraction(1000)

# The answer is stored in variable 'a'


"""


The variable `a` now contains the volume of the frustum in cubic 尺 (尺^3).
"""


"""
Variable 'a' has wrong value. Expected: 26500, Actual: 9000"""
