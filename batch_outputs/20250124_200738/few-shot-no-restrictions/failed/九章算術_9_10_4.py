"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). 
The diagonal distance between the two corners of the door is exactly 1 zhang (10 chi).
Question: What are the height and width of the door?

The procedure says:
1. Let the diagonal (1 zhang) be squared to obtain the product.
2. Take half of the difference between the height and width (6 chi 8 cun), square it, double it, and subtract it from the product. Then halve the remainder.
3. Extract the square root of the result and divide it. Subtract half of the difference to get the width of the door.
4. Add half of the difference to get the height of the door.

Answer: The width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
from math import sqrt

# Given values
diagonal = 10  # 1 zhang = 10 chi
difference = 6 + Fraction(8, 10)  # 6 chi 8 cun = 6.8 chi

# Step 1: Square the diagonal
diagonal_squared = diagonal ** 2

# Step 2: Half the difference, square it, double it, and subtract from the diagonal squared
half_difference = difference / 2
adjustment = 2 * (half_difference ** 2)
remainder = diagonal_squared - adjustment
half_remainder = remainder / 2

# Step 3: Extract the square root and subtract half the difference to get the width
width = sqrt(half_remainder) - half_difference

# Step 4: Add half the difference to get the height
height = width + difference

# Final results
a = round(width, 2)  # Width in chi
b = round(height, 2)  # Height in chi

# Output
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 2.8
Variable 'b' has wrong value. Expected: 48/5, Actual: 9.6"""
