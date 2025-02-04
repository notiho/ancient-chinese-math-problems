"""
今有甲乙丙丁戊己庚辛壬癸九家共輸租甲出三十五斛乙出四十六斛丙出五十七斛丁出六十八斛戊出七十九斛己出八十斛庚出一百斛辛出二百一十斛壬出三百二十五斛凡九家共輸租一千斛僦運直折二百斛外問家各幾何
術曰置甲出三十五斛以四乘之得一百四十斛以五除之得二十八斛乙出四十六斛以四乘之得一百八十四斛以五除之得三十六斛八斗丙出五十七斛以四乘之得二百二十八斛以五除之得四十五斛六斗丁出六十八斛以四乘之得二百七十二斛以五除之得五十四斛四斗戊出七十九斛以四乘之得三百一十六斛以五除之得六十三斛二斗己出八十斛以四乘之得三百二十斛以五除之得六十四斛庚出一百斛以四乘之得四百斛以五除之得八十斛辛出二百一十斛以四乘之得八百四十斛以五除之得一百六十八斛壬出三百二十五斛以四乘之得一千三百斛以五除之得二百六十斛
答曰甲 a斛 乙 b斛 丙 c斛 丁 d斛 戊 e斛 己 f斛 庚 g斛 辛 h斛 壬 i斛 
"""

"""
Suppose there are nine households: Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, and Ren. Together, they contribute a total rent of 1000 hu.
The transportation cost is deducted as 200 hu. How much does each household contribute after deducting the transportation cost?

The procedure says: Place Jia's contribution of 35 hu, multiply it by 4, obtaining 140 hu. Divide it by 5, obtaining 28 hu.
Place Yi's contribution of 46 hu, multiply it by 4, obtaining 184 hu. Divide it by 5, obtaining 36 hu and 8 dou.
Place Bing's contribution of 57 hu, multiply it by 4, obtaining 228 hu. Divide it by 5, obtaining 45 hu and 6 dou.
Place Ding's contribution of 68 hu, multiply it by 4, obtaining 272 hu. Divide it by 5, obtaining 54 hu and 4 dou.
Place Wu's contribution of 79 hu, multiply it by 4, obtaining 316 hu. Divide it by 5, obtaining 63 hu and 2 dou.
Place Ji's contribution of 80 hu, multiply it by 4, obtaining 320 hu. Divide it by 5, obtaining 64 hu.
Place Geng's contribution of 100 hu, multiply it by 4, obtaining 400 hu. Divide it by 5, obtaining 80 hu.
Place Xin's contribution of 210 hu, multiply it by 4, obtaining 840 hu. Divide it by 5, obtaining 168 hu.
Place Ren's contribution of 325 hu, multiply it by 4, obtaining 1300 hu. Divide it by 5, obtaining 260 hu.

Answer: Jia contributes *a* hu, Yi contributes *b* hu, Bing contributes *c* hu, Ding contributes *d* hu, Wu contributes *e* hu, Ji contributes *f* hu, Geng contributes *g* hu, Xin contributes *h* hu, Ren contributes *i* hu.
"""

# Contributions of each household in hu
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

# Multiplication factor and divisor
multiplication_factor = 4
divisor = 5

# Calculate the adjusted contributions
adjusted_contributions = {}
for household, contribution in contributions.items():
    adjusted_contributions[household] = Fraction(contribution * multiplication_factor, divisor)

# Assign results to variables
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
