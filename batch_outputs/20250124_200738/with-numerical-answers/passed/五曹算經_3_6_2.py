"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a(=16699)枚 奇 b(=4)文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen of money in total. 
For every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Place the money, 27 guan and 833 wen.
Multiply it by 3, obtaining 83499.
Divide it by 5, and the result is obtained.

Answer: *a*(=16699) pears, with *b*(=4) wen remaining.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫等於 1000 文
總文 = 貫 * 1000 + 文

# 每五文買三枚
每五文得棃 = 3

# 以三乘之
總棃文 = 每五文得棃 * 總文

# 以五除之
a = 總棃文 // 5  # 棃的數量
b = 總棃文 % 5   # 剩餘文數

# a = 16699, b = 4#----- content ends here -----

"""
"""
