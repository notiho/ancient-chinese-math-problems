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

The reverse weighting procedure says: Place the weights in a line and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Use the rates of millet (50), roughly husked rice (30), and roughly cooked rice (75) as weights, and reverse the weights.
Add the reversed weights together to form the divisor.
Multiply the total 9 sheng by the unreversed weights for each person to form the dividends.
Divide the dividends by the divisor to obtain the amount of 1 sheng for each person.

Answer: A receives *a* sheng, B receives *b* sheng, and C receives *c* sheng.
"""

from fractions import Fraction

# 粟率、糲米率、糲飯率
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 甲、乙、丙各持 3 升
甲持 = 3
乙持 = 3
丙持 = 3

# 返衰之 (reverse the weights)
甲衰 = Fraction(1, 粟率)
乙衰 = Fraction(1, 糲米率)
丙衰 = Fraction(1, 糲飯率)

# 副并為法 (sum the reversed weights to form the divisor)
法 = 甲衰 + 乙衰 + 丙衰

# 以九升乘未并者各自為實 (multiply the total 9 sheng by the unreversed weights for each person)
總升 = 甲持 + 乙持 + 丙持
甲實 = 總升 * 粟率
乙實 = 總升 * 糲米率
丙實 = 總升 * 糲飯率

# 實如法得一升 (divide the dividends by the divisor)
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)

a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 6750
Variable 'b' has wrong value. Expected: 9/2, Actual: 4050
Variable 'c' has wrong value. Expected: 9/5, Actual: 10125"""
