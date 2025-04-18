"""
今有粟二千三百七十四斛斛加三升問共粟幾何
術曰置粟二千三百七十四斛以一斛三升乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 2374 hu of millet, and each hu has an additional 3 sheng.
Question: how much millet is there in total?

The procedure says: Place the 2374 hu of millet.
Multiply it by 1 hu and 3 sheng, and the result is obtained.

Answer: *a* hu.
"""

# 粟二千三百七十四斛
粟 = 2374

# 一斛加三升 (1 hu = 1 + 3/10 hu, since 10 sheng = 1 hu)
一斛三升 = 1 + Fraction(3, 10)

# 以一斛三升乘之
總粟 = 粟 * 一斛三升

# 答案
a = 總粟#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
