"""
今有絲一两直錢五文有絲一百八十八斤一十两問計直㡬何
術曰列絲一百八十八斤以一十六两乘之納十两得三千一十八两以五文乘之即得
答曰 a貫 
"""

#----- content starts here -----
"""
Suppose there is 1 liang of silk worth 5 wen. There are 188 jin and 10 liang of silk.
Question: what is the total value?

The procedure says: Place the 188 jin of silk, multiply it by 16 liang [per jin], and add the 10 liang, obtaining 3018 liang.
Multiply this by 5 wen, obtaining the total value.

Answer: *a* guan.
"""

# 絲一两直錢五文
絲單價 = 5  # 每两的價值，單位：文

# 絲一百八十八斤
絲斤數 = 188

# 一十两
絲額外兩數 = 10

# 以一十六两乘之，納十两，得三千一十八两
絲總兩數 = (絲斤數 * 16) + 絲額外兩數

# 以五文乘之，即得
總價值文 = 絲總兩數 * 絲單價

# 換算為貫（1貫 = 1000文）
a = Fraction(總價值文, 1000)  # 單位：貫#----- content ends here -----

"""
"""
