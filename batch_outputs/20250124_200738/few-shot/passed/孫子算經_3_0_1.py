"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
術曰：置甲出三十五斛，以四乘之，得一百四十斛；以五除之，得二十八斛。乙出四十六斛，以四乘之，得一百八十四斛；以五除之，得三十六斛八斗。丙出五十七斛，以四乘之，得二百二十八斛；以五除之，得四十五斛六斗。丁出六十八斛，以四乘之，得二百七十二斛；以五除之，得五十四斛四斗。戊出七十九斛，以四乘之，得三百一十六斛；以五除之，得六十三斛二斗。己出八十斛，以四乘之，得三百二十斛；以五除之，得六十四斛。庚出一百斛，以四乘之，得四百斛；以五除之，得八十斛。辛出二百一十斛，以四乘之，得八百四十斛；以五除之，得一百六十八斛。壬出三百二十五斛，以四乘之，得一千三百斛；以五除之，得二百六十斛。
答曰：甲 a斛 ，乙 b斛 ，丙 c斛 ，丁 d斛 ，戊 e斛 ，己 f斛 ，庚 g斛 ，辛 h斛 ，壬 i斛 。
"""

#----- content starts here -----
"""
Suppose there are nine households (Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, Ren) collectively paying rent.
Jia pays 35 hu, Yi pays 46 hu, Bing pays 57 hu, Ding pays 68 hu, Wu pays 79 hu, Ji pays 80 hu, Geng pays 100 hu, Xin pays 210 hu, and Ren pays 325 hu.
In total, the nine households pay 1000 hu of rent, and the transportation cost is deducted as 200 hu.
Question: how much does each household contribute after deducting the transportation cost?

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

# Contributions of each household in hu
contributions = [35, 46, 57, 68, 79, 80, 100, 210, 325]

# Transportation cost adjustment factors
multiplier = 4
divisor = 5

# Calculate the adjusted contributions for each household
adjusted_contributions = [Fraction(contribution * multiplier, divisor) for contribution in contributions]

# Assign the results to variables
a, b, c, d, e, f, g, h, i = adjusted_contributions

# Results
a, b, c, d, e, f, g, h, i#----- content ends here -----

"""
"""
