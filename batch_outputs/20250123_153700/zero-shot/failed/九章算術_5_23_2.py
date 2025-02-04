"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum (truncated prism) based on the given dimensions. The formula provided in the problem is:

1. Double the top length (袤) and bottom length (袤), then multiply each by their respective widths (廣).
2. Add these two results together.
3. Multiply the sum by the height (高).
4. Divide the result by 6 to get the final volume.

The dimensions provided are:
- Bottom width (下廣): 2丈
- Bottom length (下袤): 3丈
- Top width (上廣): 3丈
- Top length (上袤): 4丈
- Height (高): 3丈

We will compute the volume step by step in Python. Note that 1丈 = 10尺, so we will convert all dimensions to 尺 before performing calculations.

Here is the Python code:


"""


from fractions import Fraction

# Dimensions in 丈
bottom_width = 2  # 下廣
bottom_length = 3  # 下袤
top_width = 3  # 上廣
top_length = 4  # 上袤
height = 3  # 高

# Convert dimensions to 尺 (1丈 = 10尺)
bottom_width *= 10
bottom_length *= 10
top_width *= 10
top_length *= 10
height *= 10

# Step 1: Double the top and bottom lengths
double_top_length = 2 * top_length
double_bottom_length = 2 * bottom_length

# Step 2: Multiply each by their respective widths
top_area = double_top_length * top_width
bottom_area = double_bottom_length * bottom_width

# Step 3: Add the two areas together
total_area = top_area + bottom_area

# Step 4: Multiply by height
volume = total_area * height

# Step 5: Divide by 6
a = Fraction(volume, 6)  # Volume in 尺

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the volume in 尺 as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 26500, Actual: 18000"""
