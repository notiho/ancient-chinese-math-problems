"""
今有粟二斗一升。問：為粺米幾何？
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much husked millet does it make?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟 = 2 + Fraction(1, 10)  # 1 dou = 10 sheng, so 1 sheng = 1/10 dou

# Multiply by 3 and divide by 5 to get husked millet
a = Fraction(3 * 粟, 5)

# Convert result into dou and sheng
dou = a.numerator // a.denominator  # Whole dou
sheng = (a.numerator % a.denominator) * 10 // a.denominator  # Remaining sheng (1 dou = 10 sheng)

# Final result
result = f"{dou} dou and {sheng} sheng"
result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 63/50"""
