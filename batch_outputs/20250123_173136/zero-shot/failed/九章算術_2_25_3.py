"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a given amount of 糲米 (coarse rice) into 糲飯 (cooked coarse rice). The rule provided is "五之，二而一," which means for every 5 parts of rice, you get 2 parts of cooked rice.

The given amount of 糲米 is 6斗4升 and 3/5升. We will calculate the amount of 糲飯 (cooked coarse rice) using the rule.

Here is the Python code:


"""


from fractions import Fraction

# Given 糲米
rice = 6 + Fraction(4, 10) + Fraction(3, 5)  # 6斗4升3/5升 (1斗 = 10升)

# Rule: For every 5 parts of rice, you get 2 parts of 糲飯
a = rice * Fraction(2, 5)  # 糲飯 in 斗

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the amount of 糲飯 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 14/5"""
