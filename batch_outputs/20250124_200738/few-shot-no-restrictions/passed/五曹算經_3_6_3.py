"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen of money. Each 5 wen buys 3 pears.
Question: how many pears can be bought?

The procedure says: Write down the money as 27 guan and 833 wen. Multiply it by 3, obtaining 83,499. Divide it by 5 to get the result.

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫有 1000 文
總文數 = 貫 * 1000 + 文

# 每五文買三枚
每五文得棃 = 3

# 以三乘之
總棃數 = 每五文得棃 * 總文數

# 以五除之
每枚價格 = 5
a = 總棃數 // 每枚價格  # 棃的整數部分
b = 總棃數 % 每枚價格  # 剩餘的文數

a, b  # Output the result as (a枚, b文)#----- content ends here -----

"""
"""
