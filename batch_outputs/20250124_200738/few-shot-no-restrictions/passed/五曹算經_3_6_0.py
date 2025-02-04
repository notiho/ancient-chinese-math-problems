"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen of money. 
Each 5 wen buys 3 pears.
Question: how many pears can be bought?

The procedure says: Write down the money, 27 guan and 833 wen. 
Multiply it by 3, obtaining 83,499.
Divide it by 5, and the result is the number of pears.

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫有 1000 文
總文數 = 貫 * 1000 + 文

# 每 5 文買 3 棃
棃率 = Fraction(3, 5)

# 總棃數
總棃數 = 總文數 * 棃率

# 得整棃數和剩餘文數
a = 總棃數.numerator // 總棃數.denominator  # 整棃數
b = 總棃數.numerator % 總棃數.denominator  # 剩餘文數

a, b#----- content ends here -----

"""
"""
