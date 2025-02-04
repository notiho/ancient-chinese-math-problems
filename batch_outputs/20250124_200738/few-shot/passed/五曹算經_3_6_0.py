"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen. For every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Write down the money, 27 guan and 833 wen. Multiply it by 3, obtaining 83,499. Divide it by 5, and the result is obtained.

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫等於一千文
總文 = 貫 * 1000 + 文

# 每五文買三枚
每五文得棃 = 3

# 以三乘之
總棃文 = 每五文得棃 * 總文

# 以五除之
總棃 = Fraction(總棃文, 5)

# 得整數棃數和餘文
a = 總棃.numerator // 總棃.denominator  # 整數棃數
b = 總棃.numerator % 總棃.denominator   # 餘文#----- content ends here -----

"""
"""
