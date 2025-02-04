"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a(=27/5)丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun less. It holds 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Place the volume of rice in cubic chi. Multiply it by 12. Let the height be the divisor. Take the square root of the result, and that is the circumference.

Answer: *a*(=27/5) zhang.
"""

from fractions import Fraction
import math

# 高一丈三尺三寸、少半寸
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

高 = 1 * 丈 + 3 * 尺 + 3 * 寸 - Fraction(1, 20)  # 高 = 1 丈 3 尺 3 寸 - 0.5 寸

# 容米二千斛
米積 = 2000 * 100  # 1 斛 = 100 立方尺

# 置米積尺，以十二乘之
積乘十二 = 米積 * 12

# 令高而一
積除高 = Fraction(積乘十二, 高)

# 所得，開方除之，即周
周 = Fraction(int(math.sqrt(積除高)), 1)  # 開方後取整數

a = Fraction(周, 10)  # 轉換為丈單位 (1 丈 = 10 尺)

# Answer: a = 27/5 丈#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/5, Actual: 85/2"""
