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
2. Take half of the difference between the height and the width (6.8 chi), square it, double it, and subtract it from the product.
3. Halve the remainder.
4. Extract the square root of this value, and divide it by the square root of 2.
5. Subtract half of the difference (6.8 chi) to obtain the width.
6. Add half of the difference (6.8 chi) to obtain the height.

Answer: the width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
import math

# Given values
相多 = Fraction(6, 1) + Fraction(8, 10)  # 6 chi 8 cun = 6.8 chi
對角 = 10  # 1 zhang = 10 chi

# Step 1: Let the diagonal (1 zhang) be squared to obtain the product
實 = 對角 ** 2

# Step 2: Take half of the difference, square it, double it, and subtract it from the product
半相多 = 相多 / 2
減項 = 2 * (半相多 ** 2)
餘 = 實 - 減項

# Step 3: Halve the remainder
半餘 = 餘 / 2

# Step 4: Extract the square root of this value
開方 = math.sqrt(float(半餘))

# Step 5: Subtract half of the difference to obtain the width
廣 = 開方 - float(半相多)

# Step 6: Add half of the difference to obtain the height
高 = 開方 + float(半相多)

# Convert results to fractions for exact representation
a = Fraction(廣).limit_denominator(100)  # Width
b = Fraction(高).limit_denominator(100)  # Height

# Final results
a, b  # Width (廣) and Height (高) in chi#----- content ends here -----

"""
"""
