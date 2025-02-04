"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the "盤池" (a trapezoidal prism) using the given formula. The dimensions are:

- Top length (上袤): 8 丈
- Top width (上廣): 6 丈
- Bottom length (下袤): 6 丈
- Bottom width (下廣): 4 丈
- Depth (深): 2 丈

The formula provided is:

1. Double the top length (上袤) and add the bottom length (下袤).
2. Double the bottom length (下袤) and add the top length (上袤).
3. Multiply each result by its respective width (廣).
4. Add these two products together.
5. Multiply the sum by the depth (深).
6. Divide the result by 6 to get the final volume.

We will compute the solution step by step in Python.


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions in 丈
top_length = Fraction(8)  # 上袤
top_width = Fraction(6)   # 上廣
bottom_length = Fraction(6)  # 下袤
bottom_width = Fraction(4)   # 下廣
depth = Fraction(2)  # 深

# Step 1: Double the top length and add the bottom length
term1 = 2 * top_length + bottom_length

# Step 2: Double the bottom length and add the top length
term2 = 2 * bottom_length + top_length

# Step 3: Multiply each term by its respective width
area1 = term1 * top_width
area2 = term2 * bottom_width

# Step 4: Add the two areas together
total_area = area1 + area2

# Step 5: Multiply the total area by the depth
volume = total_area * depth

# Step 6: Divide the result by 6
a = volume / 6  # Volume in cubic 丈

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the volume of the trapezoidal prism in cubic 丈.
"""


"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 212/3"""
