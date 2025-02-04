"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk worth 345 qian. Now, there is 7 liang and 12 zhu of silk.
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

# 1斤 = 16兩, 1兩 = 24銖
一斤價值 = 345  # in qian
一斤重量 = 16  # in liang
一兩重量 = 24  # in zhu

# 絲重量 = 7兩1十二銖
絲重量 = 7 + Fraction(12, 一兩重量)  # Convert to liang

# 每兩價值
每兩價值 = Fraction(一斤價值, 一斤重量)

# 絲價值
a = 絲重量 * 每兩價值  # in qian

a#----- content ends here -----

"""
"""
