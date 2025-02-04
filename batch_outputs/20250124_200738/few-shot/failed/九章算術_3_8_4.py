"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The reverse-weighting procedure says: Arrange the weights and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rate as 75 as weights, and reverse-weight them.
Add the auxiliary weights together to form the divisor.
Multiply the total 9 sheng by the unreversed weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng for each person.

Answer: Person A gets *a* sheng, person B gets *b* sheng, and person C gets *c* sheng.
"""

from fractions import Fraction

# Initial quantities
甲粟 = 3  # 3 sheng of millet
乙糲米 = 3  # 3 sheng of roughly husked millet
丙糲飯 = 3  # 3 sheng of roughly cooked millet

# Rates (weights)
粟率 = 50
糲米率 = 30
糲飯率 = 75

# Reverse weights (衰)
甲衰 = 粟率
乙衰 = 糲米率
丙衰 = 糲飯率

# Auxiliary weights summed to form the divisor (法)
法 = 甲衰 + 乙衰 + 丙衰

# Total quantity (9 sheng) multiplied by unreversed weights to form dividends (實)
總量 = 甲粟 + 乙糲米 + 丙糲飯
甲實 = 總量 * 甲衰
乙實 = 總量 * 乙衰
丙實 = 總量 * 丙衰

# Divide each dividend by the divisor to get the result
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
