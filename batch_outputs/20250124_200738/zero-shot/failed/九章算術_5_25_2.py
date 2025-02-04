"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve the problem, we need to calculate the volume of a trapezoidal prism (盤池). The formula provided in the problem can be translated into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
upper_length = Fraction(6 * 10)  # Convert 丈 to 尺 (1 丈 = 10 尺)
upper_width = Fraction(8 * 10)   # Convert 丈 to 尺
lower_length = Fraction(4 * 10)  # Convert 丈 to 尺
lower_width = Fraction(6 * 10)   # Convert 丈 to 尺
depth = Fraction(2 * 10)         # Convert 丈 to 尺

# Step 1: Double the upper length and add the lower length
upper_length_doubled = upper_length * 2
lower_length_doubled = lower_length * 2

# Step 2: Multiply each by their respective widths
upper_area = upper_length_doubled * upper_width
lower_area = lower_length_doubled * lower_width

# Step 3: Add the two areas together
total_area = upper_area + lower_area

# Step 4: Multiply by the depth
volume = total_area * depth

# Step 5: Divide by 6
a = volume / 6

# The answer is stored in variable `a` in 尺³
a
#----- content ends here -----


"""


### Explanation:
1. Convert all dimensions from 丈 to 尺 (1 丈 = 10 尺).
2. Follow the steps in the problem:
   - Double the upper length and multiply by the upper width.
   - Double the lower length and multiply by the lower width.
   - Add the two areas together.
   - Multiply by the depth.
   - Divide the result by 6 to get the final volume.
3. The result is stored in the variable `a` in cubic 尺 (尺³).
"""


"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 48000"""
