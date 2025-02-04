"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a步 。
"""

"""
This problem involves a right triangle where the lengths of the two legs (句 and 股) are given, and we are tasked to find the area of the square (方) formed by the shorter leg (句). Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句 = 5  # in steps
股 = 12  # in steps

# Compute the area of the square formed by 句
a = Fraction(句 * 句)  # Area of the square (方)

# The result
a  # in steps²
#----- content ends here -----


"""


The variable `a` will hold the value of the area of the square in terms of steps².
"""


"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 25"""
