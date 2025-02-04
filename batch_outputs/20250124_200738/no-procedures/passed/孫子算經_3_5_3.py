"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
答曰： a乘 奇 b斛 。
"""

#----- content starts here -----
"""
Suppose there is rent grain totaling 98,762 hu. It is desired to load 50 hu per cart.
Question: how many carts are needed, and how much grain is left over?

Answer: *a* full carts and *b* hu of leftover grain.
"""

from fractions import Fraction

# Total grain in hu
total_grain = 98762

# Grain per cart in hu
grain_per_cart = 50

# Calculate the number of full carts
a = total_grain // grain_per_cart

# Calculate the leftover grain
b = total_grain % grain_per_cart

# Results
a, b#----- content ends here -----

"""
"""
