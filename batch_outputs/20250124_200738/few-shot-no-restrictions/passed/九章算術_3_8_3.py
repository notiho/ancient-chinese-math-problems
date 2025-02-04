"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose Person A holds 3 sheng of millet, Person B holds 3 sheng of roughly husked millet, and Person C holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The procedure for reverse weighting says: Arrange the weights and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Use the rates for millet (50), roughly husked millet (30), and roughly cooked millet (75) as the weights, and reverse the weights.
Add the auxiliary weights to form the divisor.
Multiply the total 9 sheng by the unreduced weights, forming the dividends.
Divide the dividends by the divisor to obtain the amount for one sheng.

Answer: Person A gets *a* sheng, Person B gets *b* sheng, and Person C gets *c* sheng.
"""

from fractions import Fraction

# Initial quantities
甲持粟 = 3  # Millet (sheng)
乙持糲米 = 3  # Roughly husked millet (sheng)
丙持糲飯 = 3  # Roughly cooked millet (sheng)

# Rates (weights)
粟率 = 50
糲米率 = 30
糲飯率 = 75

# Reverse weights (衰)
甲衰 = Fraction(1, 粟率)
乙衰 = Fraction(1, 糲米率)
丙衰 = Fraction(1, 糲飯率)

# Combine weights to form the divisor (法)
法 = 甲衰 + 乙衰 + 丙衰

# Total quantity
總量 = 甲持粟 + 乙持糲米 + 丙持糲飯  # 9 sheng

# Calculate the dividends (實)
甲實 = 總量 * 甲衰
乙實 = 總量 * 乙衰
丙實 = 總量 * 丙衰

# Divide by the divisor to get the final amounts
a = 甲實 / 法
b = 乙實 / 法
c = 丙實 / 法

# Output the results
a, b, c#----- content ends here -----

"""
"""
