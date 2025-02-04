"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

"""
Suppose there are 27 guan and 833 wen of money. For every 5 wen, 3 pears can be purchased.
Question: how many pears can be obtained?

The procedure says: Write down the money as 27 guan and 833 wen. Multiply it by 3, obtaining 83,499. Divide it by 5, and the result is obtained.

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫為一千文
總文 = 貫 * 1000 + 文

# 以三乘之
總文乘三 = 3 * 總文

# 以五除之
每五文得三枚 = 5
總梨數 = Fraction(總文乘三, 每五文得三枚)

# 分離整數部分和餘數
a = 總梨數.numerator // 總梨數.denominator  # 整數部分（梨的數量）
b = 總梨數.numerator % 總梨數.denominator  # 餘數（剩餘文數）
"""
"""
