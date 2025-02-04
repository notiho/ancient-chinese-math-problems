"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a(=16699)枚 奇 b(=4)文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen of money. For every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Place the money, 27 guan and 833 wen. Multiply it by 3, obtaining 83499. Divide it by 5, and the result is obtained.

Answer: *a*(=16699) pears, with a remainder of *b*(=4) wen.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 1貫 = 1000文
總文 = 貫 * 1000 + 文

# 每五文買三枚
每五文得 = 3

# 以三乘之
總果實 = 每五文得 * 總文

# 以五除之即得
a = 總果實 // 5  # 16699 枚
b = 總果實 % 5   # 4 文#----- content ends here -----

"""
"""
