"""
今有錢二貫四百文買錫一斤問兩銖絫各幾何
術曰置錢數以十六除之得兩價欲知銖價即置兩價以二十四除為銖價退銖價一等為絫價
答曰兩 a文 銖 b文 絫 c分
"""

"""
Suppose there are 2 guan and 400 wen used to buy 1 jin of tin.
Question: how much does each liang, zhu, and lü cost?

The procedure says: Place the total amount of money and divide it by 16 to obtain the price per liang.
If you want to know the price per zhu, then place the price per liang and divide it by 24 to obtain the price per zhu.
To find the price per lü, reduce the price per zhu by one order of magnitude.

Answer: *a* wen per liang, *b* wen per zhu, and *c* fen per lü.
"""

# 錢二貫四百文
錢數 = 2 * 1000 + 400  # 1貫 = 1000文

# 置錢數以十六除之，得兩價
兩價 = Fraction(錢數, 16)

# 欲知銖價，即置兩價以二十四除
銖價 = Fraction(兩價, 24)

# 退銖價一等，為絫價
絫價 = Fraction(銖價, 10)

a = 兩價
b = 銖價
c = 絫價
"""
Variable 'c' has wrong value. Expected: 25/4, Actual: 5/8"""
