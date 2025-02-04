"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the volume of a curved pool (曲池) using the given formula. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
upper_middle_perimeter = Fraction(2 * 10)  # 二丈 = 2丈 = 20尺
upper_outer_perimeter = Fraction(4 * 10)  # 四丈 = 4丈 = 40尺
upper_width = Fraction(1 * 10)  # 一丈 = 10尺

lower_middle_perimeter = Fraction(1 * 10 + 4)  # 一丈四尺 = 14尺
lower_outer_perimeter = Fraction(2 * 10 + 4)  # 二丈四尺 = 24尺
lower_width = Fraction(5)  # 五尺 = 5尺

depth = Fraction(1 * 10)  # 一丈 = 10尺

# Step 1: Calculate upper length (上袤)
upper_length = (upper_middle_perimeter + upper_outer_perimeter) / 2

# Step 2: Calculate lower length (下袤)
lower_length = (lower_middle_perimeter + lower_outer_perimeter) / 2

# Step 3: Calculate the volume
# Formula: [(倍上袤 * 上廣) + (倍下袤 * 下廣)] * 深 / 6
volume = ((2 * upper_length * upper_width) + (2 * lower_length * lower_width)) * depth / 6

# The answer
a = volume
a  # The volume in cubic 尺


"""


### Explanation:
1. **Units**: All dimensions are converted to 尺 (1丈 = 10尺).
2. **Formulas**:
   - The upper length (上袤) is the average of the upper middle perimeter and the upper outer perimeter.
   - The lower length (下袤) is the average of the lower middle perimeter and the lower outer perimeter.
   - The volume is calculated using the formula provided in the problem.
3. **Result**: The variable `a` contains the volume in cubic 尺.

You can run this code to compute the value of `a`.
"""


"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 3950/3"""
