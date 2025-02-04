"""
今有租，九萬八千七百六十二斛，欲以一車載五十斛。問：用車幾何？
術曰：置租九萬八千七百六十二斛為實，以一車所載五十斛為法。實如法，即得。
答曰： a乘 奇 b斛 。
"""

"""
To solve this problem, we need to determine how many carts are required to carry a total of 98,762斛 (units of grain), where each cart can carry 50斛. The solution involves dividing the total amount of grain by the capacity of one cart.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Total grain (in 斛)
total_grain = 98762

# Capacity of one cart (in 斛)
cart_capacity = 50

# Number of carts needed
a = total_grain // cart_capacity  # Integer part (whole carts)
b = total_grain % cart_capacity   # Remaining grain (in 斛)

# Results
a = Fraction(a)  # Number of full carts
b = Fraction(b)  # Remaining grain
#----- content ends here -----


"""


The solution is:
- `a` represents the number of full carts required.
- `b` represents the remaining grain in 斛 that cannot fit into a full cart.
"""


"""
"""
