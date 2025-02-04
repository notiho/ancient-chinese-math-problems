"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum (truncated prism) with the given dimensions. The formula provided in the problem is:

1. Double the upper length (袤) and add the lower length to it.
2. Double the lower length and add the upper length to it.
3. Multiply each result by its corresponding width (廣).
4. Add these two products together.
5. Multiply the sum by the height (高).
6. Divide the result by 6 to get the final volume.

The dimensions are:
- Lower width (下廣): 2丈
- Lower length (下袤): 3丈
- Upper width (上廣): 3丈
- Upper length (上袤): 4丈
- Height (高): 3丈

We will compute the volume step by step using Python code. Note that 1丈 = 10尺, so we will convert all dimensions to 尺 for the final answer.

Here is the Python code:


"""


from fractions import Fraction

# Dimensions in 丈
lower_width = 2  # 下廣
lower_length = 3  # 下袤
upper_width = 3  # 上廣
upper_length = 4  # 上袤
height = 3  # 高

# Convert dimensions to 尺 (1丈 = 10尺)
lower_width *= 10
lower_length *= 10
upper_width *= 10
upper_length *= 10
height *= 10

# Step 1: Double the upper length and add the lower length
upper_term = 2 * upper_length + lower_length

# Step 2: Double the lower length and add the upper length
lower_term = 2 * lower_length + upper_length

# Step 3: Multiply each term by its corresponding width
upper_area = upper_term * upper_width
lower_area = lower_term * lower_width

# Step 4: Add the two products together
total_area = upper_area + lower_area

# Step 5: Multiply the sum by the height
volume = total_area * height

# Step 6: Divide the result by 6
a = Fraction(volume, 6)

# The answer is stored in variable 'a' in 尺


"""


The variable `a` contains the volume in 尺.
"""


"""
"""
