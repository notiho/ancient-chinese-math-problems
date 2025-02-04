"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is silk, 1 liang of which is worth 5 wen. There is a total of 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place 188 jin of silk, multiply it by 16 liang per jin, and add 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, obtaining the total value.

Answer: *a* guan.
"""

# 絲一两直錢五文
絲價每两 = 5  # 每两的價值（文）

# 絲一百八十八斤一十两
絲斤 = 188  # 絲的斤數
絲兩 = 10   # 額外的两數

# 以一十六两乘之、納十两，得三千一十八两
總兩 = (絲斤 * 16) + 絲兩

# 以五文乘之即得
總價文 = 總兩 * 絲價每两

# 1貫 = 1000文
a = Fraction(總價文, 1000)  # 總價以貫為單位#----- content ends here -----

"""
"""
