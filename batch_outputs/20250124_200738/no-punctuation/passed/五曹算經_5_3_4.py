"""
今有絲一两直錢五文有絲一百八十八斤一十两問計直㡬何
術曰列絲一百八十八斤以一十六两乘之納十两得三千一十八两以五文乘之即得
答曰 a貫 
"""

#----- content starts here -----
"""
Suppose there is 1 liang of silk worth 5 wen. 
There are 188 jin and 10 liang of silk.
Question: how much is the total value?

The procedure says: Place 188 jin of silk, multiply it by 16 liang [per jin], and add 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, obtaining the total value.

Answer: *a* guan.
"""

# 絲一两直錢五文
絲一两價值 = 5  # in wen

# 絲一百八十八斤
絲斤數 = 188

# 一斤十六两
一斤 = 16

# 以一十六两乘之
總兩數 = 絲斤數 * 一斤

# 納十两
總兩數 += 10

# 得三千一十八两
assert 總兩數 == 3018  # Verify the calculation

# 以五文乘之
總價值文 = 總兩數 * 絲一两價值

# 換算為貫 (1貫 = 1000文)
a = Fraction(總價值文, 1000)  # in guan#----- content ends here -----

"""
"""
