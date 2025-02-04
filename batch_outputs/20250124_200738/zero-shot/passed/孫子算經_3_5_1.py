"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a乘 奇 b斛 。
"""

"""
To solve this problem, we need to determine how many carts are required to carry a total of 98,762 hu of grain if each cart can carry 50 hu. Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_grain = 98762  # in hu
grain_per_cart = 50  # in hu

# Compute the number of carts needed
a = total_grain // grain_per_cart  # Integer part (whole carts)
b = total_grain % grain_per_cart  # Remaining grain (in hu)

# Output variables
a  # Number of full carts
b  # Remaining grain in hu
#----- content ends here -----


"""


The solution is:
- `a` represents the number of full carts needed.
- `b` represents the remaining grain in hu that cannot fit into a full cart.
"""


"""
"""
