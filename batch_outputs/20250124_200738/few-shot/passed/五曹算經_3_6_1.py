"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen. Each 5 wen buys 3 pears.
Question: how many pears can be obtained?

The procedure says: Write down the amount of money, 27 guan and 833 wen. Multiply it by 3, obtaining 83499. Divide it by 5, and the result is the number of pears.

Answer: *a* pears and *b* wen remaining.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 1貫 = 1000文
總文 = 貫 * 1000 + 文

# 每五文買三枚
每五文得棃 = 3

# 以三乘之
總棃文 = 每五文得棃 * 總文

# 以五除之
a = 總棃文 // 5  # 棃的整數部分
b = 總棃文 % 5   # 剩餘的文#----- content ends here -----

"""
"""
