"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). 
The diagonal distance between the two opposite corners is exactly 1 zhang (10 chi).
Question: what are the height and width of the door?

The procedure says: 
1. Let the diagonal (1 zhang) be squared to obtain the product.
2. Take half of the difference between the height and width (6.8 chi), square it, double it, and subtract it from the product.
3. Halve the remainder.
4. Extract the square root of the result and divide it.
5. Subtract half of the difference to get the width of the door.
6. Add half of the difference to get the height of the door.

Answer: the width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
import math

# Given values
diagonal = 10  # 1 zhang = 10 chi
difference = Fraction(6, 1) + Fraction(8, 10)  # 6 chi 8 cun = 6.8 chi

# Step 1: Let the diagonal be squared to obtain the product
diagonal_squared = diagonal ** 2

# Step 2: Take half of the difference, square it, double it, and subtract it from the product
half_difference = difference / 2
adjustment = 2 * (half_difference ** 2)
remainder = diagonal_squared - adjustment

# Step 3: Halve the remainder
half_remainder = remainder / 2

# Step 4: Extract the square root of the result
width_base = math.sqrt(float(half_remainder))

# Step 5: Subtract half of the difference to get the width
width = width_base - float(half_difference)

# Step 6: Add half of the difference to get the height
height = width_base + float(half_difference)

# Convert to fractions for exact representation
a = Fraction(width).limit_denominator(100)  # Width
b = Fraction(height).limit_denominator(100)  # Height

# Output
a, b  # Width (a chi) and Height (b chi)#----- content ends here -----

"""
"""
