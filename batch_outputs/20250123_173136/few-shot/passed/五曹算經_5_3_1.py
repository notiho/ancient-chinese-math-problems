"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

"""
Suppose there is 1 liang of silk worth 5 wen. There is 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place the 188 jin of silk. Multiply it by 16 liang per jin, and add 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 絲一两直錢五文
絲價每两 = 5  # 5 文 per 1 两

# 絲一百八十八斤一十两
斤 = 188
兩 = 10

# 以一十六两乘之、納十两，得三千一十八两
總兩 = 斤 * 16 + 兩

# 以五文乘之即得
總價文 = 總兩 * 絲價每两

# 1 貫 = 1000 文
a = Fraction(總價文, 1000)  # Convert to 貫

"""
"""
