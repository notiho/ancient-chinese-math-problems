"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a乘 奇 b斛 。
"""

#----- content starts here -----
"""
Suppose there is rent grain totaling 98,762 hu. It is desired to load it using carts, each carrying 50 hu.
Question: how many carts are needed, and how much grain remains?

The procedure says: Place the rent grain, 98,762 hu, as the dividend.
Take the amount a single cart can carry, 50 hu, as the divisor.
Divide the dividend by the divisor to obtain the number of carts.
The remainder is the leftover grain.

Answer: *a* carts and *b* hu of leftover grain.
"""

from fractions import Fraction

# 租九萬八千七百六十二斛
租 = 98762

# 一車所載五十斛
車載量 = 50

# 實如法，即得
a = 租 // 車載量  # Number of full carts
b = 租 % 車載量   # Remaining grain in hu

# Output: a carts and b hu
a, b#----- content ends here -----

"""
"""
