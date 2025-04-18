"""
今有粟二千三百七十四斛斛加三升問共粟幾何
術曰置粟二千三百七十四斛以一斛三升乘之即得
答曰 a斛 
"""

"""
Suppose there are 2374 hu of millet, and each hu is increased by 3 sheng.
Question: how much millet is there in total?

The procedure says: Place the millet as 2374 hu. Multiply it by 1 hu and 3 sheng, and the result is obtained.

Answer: *a* hu.
"""

# 粟二千三百七十四斛
粟 = 2374

# 一斛加三升 (convert 3升 to hu, as 1 hu = 10升)
一斛三升 = 1 + Fraction(3, 10)

# 以一斛三升乘之
a = 粟 * 一斛三升
"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
