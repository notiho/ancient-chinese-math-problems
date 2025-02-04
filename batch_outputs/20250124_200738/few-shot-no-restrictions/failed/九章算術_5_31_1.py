"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall. 
The base perimeter is 8 chi, and the height is 5 chi.
Question: What is the volume of the pile, and how many hu of rice does it make?

The procedure for piled grain says: 
- Square the base perimeter, multiply it by the height, and divide by 36 if it is a free-standing pile.
- If it leans against a wall, divide by 18.
- If it leans against the inner corner of a wall, divide by 9.

For rice:
- 1 hu of rice occupies a volume of 1 chi 6 cun and 1/5 cun (or 1.65 chi³).

For reference:
- 1 hu of millet occupies a volume of 2 chi 7 cun (or 2.7 chi³).
- 1 hu of beans, peas, sesame, or wheat occupies a volume of 2 chi 4 cun and 3/10 cun (or 2.43 chi³).

Answer: The volume is *a* chi³. It makes *b* hu of rice, with a remainder of *c* hu.
"""

from fractions import Fraction

# Given dimensions
下周 = 8  # chi
高 = 5  # chi

# Procedure for volume
# 下周自乘，以高乘之，九而一
積 = (下周 ** 2) * 高 / 9

# Conversion for rice
# 米一斛，積一尺六寸、五分寸之一 (1 hu = 1.65 chi³)
米一斛積 = Fraction(165, 100)  # 1.65 chi³

# Calculate the number of hu of rice
米斛數 = 積 / 米一斛積

# Separate into whole hu and remainder
b = int(米斛數)  # Whole hu
c = 米斛數 - b  # Remainder in fractional hu

# Final results
a = 積  # Total volume in chi³

# Output results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320/9, Actual: 35.55555555555556
Variable 'c' has wrong value. Expected: 691/729, Actual: 0.5488215488215502"""
