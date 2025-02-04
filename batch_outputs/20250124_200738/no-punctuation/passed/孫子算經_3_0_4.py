"""
今有甲乙丙丁戊己庚辛壬癸九家共輸租甲出三十五斛乙出四十六斛丙出五十七斛丁出六十八斛戊出七十九斛己出八十斛庚出一百斛辛出二百一十斛壬出三百二十五斛凡九家共輸租一千斛僦運直折二百斛外問家各幾何
術曰置甲出三十五斛以四乘之得一百四十斛以五除之得二十八斛乙出四十六斛以四乘之得一百八十四斛以五除之得三十六斛八斗丙出五十七斛以四乘之得二百二十八斛以五除之得四十五斛六斗丁出六十八斛以四乘之得二百七十二斛以五除之得五十四斛四斗戊出七十九斛以四乘之得三百一十六斛以五除之得六十三斛二斗己出八十斛以四乘之得三百二十斛以五除之得六十四斛庚出一百斛以四乘之得四百斛以五除之得八十斛辛出二百一十斛以四乘之得八百四十斛以五除之得一百六十八斛壬出三百二十五斛以四乘之得一千三百斛以五除之得二百六十斛
答曰甲 a斛 乙 b斛 丙 c斛 丁 d斛 戊 e斛 己 f斛 庚 g斛 辛 h斛 壬 i斛 
"""

#----- content starts here -----
"""
Suppose there are nine households: Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, and Ren. Together, they contribute a total rent of 1000 hu. 
The transportation cost is deducted as 200 hu. The rent is distributed among the households proportionally to their contributions.

The contributions are as follows:
Jia: 35 hu, Yi: 46 hu, Bing: 57 hu, Ding: 68 hu, Wu: 79 hu, Ji: 80 hu, Geng: 100 hu, Xin: 210 hu, Ren: 325 hu.

The procedure says: For each household, take their contribution, multiply it by 4, and divide by 5. This gives the adjusted rent for each household.

Answer: Jia *a* hu, Yi *b* hu, Bing *c* hu, Ding *d* hu, Wu *e* hu, Ji *f* hu, Geng *g* hu, Xin *h* hu, Ren *i* hu.
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

# Procedure: Multiply by 4 and divide by 5 for each household
a = Fraction(甲 * 4, 5)
b = Fraction(乙 * 4, 5)
c = Fraction(丙 * 4, 5)
d = Fraction(丁 * 4, 5)
e = Fraction(戊 * 4, 5)
f = Fraction(己 * 4, 5)
g = Fraction(庚 * 4, 5)
h = Fraction(辛 * 4, 5)
i = Fraction(壬 * 4, 5)#----- content ends here -----

"""
"""
