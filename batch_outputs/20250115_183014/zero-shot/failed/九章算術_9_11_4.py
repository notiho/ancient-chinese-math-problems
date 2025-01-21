"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves finding the dimensions of a door (height, width, and diagonal length) based on the given constraints. Here's the Python code:


"""


from fractions import Fraction
import math

# Given values
horizontal = Fraction(4)  # Horizontal length (橫) in 尺
vertical = Fraction(2)    # Vertical length (從) in 尺

# Calculations
diagonal_squared = horizontal * vertical * 2  # 橫不出 * 從不出 * 2
diagonal = Fraction(math.sqrt(diagonal_squared))  # 開方 to find the diagonal

# Door dimensions
a = vertical + diagonal  # 廣 (width)
b = horizontal + diagonal  # 高 (height)
c = (horizontal + vertical) / 10  # 袤 (diagonal length in 丈)

# Results
a, b, c


"""


### Explanation:
1. **Input values**: The horizontal and vertical lengths are given as 4 尺 and 2 尺, respectively.
2. **Diagonal squared**: The product of horizontal and vertical lengths is multiplied by 2.
3. **Diagonal**: The square root of the diagonal squared is calculated.
4. **Width (廣)**: Add the diagonal to the vertical length.
5. **Height (高)**: Add the diagonal to the horizontal length.
6. **Diagonal length in 丈 (袤)**: Add the horizontal and vertical lengths, then divide by 10 to convert from 尺 to 丈.

The variables `a`, `b`, and `c` will hold the width, height, and diagonal length of the door, respectively.
"""


"""
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
