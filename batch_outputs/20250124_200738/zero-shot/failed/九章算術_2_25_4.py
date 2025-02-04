"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 6斗4升 and 3/5升 of 糲米 (coarse rice), and we want to calculate how much 糲飯 (coarse rice meal) can be made. The rule provided is "五之，二而一," which means the amount of 糲飯 is 2/5 of the amount of 糲米.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 糲米 amount in terms of 斗 and 升
斗_to_升 = 10  # 1斗 = 10升
糲米 = 6 * 斗_to_升 + 4 + Fraction(3, 5)  # Convert everything to 升

# Rule: 糲飯 is 2/5 of 糲米
糲飯 = 糲米 * Fraction(2, 5)

# Convert 糲飯 back to 斗
a = 糲飯 / 斗_to_升  # Convert 升 to 斗

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the amount of 糲飯 in terms of 斗.
"""


"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 323/125"""
