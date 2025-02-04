"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose person A holds 3 sheng of unhusked millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet (rice).
It is desired to combine and redistribute them equally. 
Question: how much does each person receive?

The reverse-weighting procedure says: Arrange the weights and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Take the rates of unhusked millet (50), roughly husked millet (30), and roughly cooked millet (75) as weights, and reverse-weight them. Add them together as the divisor. Multiply the total 9 sheng by the unreversed weights, each becoming its own dividend. Divide the dividends by the divisor to obtain the amount of 1 sheng.

Answer: Person A gets *a* sheng, person B gets *b* sheng, and person C gets *c* sheng.
"""

from fractions import Fraction

# Initial amounts held by A, B, and C
甲持粟 = 3  # sheng of unhusked millet
乙持糲米 = 3  # sheng of roughly husked millet
丙持糲飯 = 3  # sheng of roughly cooked millet

# Rates (weights) for each type of grain
粟率 = 50  # unhusked millet
糲米率 = 30  # roughly husked millet
糲飯率 = 75  # roughly cooked millet

# Total amount of grain
總量 = 甲持粟 + 乙持糲米 + 丙持糲飯  # 9 sheng

# Reverse weights (返衰)
甲衰 = 粟率
乙衰 = 糲米率
丙衰 = 糲飯率

# Add the reverse weights to get the divisor (法)
法 = 甲衰 + 乙衰 + 丙衰

# Calculate the dividends (實) for each person
甲實 = 總量 * 甲衰
乙實 = 總量 * 乙衰
丙實 = 總量 * 丙衰

# Divide each dividend by the divisor to get the redistributed amounts
a = Fraction(甲實, 法)  # Amount for person A
b = Fraction(乙實, 法)  # Amount for person B
c = Fraction(丙實, 法)  # Amount for person C

# Output the results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
