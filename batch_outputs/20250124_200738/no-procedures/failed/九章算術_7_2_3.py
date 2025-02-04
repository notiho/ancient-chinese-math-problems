"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade (璡). If each person contributes half the amount, there is an excess of 4 units of money. 
If each person contributes half as much as before (a quarter of the total price), there is a shortfall of 3 units of money.
Question: how many people are there (*a*), and what is the price of the jade (*b*)?

Answer: *a* people, jade price *b*.
"""

# Let the number of people be `a` and the price of the jade be `b`
from fractions import Fraction

# Equation 1: (b / a) * 1/2 = b / (2a), and there is an excess of 4
# b / (2a) = b / a - 4

# Equation 2: (b / a) * 1/4 = b / (4a), and there is a shortfall of 3
#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
