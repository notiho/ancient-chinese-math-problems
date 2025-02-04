"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 糲飯 (coarse rice) that can be made from 2斗3升 of 粟 (millet). The rule provided states: "三之，二而一," which means for every 3 parts of 粟, 2 parts of 糲飯 are obtained.

### Step-by-step solution:
1. Convert 2斗3升 into a single unit. Since 1斗 = 10升, 2斗3升 = \( 2 \times 10 + 3 = 23 \) 升.
2. Apply the ratio: For every 3 parts of 粟, 2 parts of 糲飯 are obtained. This means the amount of 糲飯 is \( \frac{2}{3} \) of the amount of 粟.
3. Compute \( \frac{2}{3} \times 23 \).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given
粟 = Fraction(23)  # 2斗3升 = 23升

# Ratio of 粟 to 糲飯
ratio = Fraction(2, 3)

# Compute 糲飯
a = 粟 * ratio  # a is the amount of 糲飯 in 升

# Result
a  # a斗 (in 升)
#----- content ends here -----


"""


The result `a` will be in terms of 升. If needed, you can convert it back to 斗 and 升 by dividing by 10 (1斗 = 10升).
"""


"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 46/3"""
