"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum (truncated prism) based on the given dimensions. The formula provided in the problem involves doubling the lengths of the top and bottom, multiplying by their respective widths, summing these areas, and then multiplying by the height. Finally, the result is divided by 6.

The dimensions are:
- Bottom width = 2丈
- Bottom length = 3丈
- Top width = 3丈
- Top length = 4丈
- Height = 3丈

We'll compute the volume step by step.

### Python Code:


"""


from fractions import Fraction

# Dimensions in 丈
bottom_width = Fraction(2)  # 下廣
bottom_length = Fraction(3)  # 下袤
top_width = Fraction(3)  # 上廣
top_length = Fraction(4)  # 上袤
height = Fraction(3)  # 高

# Step 1: Double the top and bottom lengths
double_top_length = top_length * 2
double_bottom_length = bottom_length * 2

# Step 2: Multiply by their respective widths
top_area = double_top_length * top_width
bottom_area = double_bottom_length * bottom_width

# Step 3: Sum the areas
total_area = top_area + bottom_area

# Step 4: Multiply by the height
volume = total_area * height

# Step 5: Divide by 6
a = volume / 6  # Volume in cubic 丈

# Result
a  # The volume in cubic 丈


"""


### Explanation:
1. **Double the lengths**: The problem specifies doubling the lengths of the top and bottom.
2. **Multiply by widths**: Each doubled length is multiplied by its respective width to calculate the area.
3. **Sum the areas**: Add the areas of the top and bottom.
4. **Multiply by height**: The total area is multiplied by the height of the frustum.
5. **Divide by 6**: The final result is divided by 6, as per the formula.

The result `a` will be the volume of the frustum in cubic 丈.
"""


"""
Variable 'a' has wrong value. Expected: 26500, Actual: 18"""
