"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the hypotenuse (弦) of a right triangle given the lengths of the two legs (句 and 股). The problem states that the lengths of the legs are 8 steps (句 = 8) and 15 steps (股 = 15). The hypotenuse is calculated using the Pythagorean theorem.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句 = Fraction(8)  # 8 steps
股 = Fraction(15)  # 15 steps

# Pythagorean theorem to find the hypotenuse (弦)
a = (句**2 + 股**2)**0.5  # Hypotenuse in steps

# Result
a  # Hypotenuse in steps
#----- content ends here -----


"""


The variable `a` will hold the value of the hypotenuse in steps.
"""


"""
Variable 'a' has wrong value. Expected: 6, Actual: 17.0"""
