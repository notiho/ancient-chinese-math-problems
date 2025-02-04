"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves calculating the volume of a curved pool ("曲池") with given dimensions. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
upper_middle_perimeter = Fraction(2 * 10)  # 2丈 = 20尺
upper_outer_perimeter = Fraction(4 * 10)  # 4丈 = 40尺
upper_width = Fraction(1 * 10)  # 1丈 = 10尺

lower_middle_perimeter = Fraction(1 * 10 + 4)  # 1丈4尺 = 14尺
lower_outer_perimeter = Fraction(2 * 10 + 4)  # 2丈4尺 = 24尺
lower_width = Fraction(5)  # 5尺

depth = Fraction(1 * 10)  # 1丈 = 10尺

# Step 1: Calculate the upper length (上袤)
upper_length = (upper_middle_perimeter + upper_outer_perimeter) / 2

# Step 2: Calculate the lower length (下袤)
lower_length = (lower_middle_perimeter + lower_outer_perimeter) / 2

# Step 3: Calculate the upper area and lower area
upper_area = upper_length * upper_width
lower_area = lower_length * lower_width

# Step 4: Add the upper area and lower area
total_area = upper_area + lower_area

# Step 5: Multiply by the depth and divide by 6
a = (total_area * depth) / 6

# The result is stored in variable 'a'
print(f"The volume of the curved pool is {a} cubic 尺.")


"""


This code calculates the volume of the curved pool using the method described in the problem. The result is stored in the variable `a`, which represents the volume in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 1975/3"""
