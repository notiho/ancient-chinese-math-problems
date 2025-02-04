"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a(=1975)乘 奇 b(=12)斛 。
"""

"""
Suppose there is rent of 98,762 hu, and it is desired to load 50 hu per cart.
Question: how many carts are needed?

The procedure says: Place the rent of 98,762 hu as the dividend.
Take the amount a single cart can carry, 50 hu, as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a*(=1975) full carts, with a remainder of *b*(=12) hu.
"""

# 置租九萬八千七百六十二斛為實
租 = 98762

# 以一車所載五十斛為法
車載量 = 50

# 實如法，即得
a = 租 // 車載量  # 1975 full carts
b = 租 % 車載量   # 12 hu remaining
"""
"""
