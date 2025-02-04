"""
今有甲乙丙丁戊己庚辛壬癸九家共輸租甲出三十五斛乙出四十六斛丙出五十七斛丁出六十八斛戊出七十九斛己出八十斛庚出一百斛辛出二百一十斛壬出三百二十五斛凡九家共輸租一千斛僦運直折二百斛外問家各幾何
術曰置甲出三十五斛以四乘之得一百四十斛以五除之得二十八斛乙出四十六斛以四乘之得一百八十四斛以五除之得三十六斛八斗丙出五十七斛以四乘之得二百二十八斛以五除之得四十五斛六斗丁出六十八斛以四乘之得二百七十二斛以五除之得五十四斛四斗戊出七十九斛以四乘之得三百一十六斛以五除之得六十三斛二斗己出八十斛以四乘之得三百二十斛以五除之得六十四斛庚出一百斛以四乘之得四百斛以五除之得八十斛辛出二百一十斛以四乘之得八百四十斛以五除之得一百六十八斛壬出三百二十五斛以四乘之得一千三百斛以五除之得二百六十斛
答曰甲 a斛 乙 b斛 丙 c斛 丁 d斛 戊 e斛 己 f斛 庚 g斛 辛 h斛 壬 i斛 
"""

"""
Suppose there are nine families: Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, and Ren. 
They collectively pay a rent of 1000 hu. 
The transportation cost is deducted as 200 hu. 
The remaining rent is distributed proportionally based on their original contributions.

Jia contributes 35 hu, Yi contributes 46 hu, Bing contributes 57 hu, Ding contributes 68 hu, Wu contributes 79 hu, Ji contributes 80 hu, Geng contributes 100 hu, Xin contributes 210 hu, and Ren contributes 325 hu.

The procedure says: 
For each family, take their contribution and multiply it by 4. 
Divide the result by 5 to determine their share of the rent after deducting transportation costs.

Answer: Jia gets *a* hu, Yi gets *b* hu, Bing gets *c* hu, Ding gets *d* hu, Wu gets *e* hu, Ji gets *f* hu, Geng gets *g* hu, Xin gets *h* hu, Ren gets *i* hu.
"""

# Contributions of each family
甲 = 35
乙 = 46
丙 = 57
丁 = 68
戊 = 79
己 = 80
庚 = 100
辛 = 210
壬 = 325

# Total rent after deducting transportation cost
總租 = 1000 - 200

# Procedure: Multiply each contribution by 4 and divide by 5
a = Fraction(甲 * 4, 5)
b = Fraction(乙 * 4, 5)
c = Fraction(丙 * 4, 5)
d = Fraction(丁 * 4, 5)
e = Fraction(戊 * 4, 5)
f = Fraction(己 * 4, 5)
g = Fraction(庚 * 4, 5)
h = Fraction(辛 * 4, 5)
i = Fraction(壬 * 4, 5)
"""
"""
