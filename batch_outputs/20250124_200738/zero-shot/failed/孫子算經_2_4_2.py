"""
今有粟一斗。問：為糲米幾何？
術曰：置粟一斗十升，以糲米率三十乘之，得三百升為實，以粟率五十為法，除之，即得。
答曰： a升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟_rate = Fraction(50)  # 粟 rate (法)
糲米_rate = Fraction(30)  # 糲米 rate
粟_quantity = Fraction(1, 1) + Fraction(10, 10)  # 粟 quantity (1斗10升 = 1.1斗)

# Calculation
實 = 粟_quantity * 糲米_rate  # 實 = 粟 quantity * 糲米 rate
a = 實 / 粟_rate  # a = 實 / 粟 rate

# Answer
a  # in 升
#----- content ends here -----


"""


The variable `a` will contain the result in 升 (liters).
"""


"""
Variable 'a' has wrong value. Expected: 6, Actual: 6/5"""
