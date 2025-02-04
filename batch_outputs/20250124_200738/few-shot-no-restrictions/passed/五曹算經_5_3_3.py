"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is silk, 1 liang of which is worth 5 wen. Now there is 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place 188 jin of silk, multiply it by 16 liang per jin, and add 10 liang, obtaining 3018 liang.
Multiply this by 5 wen to get the total value.

Answer: *a* guan.
"""

from fractions import Fraction

# 絲一两直錢五文
價值每兩 = 5  # in wen

# 絲一百八十八斤一十两
斤 = 188
兩 = 10

# 一斤等於十六两
兩每斤 = 16

# 計算總兩數
總兩數 = (斤 * 兩每斤) + 兩

# 以五文乘之即得
總價值文 = 總兩數 * 價值每兩

# 一貫等於一千文
文每貫 = 1000

# 換算為貫
a = Fraction(總價值文, 文每貫)

a#----- content ends here -----

"""
"""
