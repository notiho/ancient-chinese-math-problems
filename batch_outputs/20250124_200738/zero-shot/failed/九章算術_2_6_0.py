"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 糲飯 (coarse rice) that can be made from 2斗3升 of 粟 (millet). The method described in the problem states: "三之，二而一," which means that for every 3 parts of 粟, 2 parts of 糲飯 are obtained.

### Steps:
1. Convert the given amount of 粟 into a single unit (e.g., 升).
   - 1斗 = 10升, so 2斗3升 = 2 * 10 + 3 = 23升.
2. Use the ratio 3:2 (粟:糲飯) to calculate the amount of 糲飯.
   - For every 3升 of 粟, 2升 of 糲飯 is produced.
   - The formula is: 糲飯 = (2/3) * 粟.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given 粟
粟 = 2 * 10 + 3  # Convert 2斗3升 to 升

# Ratio of 粟 to 糲飯
ratio = Fraction(2, 3)

# Calculate 糲飯
a = ratio * 粟  # 糲飯 in 升

# Convert back to 斗 and 升 if needed
斗 = a // 10  # Whole number of 斗
升 = a % 10   # Remaining 升
#----- content ends here -----


"""


### Final Answer:
The variable `a` contains the amount of 糲飯 in 升. If you need it in 斗 and 升, you can use the `斗` and `升` variables.
"""


"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 46/3"""
