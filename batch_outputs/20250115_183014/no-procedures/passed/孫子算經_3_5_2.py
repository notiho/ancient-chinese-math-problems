"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
答曰： a乘 奇 b斛 。
"""

"""
Suppose there is rent grain totaling 98,762 hu. Each cart can carry 50 hu.
Question: how many carts are needed, and how much grain is left over?

Answer: *a* full carts and *b* hu of leftover grain.
"""

# Total grain in hu
total_grain = 98762

# Grain carried per cart in hu
grain_per_cart = 50

# Calculate the number of full carts
a = total_grain // grain_per_cart

# Calculate the leftover grain
b = total_grain % grain_per_cart
"""
"""
