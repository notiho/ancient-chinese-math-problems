"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is 1 liang of silk worth 5 wen. There is 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place the 188 jin of silk, multiply it by 16 liang per jin, and add the 10 liang, obtaining 3018 liang.
Multiply this by 5 wen to get the total value.

Answer: *a* guan.
"""

from fractions import Fraction

# 絲一两直錢五文
絲單價 = 5  # 文 per 两

# 絲一百八十八斤一十两
絲斤 = 188  # 斤
絲兩 = 10  # 两

# 每斤十六两
每斤兩 = 16

# 計算總两數
總兩 = (絲斤 * 每斤兩) + 絲兩

# 以五文乘之即得
總價值文 = 總兩 * 絲單價

# 一貫等於一千文
文每貫 = 1000

# 計算貫數
a = Fraction(總價值文, 文每貫)

a#----- content ends here -----

"""
"""
