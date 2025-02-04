"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a(=3950)人 奇 b(=16) 丁。
"""

#----- content starts here -----
"""
Suppose there are 98,766 adult males (丁). For every 25 adult males, one soldier (兵) is conscripted.
Question: how many soldiers are conscripted, and how many adult males are left over?

The procedure says: Place 98,766 adult males as the dividend.
Take 25 as the divisor.
Divide the dividend by the divisor, obtaining the number of soldiers.
The remainder is the number of leftover adult males.

Answer: *a*(=3950) soldiers and *b*(=16) leftover adult males.
"""

# 置丁九萬八千七百六十六為實
實 = 98766

# 以二十五為法
法 = 25

# 實如法，即得
a = 實 // 法  # 3950 soldiers
b = 實 % 法   # 16 leftover adult males#----- content ends here -----

"""
"""
