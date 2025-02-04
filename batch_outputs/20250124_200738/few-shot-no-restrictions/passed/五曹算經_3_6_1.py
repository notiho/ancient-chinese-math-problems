"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen of money, and for every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Take the money, 27 guan and 833 wen, multiply it by 3, obtaining 83,499. Divide this by 5, and the result is the number of pears.

Answer: *a* pears and *b* wen remaining.
"""

from fractions import Fraction

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 1貫 = 1000文
總文數 = 貫 * 1000 + 文

# 每五文買三枚棃
每五文得棃 = 3
每棃需文 = 5

# 列錢二十七貫八百三十三文，以三乘之
總棃數 = 每五文得棃 * 總文數

# 以五除之即得
總棃數除以五 = Fraction(總棃數, 每棃需文)

# 整棃數
a = 總棃數除以五.numerator // 總棃數除以五.denominator

# 剩餘文數
b = 總棃數除以五.numerator % 總棃數除以五.denominator

a, b#----- content ends here -----

"""
"""
