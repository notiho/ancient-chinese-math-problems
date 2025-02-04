"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
術曰：置粟二千三百七十四斛，以一斛三升乘之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is millet, 2374 hu, and each hu is increased by 3 sheng.
Question: what is the total amount of millet?

The procedure says: Place the millet, 2374 hu, and multiply it by 1 hu and 3 sheng. This gives the total.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 斛加三升 (1 hu = 10 sheng, so 1 hu + 3 sheng = 1 + 3/10 hu)
每斛增加 = 1 + Fraction(3, 10)

# 以一斛三升乘之，即得
總粟 = 粟 * 每斛增加

# 答案
a = 總粟
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
