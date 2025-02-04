"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a(=1975)乘 奇 b(=12)斛 。
"""

"""
Suppose there is rent of 98,762 hu, and it is desired to load 50 hu per cart.
Question: how many carts are needed?

The procedure says: Place the rent of 98,762 hu as the dividend.
Take the amount one cart can carry, 50 hu, as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a*(=1975) full carts and *b*(=12) hu remaining.
"""

from fractions import Fraction

# 置租九萬八千七百六十二斛為實
租 = 98762

# 以一車所載五十斛為法
車載量 = 50

# 實如法，即得
總車數 = Fraction(租, 車載量)

# 分解為整車數與剩餘斛數
a = 總車數.numerator // 總車數.denominator  # 1975 (整車數)
b = 總車數.numerator % 總車數.denominator  # 12 (剩餘斛數)
"""
Variable 'b' has wrong value. Expected: 12, Actual: 6"""
