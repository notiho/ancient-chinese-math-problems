"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a(=1509/100)貫 。
"""

#----- content starts here -----
"""
Suppose there is 1 liang of silk worth 5 wen. There are 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place the 188 jin of silk, multiply it by 16 liang per jin, and add the 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, obtaining the total value.

Answer: *a*(=1509/100) guan.
"""

from fractions import Fraction

# 絲一两直錢五文
絲價每两 = 5  # 文

# 絲一百八十八斤一十两
絲斤 = 188
絲兩 = 10

# 以一十六两乘之、納十两，得三千一十八两
總絲兩 = (絲斤 * 16) + 絲兩  # 16两 per 斤

# 以五文乘之即得
總價文 = 絲價每两 * 總絲兩

# 換算為貫 (1貫 = 1000文)
a = Fraction(總價文, 1000)  # 1509/100 貫#----- content ends here -----

"""
"""
