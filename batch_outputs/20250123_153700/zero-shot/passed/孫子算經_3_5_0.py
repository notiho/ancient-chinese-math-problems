"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a乘 奇 b斛 。
"""

"""
To solve this problem, we need to calculate how many carts are required to transport 98,762 hu of grain, given that each cart can carry 50 hu. Let's write this in Python code:


"""


from fractions import Fraction

# Given values
total_grain = 98762  # in hu
grain_per_cart = 50  # in hu

# Calculate the number of carts needed
a = total_grain // grain_per_cart  # Integer part (full carts)
b = total_grain % grain_per_cart   # Remaining grain (in hu)

# Results
a  # Number of full carts
b  # Remaining grain in hu


"""


This code calculates the number of full carts (`a`) and the remaining grain (`b`) that cannot fill a full cart.
"""


"""
"""
