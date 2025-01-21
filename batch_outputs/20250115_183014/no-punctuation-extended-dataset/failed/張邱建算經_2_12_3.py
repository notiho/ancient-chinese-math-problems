"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 c 大上下戸戸出絹 d疋 中上戸戸出絹 e疋 中中戸戸出絹 f疋 中下戸戸出絹 g疋 下上戸戸出絹 h疋 下中戸戸出絹 i疋 下下戸戸出絹 j疋
"""

"""
Suppose there is a tax rate of 3 bolts of silk per household, adjusted according to wealth into nine ranks. Each household differs by 2 zhang (units of silk). 
There are 39 households in the highest rank (上上), 24 in the second rank (上中), 57 in the third rank (上下), 31 in the fourth rank (中上), 78 in the fifth rank (中中), 43 in the sixth rank (中下), 25 in the seventh rank (下上), 76 in the eighth rank (下中), and 13 in the lowest rank (下下). 
Question: How much silk should each household in the nine ranks contribute?

The procedure says: Assign the differences in contribution for each rank. 
The 上上 households contribute 16, 上中 households contribute 14, 上下 households contribute 12, 中上 households contribute 10, 中中 households contribute 8, 中下 households contribute 6, 下上 households contribute 4, 下中 households contribute 2, and 下下 households contribute 0. 
Multiply the number of households in each rank by their respective contribution and sum these products to find the total contribution. 
Divide the total contribution by the total number of households to find the base contribution for each household. 
Subtract the base contribution from the contribution of each rank to find the additional contribution for each rank. 
Add these differences to the base contribution to find the contribution for each rank.

Answer: 上上 households contribute *a* bolts of silk, 上中 households contribute *b* bolts and *c* zhang of silk, 上下 households contribute *d* bolts of silk, 中上 households contribute *e* bolts of silk, 中中 households contribute *f* bolts of silk, 中下 households contribute *g* bolts of silk, 下上 households contribute *h* bolts of silk, 下中 households contribute *i* bolts of silk, 下下 households contribute *j* bolts of silk.
"""

from fractions import Fraction

# 戶數 for each rank
戶數 = {
    "上上": 39,
    "上中": 24,
    "上下": 57,
    "中上": 31,
    "中中": 78,
    "中下": 43,
    "下上": 25,
    "下中": 76,
    "下下": 13,
}

# 差 for each rank
差 = {
    "上上": 16,
    "上中": 14,
    "上下": 12,
    "中上": 10,
    "中中": 8,
    "中下": 6,
    "下上": 4,
    "下中": 2,
    "下下": 0,
}

# Calculate total contribution (併數)
併數 = sum(戶數[rank] * 差[rank] for rank in 戶數)

# Calculate total households (凡戶數)
凡戶數 = sum(戶數.values())

# Calculate base contribution per household (所得)
所得 = Fraction(併數, 凡戶數)

# Calculate contribution for each rank
貢獻 = {}
for rank in 戶數:
    貢獻[rank] = 所得 + 差[rank]

# Extract contributions for each rank
a = 貢獻["上上"]
b = 貢獻["上中"].numerator // 貢獻["上中"].denominator  # bolts
c = Fraction(貢獻["上中"].numerator % 貢獻["上中"].denominator, 貢獻["上中"].denominator)  # zhang
d = 貢獻["上下"]
e = 貢獻["中上"]
f = 貢獻["中中"]
g = 貢獻["中下"]
h = 貢獻["下上"]
i = 貢獻["下中"]
j = 貢獻["下下"]
"""
Variable 'a' has wrong value. Expected: 5, Actual: 24
Variable 'b' has wrong value. Expected: 4, Actual: 22
Variable 'c' has wrong value. Expected: 2, Actual: 0
Variable 'd' has wrong value. Expected: 4, Actual: 20
Variable 'e' has wrong value. Expected: 7/2, Actual: 18
Variable 'f' has wrong value. Expected: 3, Actual: 16
Variable 'g' has wrong value. Expected: 5/2, Actual: 14
Variable 'h' has wrong value. Expected: 2, Actual: 12
Variable 'i' has wrong value. Expected: 3/2, Actual: 10
Variable 'j' has wrong value. Expected: 1, Actual: 8"""
