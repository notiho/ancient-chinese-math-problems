"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose Person A holds 3 sheng of millet, Person B holds 3 sheng of roughly husked millet, and Person C holds 3 sheng of roughly cooked millet (rice).
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The procedure for "inverse weighting" says: Place the weights (rates) in a line and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rate as 75 as the weights, and invert the weights. Add them together as the divisor.
Multiply the total 9 sheng by the uninverted weights, each becoming the dividend.
Divide the dividends by the divisor to obtain the amount for each person.

Answer: Person A receives *a* sheng, Person B receives *b* sheng, and Person C receives *c* sheng.
"""

from fractions import Fraction

# 粟、糲米、糲飯各持三升
甲持粟 = 3
乙持糲米 = 3
丙持糲飯 = 3

# 粟率五十、糲米率三十、糲飯率七十五
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 返衰之 (invert the weights)
粟返衰 = Fraction(1, 粟率)
糲米返衰 = Fraction(1, 糲米率)
糲飯返衰 = Fraction(1, 糲飯率)

# 副并為法 (sum the inverted weights to form the divisor)
法 = 粟返衰 + 糲米返衰 + 糲飯返衰

# 以九升乘未并者各自為實 (multiply the total 9 sheng by the uninverted weights)
總升 = 甲持粟 + 乙持糲米 + 丙持糲飯
甲實 = 粟率 * 總升
乙實 = 糲米率 * 總升
丙實 = 糲飯率 * 總升

# 實如法得一升 (divide the dividends by the divisor)
a = Fraction(甲實, 法.denominator * 法.numerator)
b = Fraction(乙實, 法.denominator * 法.numerator)
c = Fraction(丙實, 法.denominator * 法.numerator)

a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 30
Variable 'b' has wrong value. Expected: 9/2, Actual: 18
Variable 'c' has wrong value. Expected: 9/5, Actual: 45"""
