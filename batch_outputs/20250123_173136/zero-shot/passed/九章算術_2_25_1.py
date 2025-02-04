"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of 糲飯 (a) that can be made from the given amount of 糲米. The rule provided states: "五之，二而一," which means multiply by 5 and then divide by 2.

Here is the Python code:


"""


from fractions import Fraction

# Given 糲米
糲米 = Fraction(6, 1) + Fraction(4, 10) + Fraction(3, 50)  # 6斗4升3/5升

# Calculation for 糲飯
a = 糲米 * 5 / 2  # Multiply by 5 and divide by 2

# Result
a  # a斗


"""


The variable `a` will contain the amount of 糲飯 in terms of "斗".
"""


"""
"""
