"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 糲飯 (coarse rice) obtained from 粟 (millet). The method described in the problem states: "三之，二而一," which means that for every 3 units of 粟, 2 units of 糲飯 are obtained.

Given:
- 粟 = 2斗3升
- 1斗 = 10升 (conversion factor)

We first convert everything to the same unit (升), perform the calculation, and then convert back to 斗 and 升.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given 粟 in 斗 and 升
粟_斗 = 2
粟_升 = 3

# Convert 粟 to total 升
total_粟_升 = 粟_斗 * 10 + 粟_升

# 糲飯 calculation: for every 3 units of 粟, 2 units of 糲飯 are obtained
total_糲飯_升 = total_粟_升 * Fraction(2, 3)

# Convert 糲飯 back to 斗 and 升
糲飯_斗 = total_糲飯_升 // 10  # Integer part is the number of 斗
糲飯_升 = total_糲飯_升 % 10   # Remainder is the number of 升

# Assign the result to variable 'a' in terms of 斗 and 升
a = (糲飯_斗, 糲飯_升)

# Output the result
a
#----- content ends here -----


"""


Explanation of the result:
- `a` will be a tuple representing the amount of 糲飯 in 斗 and 升.
"""


"""
Variable 'a' has wrong value. Expected: 69/20, Actual: (1, Fraction(16, 3))"""
