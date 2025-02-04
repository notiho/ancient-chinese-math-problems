"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of 糲飯 (a) that can be made from the given amount of 糲米. The problem states that the conversion is based on the rule "五之，二而一," which means that for every 5 units of 糲米, 2 units of 糲飯 are produced.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given 糲米
糲米 = Fraction(6, 1) + Fraction(4, 10) + Fraction(3, 50)  # 6斗4升3/5升

# Conversion rule: 5 units of 糲米 produce 2 units of 糲飯
a = 糲米 * Fraction(2, 5)  # Multiply by the conversion ratio

# The result is stored in variable 'a'


"""


The variable `a` will contain the amount of 糲飯 in units of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 323/125"""
