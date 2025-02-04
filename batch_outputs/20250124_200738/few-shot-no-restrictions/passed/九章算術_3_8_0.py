"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked rice, and person C holds 3 sheng of roughly cooked rice.
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The procedure for reverse proportional distribution says: Arrange the rates (weights) and let them multiply. The moving rate becomes the rate of the stationary one.
The procedure says: Take the rates of millet as 50, roughly husked rice as 30, and roughly cooked rice as 75 as the rates, and reverse them. Add them together to form the divisor.
Multiply the total 9 sheng by the unreversed rates of each, forming the dividends.
Divide the dividends by the divisor to obtain the amount of 1 sheng for each.

Answer: Person A gets *a* sheng, person B gets *b* sheng, and person C gets *c* sheng.
"""

from fractions import Fraction

# Initial amounts held by A, B, and C
甲持粟 = 3
乙持糲米 = 3
丙持糲飯 = 3

# Rates for 粟 (millet), 糲米 (roughly husked rice), and 糲飯 (roughly cooked rice)
粟率 = 50
糲米率 = 30
糲飯率 = 75

# Reverse the rates (返衰)
粟返衰 = Fraction(1, 粟率)
糲米返衰 = Fraction(1, 糲米率)
糲飯返衰 = Fraction(1, 糲飯率)

# Add the reversed rates to form the divisor (法)
法 = 粟返衰 + 糲米返衰 + 糲飯返衰

# Total amount of grain (9 sheng)
總量 = 甲持粟 + 乙持糲米 + 丙持糲飯

# Multiply the total by the unreversed rates to form the dividends (實)
甲實 = 總量 * 粟返衰
乙實 = 總量 * 糲米返衰
丙實 = 總量 * 糲飯返衰

# Divide each dividend by the divisor to find the redistributed amounts
a = 甲實 / 法
b = 乙實 / 法
c = 丙實 / 法

# Output the results
a, b, c#----- content ends here -----

"""
"""
