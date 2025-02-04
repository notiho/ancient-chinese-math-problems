"""
今有甲持粟三升乙持糲米三升丙持糲飯三升欲令合而分之問各幾何
返衰術曰列置衰而令相乘動者為不動者衰術曰以粟率五十糲米率三十糲飯率七十五為衰而返衰之副并為法以九升乘未并者各自為實實如法得一升
荅曰甲 a升 乙 b升 丙 c升 
"""

#----- content starts here -----
"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The procedure for reverse weighting says: Place the weights in a line and let them multiply each other. The moving [quantity] becomes the non-moving [quantity].
The procedure for weighting says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rate as 75 as the weights.
Reverse the weights, and in auxiliary, add them to obtain the divisor.
Multiply the total 9 sheng by the unadded [weights], and each becomes its own dividend.
Do the division, obtaining the amount of one sheng.

The answer says: A receives *a* sheng, B receives *b* sheng, and C receives *c* sheng.
"""

# 粟率五十，糲米率三十，糲飯率七十五
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 列置衰
衰 = [粟率, 糲米率, 糲飯率]

# 返衰之副并為法
法 = sum(衰)

# 以九升乘未并者
總量 = 9
實 = [總量 * 粟率, 總量 * 糲米率, 総量 * 糲飯率]

# 各自為實，實如法得一升
a, b, c = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
Code error: name '総量' is not defined"""
