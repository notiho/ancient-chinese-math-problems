"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
術曰：置甲出三十五斛，以四乘之，得一百四十斛；以五除之，得二十八斛。乙出四十六斛，以四乘之，得一百八十四斛；以五除之，得三十六斛八斗。丙出五十七斛，以四乘之，得二百二十八斛；以五除之，得四十五斛六斗。丁出六十八斛，以四乘之，得二百七十二斛；以五除之，得五十四斛四斗。戊出七十九斛，以四乘之，得三百一十六斛；以五除之，得六十三斛二斗。己出八十斛，以四乘之，得三百二十斛；以五除之，得六十四斛。庚出一百斛，以四乘之，得四百斛；以五除之，得八十斛。辛出二百一十斛，以四乘之，得八百四十斛；以五除之，得一百六十八斛。壬出三百二十五斛，以四乘之，得一千三百斛；以五除之，得二百六十斛。
答曰：甲 a(=28)斛 ，乙 b(=184/5)斛 ，丙 c(=228/5)斛 ，丁 d(=272/5)斛 ，戊 e(=316/5)斛 ，己 f(=64)斛 ，庚 g(=80)斛 ，辛 h(=168)斛 ，壬 i(=260)斛 。
"""

#----- content starts here -----
"""
Suppose there are nine households: Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, and Ren. Together, they pay a total of 1000 hu in rent. 
The rent contribution of each household is as follows: Jia pays 35 hu, Yi pays 46 hu, Bing pays 57 hu, Ding pays 68 hu, Wu pays 79 hu, Ji pays 80 hu, Geng pays 100 hu, Xin pays 210 hu, and Ren pays 325 hu. 
Additionally, the transportation cost is deducted as 200 hu. 
Question: How much does each household contribute after deducting the transportation cost?

The procedure says: Place Jia's contribution of 35 hu, multiply it by 4, obtaining 140 hu; divide it by 5, obtaining 28 hu. 
For Yi's contribution of 46 hu, multiply it by 4, obtaining 184 hu; divide it by 5, obtaining 36 hu and 8 dou. 
For Bing's contribution of 57 hu, multiply it by 4, obtaining 228 hu; divide it by 5, obtaining 45 hu and 6 dou. 
For Ding's contribution of 68 hu, multiply it by 4, obtaining 272 hu; divide it by 5, obtaining 54 hu and 4 dou. 
For Wu's contribution of 79 hu, multiply it by 4, obtaining 316 hu; divide it by 5, obtaining 63 hu and 2 dou. 
For Ji's contribution of 80 hu, multiply it by 4, obtaining 320 hu; divide it by 5, obtaining 64 hu. 
For Geng's contribution of 100 hu, multiply it by 4, obtaining 400 hu; divide it by 5, obtaining 80 hu. 
For Xin's contribution of 210 hu, multiply it by 4, obtaining 840 hu; divide it by 5, obtaining 168 hu. 
For Ren's contribution of 325 hu, multiply it by 4, obtaining 1300 hu; divide it by 5, obtaining 260 hu.

Answer: Jia contributes *a*(=28) hu, Yi contributes *b*(=184/5) hu, Bing contributes *c*(=228/5) hu, Ding contributes *d*(=272/5) hu, Wu contributes *e*(=316/5) hu, Ji contributes *f*(=64) hu, Geng contributes *g*(=80) hu, Xin contributes *h*(=168) hu, Ren contributes *i*(=260) hu.
"""

# Contributions of each household in hu
contributions = [35, 46, 57, 68, 79, 80, 100, 210, 325]

# Transportation cost adjustment: multiply by 4 and divide by 5
adjusted_contributions = [Fraction(4 * c, 5) for c in contributions]

# Assign results to variables
a, b, c, d, e, f, g, h, i = adjusted_contributions

# Results:
# a = 28
# b = 184/5
# c = 228/5
# d = 272/5
# e = 316/5
# f = 64
# g = 80
# h = 168
# i = 260#----- content ends here -----

"""
"""
