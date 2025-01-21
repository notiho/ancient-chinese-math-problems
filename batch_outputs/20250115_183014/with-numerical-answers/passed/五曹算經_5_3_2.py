"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a(=1509/100)貫 。
"""

"""
Suppose there is 1 liang of silk worth 5 wen. There are 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place the 188 jin of silk. Multiply it by 16 liang per jin, and add the 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, obtaining the total value.

Answer: *a*(=1509/100) guan.
"""

from fractions import Fraction

# 絲一两直錢五文
絲單價 = 5  # 5 wen per liang

# 絲一百八十八斤一十两
絲斤 = 188
絲兩 = 10

# 以一十六两乘之、納十两
總兩 = (絲斤 * 16) + 絲兩  # 1 jin = 16 liang

# 以五文乘之即得
總價文 = 總兩 * 絲單價

# 1 貫 = 1000 文
a = Fraction(總價文, 1000)  # Convert to guan (貫)

# a = 1509/100 貫
"""
"""
