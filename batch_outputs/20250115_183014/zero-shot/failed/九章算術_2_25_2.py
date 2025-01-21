"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of 糲飯 (a) that can be made from 糲米 (6斗4升 and 3/5升). The rule provided is "五之，二而一," which means for every 5 parts of 糲米, 2 parts of 糲飯 are produced.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# 糲米 total amount in terms of 升
糲米 = 6 * 10 + 4 + Fraction(3, 5)  # 1斗 = 10升

# Conversion rule: for every 5 parts of 糲米, 2 parts of 糲飯 are produced
a = 糲米 * Fraction(2, 5)  # 糲飯 in terms of 升

# Convert 糲飯 back to 斗
a = a / 10  # 1斗 = 10升

# a now represents the amount of 糲飯 in 斗


"""


After running this code, the variable `a` will contain the amount of 糲飯 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 323/125"""
