"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 2斗3升 of 粟 (grain) and want to calculate how much 糲飯 (coarse rice) can be made. The method described is to multiply the amount of 粟 by 2/3.

Here is the Python code:


"""


from fractions import Fraction

# Given amount of 粟
粟 = Fraction(2, 1) + Fraction(3, 10)  # 2斗3升 (1斗 = 10升)

# Calculation for 糲飯
a = 粟 * Fraction(2, 3)  # Multiply by 2/3

# Result
a  # a斗


"""


The variable `a` will contain the amount of 糲飯 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 23/15"""
