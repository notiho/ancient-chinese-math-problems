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
Divide the dividend by the divisor, and the result is obtained.

Answer: *a*(=1975) full carts and *b*(=12) hu remaining.
"""

# 置租九萬八千七百六十二斛為實
實 = 98762

# 以一車所載五十斛為法
法 = 50

# 實如法，即得
a = 實 // 法  # 1975 full carts
b = 實 % 法   # 12 hu remaining
"""
"""
