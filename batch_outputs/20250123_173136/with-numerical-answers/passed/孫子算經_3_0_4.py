"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
術曰：置甲出三十五斛，以四乘之，得一百四十斛；以五除之，得二十八斛。乙出四十六斛，以四乘之，得一百八十四斛；以五除之，得三十六斛八斗。丙出五十七斛，以四乘之，得二百二十八斛；以五除之，得四十五斛六斗。丁出六十八斛，以四乘之，得二百七十二斛；以五除之，得五十四斛四斗。戊出七十九斛，以四乘之，得三百一十六斛；以五除之，得六十三斛二斗。己出八十斛，以四乘之，得三百二十斛；以五除之，得六十四斛。庚出一百斛，以四乘之，得四百斛；以五除之，得八十斛。辛出二百一十斛，以四乘之，得八百四十斛；以五除之，得一百六十八斛。壬出三百二十五斛，以四乘之，得一千三百斛；以五除之，得二百六十斛。
答曰：甲 a(=28)斛 ，乙 b(=184/5)斛 ，丙 c(=228/5)斛 ，丁 d(=272/5)斛 ，戊 e(=316/5)斛 ，己 f(=64)斛 ，庚 g(=80)斛 ，辛 h(=168)斛 ，壬 i(=260)斛 。
"""

"""
Suppose there are nine households: Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, and Ren. Together, they contribute rent.
Jia contributes 35 hu, Yi contributes 46 hu, Bing contributes 57 hu, Ding contributes 68 hu, Wu contributes 79 hu, Ji contributes 80 hu, Geng contributes 100 hu, Xin contributes 210 hu, and Ren contributes 325 hu.
In total, the nine households contribute 1000 hu of rent, with an additional transportation fee equivalent to 200 hu deducted proportionally.
Question: how much does each household contribute after the deduction?

The procedure says: Place Jia's contribution of 35 hu. Multiply it by 4, obtaining 140 hu. Divide it by 5, obtaining 28 hu.
For Yi's contribution of 46 hu, multiply it by 4, obtaining 184 hu. Divide it by 5, obtaining 36 hu and 8 dou.
For Bing's contribution of 57 hu, multiply it by 4, obtaining 228 hu. Divide it by 5, obtaining 45 hu and 6 dou.
For Ding's contribution of 68 hu, multiply it by 4, obtaining 272 hu. Divide it by 5, obtaining 54 hu and 4 dou.
For Wu's contribution of 79 hu, multiply it by 4, obtaining 316 hu. Divide it by 5, obtaining 63 hu and 2 dou.
For Ji's contribution of 80 hu, multiply it by 4, obtaining 320 hu. Divide it by 5, obtaining 64 hu.
For Geng's contribution of 100 hu, multiply it by 4, obtaining 400 hu. Divide it by 5, obtaining 80 hu.
For Xin's contribution of 210 hu, multiply it by 4, obtaining 840 hu. Divide it by 5, obtaining 168 hu.
For Ren's contribution of 325 hu, multiply it by 4, obtaining 1300 hu. Divide it by 5, obtaining 260 hu.

Answer: Jia contributes *a*(=28) hu, Yi contributes *b*(=184/5) hu, Bing contributes *c*(=228/5) hu, Ding contributes *d*(=272/5) hu, Wu contributes *e*(=316/5) hu, Ji contributes *f*(=64) hu, Geng contributes *g*(=80) hu, Xin contributes *h*(=168) hu, Ren contributes *i*(=260) hu.
"""

# Contributions from each household
甲 = 35
乙 = 46
丙 = 57
丁 = 68
戊 = 79
己 = 80
庚 = 100
辛 = 210
壬 = 325

# Multiplication factor (4)
乘法 = 4

# Division factor (5)
除法 = 5

# Calculating the adjusted contributions
a = Fraction(甲 * 乘法, 除法)  # 28
b = Fraction(乙 * 乘法, 除法)  # 184/5
c = Fraction(丙 * 乘法, 除法)  # 228/5
d = Fraction(丁 * 乘法, 除法)  # 272/5
e = Fraction(戊 * 乘法, 除法)  # 316/5
f = Fraction(己 * 乘法, 除法)  # 64
g = Fraction(庚 * 乘法, 除法)  # 80
h = Fraction(辛 * 乘法, 除法)  # 168
i = Fraction(壬 * 乘法, 除法)  # 260
"""
"""
