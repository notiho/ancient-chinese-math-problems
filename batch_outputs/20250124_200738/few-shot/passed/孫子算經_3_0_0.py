"""
今有甲、乙、丙、丁、戊、己、庚、辛、壬、癸九家共輸租，甲出三十五斛，乙出四十六斛，丙出五十七斛，丁出六十八斛，戊出七十九斛，己出八十斛，庚出一百斛，辛出二百一十斛，壬出三百二十五斛，凡九家，共輸租一千斛，僦運直折二百斛外。問：家各幾何？
術曰：置甲出三十五斛，以四乘之，得一百四十斛；以五除之，得二十八斛。乙出四十六斛，以四乘之，得一百八十四斛；以五除之，得三十六斛八斗。丙出五十七斛，以四乘之，得二百二十八斛；以五除之，得四十五斛六斗。丁出六十八斛，以四乘之，得二百七十二斛；以五除之，得五十四斛四斗。戊出七十九斛，以四乘之，得三百一十六斛；以五除之，得六十三斛二斗。己出八十斛，以四乘之，得三百二十斛；以五除之，得六十四斛。庚出一百斛，以四乘之，得四百斛；以五除之，得八十斛。辛出二百一十斛，以四乘之，得八百四十斛；以五除之，得一百六十八斛。壬出三百二十五斛，以四乘之，得一千三百斛；以五除之，得二百六十斛。
答曰：甲 a斛 ，乙 b斛 ，丙 c斛 ，丁 d斛 ，戊 e斛 ，己 f斛 ，庚 g斛 ，辛 h斛 ，壬 i斛 。
"""

#----- content starts here -----
"""
Suppose there are nine households (甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬) contributing rent together. 
The contributions are as follows:
甲 contributes 35 hu, 乙 contributes 46 hu, 丙 contributes 57 hu, 丁 contributes 68 hu, 戊 contributes 79 hu, 己 contributes 80 hu, 庚 contributes 100 hu, 辛 contributes 210 hu, and 壬 contributes 325 hu.
In total, they contribute 1000 hu of rent, with an additional transportation cost equivalent to 200 hu.

Question: How much does each household contribute after accounting for the transportation cost?

The procedure says: For each household, multiply their original contribution by 4, then divide the result by 5 to determine their adjusted contribution.

Answer: 甲 contributes *a* hu, 乙 contributes *b* hu, 丙 contributes *c* hu, 丁 contributes *d* hu, 戊 contributes *e* hu, 己 contributes *f* hu, 庚 contributes *g* hu, 辛 contributes *h* hu, 壬 contributes *i* hu.
"""

# Original contributions
甲 = 35
乙 = 46
丙 = 57
丁 = 68
戊 = 79
己 = 80
庚 = 100
辛 = 210
壬 = 325

# Procedure: Multiply by 4, then divide by 5
a = Fraction(4 * 甲, 5)
b = Fraction(4 * 乙, 5)
c = Fraction(4 * 丙, 5)
d = Fraction(4 * 丁, 5)
e = Fraction(4 * 戊, 5)
f = Fraction(4 * 己, 5)
g = Fraction(4 * 庚, 5)
h = Fraction(4 * 辛, 5)
i = Fraction(4 * 壬, 5)#----- content ends here -----

"""
"""
