"""
今有絲一两直錢五文有絲一百八十八斤一十两問計直㡬何
術曰列絲一百八十八斤以一十六两乘之納十两得三千一十八两以五文乘之即得
答曰 a貫 
"""

"""
Suppose there is 1 liang of silk worth 5 wen. 
Now, there are 188 jin and 10 liang of silk. 
Question: what is the total value?

The procedure says: Place the 188 jin of silk, multiply it by 16 liang (per jin), and add the 10 liang. 
This gives 3018 liang. Multiply this by 5 wen, and the result is the total value.

Answer: *a* guan.
"""

# 絲一两直錢五文
絲價每两 = 5  # 文

# 絲一百八十八斤
絲斤數 = 188

# 一斤十六两
每斤兩數 = 16

# 納十两
絲額外兩數 = 10

# 列絲一百八十八斤，以一十六两乘之，納十两
總兩數 = (絲斤數 * 每斤兩數) + 絲額外兩數

# 以五文乘之，即得
總價文 = 總兩數 * 絲價每两

# 換算為貫 (1貫 = 1000文)
a = Fraction(總價文, 1000)  # 貫
"""
"""
