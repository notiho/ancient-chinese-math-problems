"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally. 
Question: how much does each person receive?

The reverse weighting procedure says: Arrange the weights and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Use the millet rate of 50, the roughly husked millet rate of 30, and the roughly cooked millet rate of 75 as the weights, and reverse the weights.
Add the auxiliary weights to form the divisor.
Multiply 9 sheng by the uncombined weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng.

The answer says: A receives *a* sheng, B receives *b* sheng, and C receives *c* sheng.
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

# Reverse the weights (返衰)
甲衰 = Fraction(1, 粟率)
乙衰 = Fraction(1, 糲米率)
丙衰 = Fraction(1, 糲飯率)

# Combine the reversed weights to form the divisor (副并為法)
法 = 甲衰 + 乙衰 + 丙衰

# Total combined amount (9升)
總量 = 甲持粟 + 乙持糲米 + 丙持糲飯

# Multiply the total amount by the reversed weights to form the dividends (以九升乘未并者各自為實)
甲實 = 總量 * 甲衰
乙實 = 總量 * 乙衰
丙實 = 總量 * 丙衰

# Divide the dividends by the divisor to get the final amounts (實如法得一升)
a = 甲實 / 法
b = 乙實 / 法
c = 丙實 / 法
"""
"""
