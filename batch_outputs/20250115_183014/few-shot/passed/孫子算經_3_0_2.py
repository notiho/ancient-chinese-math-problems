"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
術曰：置甲出三十五斛，以四乘之，得一百四十斛；以五除之，得二十八斛。乙出四十六斛，以四乘之，得一百八十四斛；以五除之，得三十六斛八斗。丙出五十七斛，以四乘之，得二百二十八斛；以五除之，得四十五斛六斗。丁出六十八斛，以四乘之，得二百七十二斛；以五除之，得五十四斛四斗。戊出七十九斛，以四乘之，得三百一十六斛；以五除之，得六十三斛二斗。己出八十斛，以四乘之，得三百二十斛；以五除之，得六十四斛。庚出一百斛，以四乘之，得四百斛；以五除之，得八十斛。辛出二百一十斛，以四乘之，得八百四十斛；以五除之，得一百六十八斛。壬出三百二十五斛，以四乘之，得一千三百斛；以五除之，得二百六十斛。
答曰：甲 a斛 ，乙 b斛 ，丙 c斛 ，丁 d斛 ，戊 e斛 ，己 f斛 ，庚 g斛 ，辛 h斛 ，壬 i斛 。
"""

"""
Suppose there are nine families (Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, Ren) who together contribute rent.
Jia contributes 35 hu, Yi contributes 46 hu, Bing contributes 57 hu, Ding contributes 68 hu, Wu contributes 79 hu, Ji contributes 80 hu, Geng contributes 100 hu, Xin contributes 210 hu, and Ren contributes 325 hu.
In total, the nine families contribute 1000 hu of rent, and the transportation cost is deducted as 200 hu.
Question: how much does each family contribute after the deduction?

The procedure says: Place Jia's contribution of 35 hu, multiply it by 4, obtaining 140 hu; divide it by 5, obtaining 28 hu.
Place Yi's contribution of 46 hu, multiply it by 4, obtaining 184 hu; divide it by 5, obtaining 36 hu and 8 dou.
Place Bing's contribution of 57 hu, multiply it by 4, obtaining 228 hu; divide it by 5, obtaining 45 hu and 6 dou.
Place Ding's contribution of 68 hu, multiply it by 4, obtaining 272 hu; divide it by 5, obtaining 54 hu and 4 dou.
Place Wu's contribution of 79 hu, multiply it by 4, obtaining 316 hu; divide it by 5, obtaining 63 hu and 2 dou.
Place Ji's contribution of 80 hu, multiply it by 4, obtaining 320 hu; divide it by 5, obtaining 64 hu.
Place Geng's contribution of 100 hu, multiply it by 4, obtaining 400 hu; divide it by 5, obtaining 80 hu.
Place Xin's contribution of 210 hu, multiply it by 4, obtaining 840 hu; divide it by 5, obtaining 168 hu.
Place Ren's contribution of 325 hu, multiply it by 4, obtaining 1300 hu; divide it by 5, obtaining 260 hu.

Answer: Jia contributes *a* hu, Yi contributes *b* hu, Bing contributes *c* hu, Ding contributes *d* hu, Wu contributes *e* hu, Ji contributes *f* hu, Geng contributes *g* hu, Xin contributes *h* hu, Ren contributes *i* hu.
"""

# Contributions of each family in hu
contributions = {
    "甲": 35,
    "乙": 46,
    "丙": 57,
    "丁": 68,
    "戊": 79,
    "己": 80,
    "庚": 100,
    "辛": 210,
    "壬": 325,
}

# Transportation cost multiplier and divisor
multiplier = 4
divisor = 5

# Calculate the adjusted contributions for each family
adjusted_contributions = {}
for family, contribution in contributions.items():
    adjusted_contributions[family] = Fraction(contribution * multiplier, divisor)

# Extract the results
a = adjusted_contributions["甲"]
b = adjusted_contributions["乙"]
c = adjusted_contributions["丙"]
d = adjusted_contributions["丁"]
e = adjusted_contributions["戊"]
f = adjusted_contributions["己"]
g = adjusted_contributions["庚"]
h = adjusted_contributions["辛"]
i = adjusted_contributions["壬"]
"""
"""
