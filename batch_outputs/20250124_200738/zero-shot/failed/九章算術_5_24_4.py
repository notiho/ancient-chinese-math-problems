"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves calculating the volume of a curved pool (曲池) using the given dimensions. The formula provided in the problem will be implemented step by step.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
upper_middle_perimeter = Fraction(2, 1)  # 2丈
upper_outer_perimeter = Fraction(4, 1)  # 4丈
upper_width = Fraction(1, 1)  # 1丈

lower_middle_perimeter = Fraction(1, 1) + Fraction(4, 10)  # 1丈4尺 = 1 + 4/10丈
lower_outer_perimeter = Fraction(2, 1) + Fraction(4, 10)  # 2丈4尺 = 2 + 4/10丈
lower_width = Fraction(5, 10)  # 5尺 = 5/10丈

depth = Fraction(1, 1)  # 1丈

# Step 1: Calculate the upper length (上袤)
upper_length = (upper_middle_perimeter + upper_outer_perimeter) / 2

# Step 2: Calculate the lower length (下袤)
lower_length = (lower_middle_perimeter + lower_outer_perimeter) / 2

# Step 3: Calculate the upper area and lower area
upper_area = upper_length * upper_width
lower_area = lower_length * lower_width

# Step 4: Add the upper and lower areas
total_area = upper_area + lower_area

# Step 5: Multiply by the depth
volume = total_area * depth

# Step 6: Divide by 6
a = volume / 6

# The result is in 丈^3, but we need the answer in 尺^3
# 1 丈^3 = 1000 尺^3
a = a * 1000

# The result
a  # Volume in 尺^3
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Dimensions**: All dimensions are converted into fractions for precise calculations. Units are in 丈 unless specified otherwise.
2. **Upper and Lower Lengths**: The formula for the upper and lower lengths is derived from the problem statement: the average of the middle and outer perimeters.
3. **Areas**: The upper and lower areas are calculated by multiplying the respective lengths by their widths.
4. **Volume**: The total area is multiplied by the depth, and the result is divided by 6 as per the formula.
5. **Unit Conversion**: The final volume is converted from 丈³ to 尺³ by multiplying by 1000.

### Final Answer:
The variable `a` contains the volume of the curved pool in 尺³.
"""


"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 1975/3"""
