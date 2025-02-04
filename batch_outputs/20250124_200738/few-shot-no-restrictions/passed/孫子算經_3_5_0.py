"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a乘 奇 b斛 。
"""

#----- content starts here -----
"""
Suppose there is rent of 98,762 hu. It is desired to load it using carts, with each cart carrying 50 hu.
Question: how many carts are needed?

The procedure says: Place the rent of 98,762 hu as the dividend.
Take the amount each cart can carry, 50 hu, as the divisor.
Perform the division to obtain the number of carts and the remainder.

Answer: *a* full carts and *b* hu remaining.
"""

from fractions import Fraction

# 租九萬八千七百六十二斛
租 = 98762

# 一車所載五十斛
車載量 = 50

# 實如法，即得
a = 租 // 車載量  # Full carts
b = 租 % 車載量  # Remaining hu

# Output
a, b#----- content ends here -----

"""
"""
