"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a乘 奇 b斛 。
"""

"""
Suppose there is rent grain totaling 98,762 hu. It is desired to load it using carts, with each cart carrying 50 hu.
Question: how many carts are needed?

The procedure says: Place the rent grain of 98,762 hu as the dividend.
Take the amount one cart can carry, 50 hu, as the divisor.
Divide the dividend by the divisor to obtain the number of carts.
If there is a remainder, it is the leftover hu.

Answer: *a* carts, with an excess of *b* hu.
"""

# 置租九萬八千七百六十二斛為實
實 = 98762

# 以一車所載五十斛為法
法 = 50

# 實如法，即得
a = 實 // 法  # Number of full carts
b = 實 % 法  # Leftover hu
"""
"""
