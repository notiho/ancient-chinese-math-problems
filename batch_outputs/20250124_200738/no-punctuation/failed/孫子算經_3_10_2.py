"""
今有粟二千三百七十四斛斛加三升問共粟幾何
術曰置粟二千三百七十四斛以一斛三升乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 2374 hu of millet, with each hu increased by 3 sheng.
Question: how much millet is there in total?

The procedure says: Place the 2374 hu of millet.
Multiply it by 1 hu and 3 sheng, and the result is obtained.

Answer: *a* hu.
"""

# 粟二千三百七十四斛
粟 = 2374

# 一斛加三升
一斛 = 1
三升 = Fraction(3, 10)  # 1 hu = 10 sheng
每斛增加 = 一斛 + 三升

# 以一斛三升乘之
總粟 = 粟 * 每斛增加

# 答案
a = 總粟#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
