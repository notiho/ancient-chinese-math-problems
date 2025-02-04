"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen in total, and for every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Write down the total money, 27 guan and 833 wen. Multiply it by 3, obtaining 83499. Divide it by 5 to get the result.

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 1貫 = 1000文
總文數 = 貫 * 1000 + 文

# 每五文買三枚
每五文得棃 = 3

# 以三乘之
總棃數 = 每五文得棃 * 總文數

# 以五除之
a = 總棃數 // 5  # 棃的整數部分
b = 總棃數 % 5   # 剩餘的文數

a, b#----- content ends here -----

"""
"""
