"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a door (戶) with unknown height (高), width (廣), and diagonal (袤). A pole (竿) is used to measure the door, and the measurements are as follows:

- The pole laid horizontally across the door does not exceed 4 feet (橫不出 = 4 feet).
- The pole laid vertically across the door does not exceed 2 feet (從不出 = 2 feet).
- The pole laid diagonally across the door exactly fits the diagonal of the door (邪之適出).

The solution involves the following steps:
1. Multiply the horizontal (橫不出) and vertical (從不出) measurements.
2. Double the product.
3. Take the square root of the result and divide it by the vertical measurement to get the width (廣).
4. Add the vertical measurement to the result to get the height (高).
5. Add the horizontal and vertical measurements to get the diagonal (袤).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
horizontal = Fraction(4)  # 橫不出 = 4 feet
vertical = Fraction(2)    # 從不出 = 2 feet

# Calculations
a = Fraction(math.sqrt(2 * horizontal * vertical)) / vertical  # 廣 (width)
b = a + vertical  # 高 (height)
c = horizontal + vertical  # 袤 (diagonal in feet)

# Convert diagonal to 丈 (1 丈 = 10 feet)
c = c / 10

# Results
a  # 廣 (width) in feet
b  # 高 (height) in feet
c  # 袤 (diagonal) in 丈
#----- content ends here -----


"""


The variables `a`, `b`, and `c` represent the width, height, and diagonal of the door, respectively. The diagonal is converted to 丈 as required.
"""


"""
Variable 'a' has wrong value. Expected: 6, Actual: 2
Variable 'b' has wrong value. Expected: 8, Actual: 4
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
