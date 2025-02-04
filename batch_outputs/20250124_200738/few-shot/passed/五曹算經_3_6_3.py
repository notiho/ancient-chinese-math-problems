"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there is 27 guan and 833 wen of money. For every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Place the money, 27 guan and 833 wen. Multiply it by 3, obtaining 83499.
Divide it by 5, and the result is obtained.

Answer: *a* pears and *b* wen remaining.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 一貫等於一千文
總文 = 貫 * 1000 + 文

# 每五文買三枚棃
每五文棃數 = 3

# 以三乘之
總棃數 = 每五文棃數 * 總文

# 以五除之
a = 總棃數 // 5  # 得到整棃數
b = 總棃數 % 5   # 剩餘文數#----- content ends here -----

"""
"""
