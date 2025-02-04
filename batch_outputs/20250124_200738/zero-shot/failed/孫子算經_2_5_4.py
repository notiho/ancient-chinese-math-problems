"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

"""
To translate the ancient Chinese math problem into Python code, we will compute the value of the unknown `a` using the given rates and operations. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟數 = 21  # in 升
粺米率 = 27  # 粺米 per 粟
粟率 = 50  # 粟 per 升

# Calculation
實 = 粟數 * 粺米率  # Total 粺米 in 升
a = Fraction(實, 粟率)  # Convert to 斗 (1 斗 = 10 升)

# Result
a  # in 斗
#----- content ends here -----


"""


The variable `a` will hold the result in the unit of 斗.
"""


"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
