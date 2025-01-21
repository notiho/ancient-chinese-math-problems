"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves a door with unknown height, width, and diagonal length. A pole is used to measure these dimensions, and the measurements are as follows:

- The horizontal measurement (橫) is 4 feet.
- The vertical measurement (從) is 2 feet.
- The diagonal measurement (邪) is exactly the length of the pole.

We are tasked to find the width (廣), height (高), and diagonal length (袤) of the door.

The method described in the problem involves:
1. Multiplying the horizontal and vertical measurements.
2. Doubling the product.
3. Taking the square root of the result to find the diagonal length.
4. Adding the vertical measurement to the diagonal to find the width.
5. Adding the horizontal measurement to the diagonal to find the height.
6. Adding the horizontal and vertical measurements to the diagonal to find the diagonal length in units of "丈" (10 feet).

Here is the Python code:


"""


from fractions import Fraction
import math

# Given measurements
horizontal = Fraction(4)  # 4 feet
vertical = Fraction(2)    # 2 feet

# Step 1: Multiply horizontal and vertical measurements
product = horizontal * vertical

# Step 2: Double the product
doubled_product = 2 * product

# Step 3: Take the square root of the doubled product
diagonal = Fraction(math.sqrt(doubled_product))

# Step 4: Add the vertical measurement to the diagonal to find the width
a = vertical + diagonal  # Width (廣)

# Step 5: Add the horizontal measurement to the diagonal to find the height
b = horizontal + diagonal  # Height (高)

# Step 6: Add the horizontal and vertical measurements to the diagonal to find the diagonal length in 丈
c = (horizontal + vertical + diagonal) / 10  # Diagonal length (袤) in 丈

# Results
a  # Width in feet
b  # Height in feet
c  # Diagonal length in 丈


"""


This code computes the values of `a`, `b`, and `c` as described in the problem. The results are stored in the variables `a`, `b`, and `c`.
"""


"""
"""
