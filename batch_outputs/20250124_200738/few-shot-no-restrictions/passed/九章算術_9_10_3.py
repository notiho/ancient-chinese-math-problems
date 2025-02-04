"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). 
The diagonal distance between the two opposite corners of the door is exactly 1 zhang (10 chi). 
Question: What are the height and width of the door?

The procedure says: Let 1 zhang (10 chi) be squared to obtain the product. 
Take half of the difference between the height and width, square it, double it, and subtract it from the product. 
Take half of the remainder. Extract the square root of this value and divide it. 
The result, subtracting half of the difference, is the width of the door. 
Adding half of the difference gives the height of the door.

Answer: The width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
import math

# Given values
diagonal = 10  # 1 zhang = 10 chi
difference = Fraction(6, 1) + Fraction(8, 10)  # 6 chi 8 cun = 6.8 chi

# Step 1: Square the diagonal
diagonal_squared = diagonal ** 2

# Step 2: Take half of the difference, square it, and double it
half_difference = difference / 2
adjustment = 2 * (half_difference ** 2)

# Step 3: Subtract the adjustment from the squared diagonal
remainder = diagonal_squared - adjustment

# Step 4: Take half of the remainder
half_remainder = remainder / 2

# Step 5: Extract the square root of the half remainder
width_component = math.sqrt(float(half_remainder))

# Step 6: Calculate the width and height
width = width_component - half_difference
height = width_component + half_difference

# Final results
a = Fraction(width).limit_denominator(100)  # Width in chi
b = Fraction(height).limit_denominator(100)  # Height in chi

# Output
a, b#----- content ends here -----

"""
"""
