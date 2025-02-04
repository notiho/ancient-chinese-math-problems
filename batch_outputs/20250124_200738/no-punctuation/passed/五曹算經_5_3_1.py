"""
今有絲一两直錢五文有絲一百八十八斤一十两問計直㡬何
術曰列絲一百八十八斤以一十六两乘之納十两得三千一十八两以五文乘之即得
答曰 a貫 
"""

#----- content starts here -----
"""
Suppose there is 1 liang of silk worth 5 wen. Now there are 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place the 188 jin of silk, multiply it by 16 liang [per jin], and add the 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, and the result is obtained.

Answer: *a* guan.
"""

# 絲一两直錢五文
絲價每两 = 5  # 文

# 絲一百八十八斤
絲斤 = 188

# 一十两
絲多余两 = 10

# 以一十六两乘之
絲總两 = 絲斤 * 16

# 納十两
絲總两 += 絲多余两

# 得三千一十八两
assert 絲總两 == 3018

# 以五文乘之
總價文 = 絲總两 * 絲價每两

# 換算為貫 (1 貫 = 1000 文)
a = Fraction(總價文, 1000)  # 貫#----- content ends here -----

"""
"""
