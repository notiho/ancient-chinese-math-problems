"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade (璡). If each person contributes half of the required amount, there is an excess of 4 units. If each person contributes half less than the required amount, there is a shortage of 3 units.
Question: What is the number of people and the price of the jade?

Answer: *a* people, and the price of the jade is *b*.
"""

# Let the number of people be x and the price of the jade be y
# Each person contributes y / x

from fractions import Fraction

# Equation 1: If each person contributes half, there is an excess of 4
# (y / x) * 0.5 * x = y + 4
# y / 2 = y + 4
# Equation 2: If each person contributes half less, there is a shortage of 3
#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
