"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet.
It is desired to combine them and redistribute equally.
Question: how much does each person receive?

The reverse-weighting procedure says: Arrange the weights and let them multiply each other. The moving one becomes the weight of the unmoving one.
The procedure says: Use the millet rate of 50, the roughly husked millet rate of 30, and the roughly cooked millet rate of 75 as the weights, and reverse-weight them.
Add the auxiliary weights together to form the divisor.
Multiply 9 sheng by the uncombined weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng.

Answer: A receives *a* sheng, B receives *b* sheng, and C receives *c* sheng.
"""

from fractions import Fraction

# Initial holdings
甲持粟 = 3
乙持糲米 = 3
丙持糲飯 = 3

# Rates for 粟, 糲米, and 糲飯
粟率 = 50
糲米率 = 30
糲飯率 = 75

# Reverse-weighting: Multiply each holding by its rate
甲實 = 甲持粟 * 粟率
乙實 = 乙持糲米 * 糲米率
丙實 = 丙持糲飯 * 糲飯率

# Combine the weights to form the divisor
法 = 粟率 + 糲米率 + 糲飯率

# Total combined volume (9 sheng)
總量 = 甲持粟 + 乙持糲米 + 丙持糲飯

# Multiply total volume by uncombined weights
甲分 = Fraction(總量 * 粟率, 法)
乙分 = Fraction(總量 * 糲米率, 法)
丙分 = Fraction(總量 * 糲飯率, 法)

# Results
a = 甲分
b = 乙分
c = 丙分
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
