"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a(=27/10)升 。乙 b(=9/2)升 。丙 c(=9/5)升 。
"""

"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet rice.
It is desired to combine them and redistribute equally.
Question: how much does each person receive?

The reverse weighting procedure says: Place the weights in a line and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rice rate as 75 as the weights, and reverse the weights.
Add the auxiliary [weights] to obtain the divisor.
Multiply the total 9 sheng by the unreduced weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng.

Answer: A receives *a*(=27/10) sheng, B receives *b*(=9/2) sheng, and C receives *c*(=9/5) sheng.
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

# Reverse the weights
甲衰 = Fraction(1, 粟率)
乙衰 = Fraction(1, 糲米率)
丙衰 = Fraction(1, 糲飯率)

# Auxiliary addition for the divisor
法 = 甲衰 + 乙衰 + 丙衰

# Total combined amount
總量 = 甲持粟 + 乙持糲米 + 丙持糲飯

# Multiply total by unreduced weights to get dividends
甲實 = 總量 * 甲衰
乙實 = 總量 * 乙衰
丙實 = 總量 * 丙衰

# Divide dividends by the divisor to get the redistributed amounts
a = Fraction(甲實, 法)  # 27/10
b = Fraction(乙實, 法)  # 9/2
c = Fraction(丙實, 法)  # 9/5
"""
"""
