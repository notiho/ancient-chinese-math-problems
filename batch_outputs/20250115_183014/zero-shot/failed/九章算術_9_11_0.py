"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a door (戶) with unknown height (高), width (廣), and diagonal length (袤). A pole (竿) is used to measure the door, and the measurements are given as follows:

- The horizontal length (橫) is 4 feet (4尺).
- The vertical length (從) is 2 feet (2尺).
- The diagonal length (邪) is the hypotenuse of the right triangle formed by the horizontal and vertical lengths.

The solution involves calculating the width (廣), height (高), and diagonal length (袤) using the given formula.

Here is the Python code:


"""


from fractions import Fraction
import math

# Given values
horizontal = Fraction(4)  # 橫不出 (4尺)
vertical = Fraction(2)    # 從不出 (2尺)

# Calculate the width (廣, a)
a = math.sqrt((horizontal * vertical) * 2) - vertical

# Calculate the height (高, b)
b = math.sqrt((horizontal * vertical) * 2) - horizontal

# Calculate the diagonal length (袤, c)
c = (horizontal + vertical) / 10  # Convert to 丈 (1丈 = 10尺)

# Convert results to Fraction for exact representation
a = Fraction(a).limit_denominator()
b = Fraction(b).limit_denominator()
c = Fraction(c).limit_denominator()

# Results
a  # Width (廣) in 尺
b  # Height (高) in 尺
c  # Diagonal length (袤) in 丈


"""


This code calculates the width (`a`), height (`b`), and diagonal length (`c`) of the door using the given measurements and formulas. The results are stored in variables `a`, `b`, and `c`, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 6, Actual: 2
Variable 'b' has wrong value. Expected: 8, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
