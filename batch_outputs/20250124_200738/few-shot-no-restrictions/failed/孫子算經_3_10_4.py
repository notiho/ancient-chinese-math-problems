"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
術曰：置粟二千三百七十四斛，以一斛三升乘之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is millet, 2374 hu, with each hu increased by 3 sheng.
Question: what is the total amount of millet?

The procedure says: Place the millet as 2374 hu. Multiply it by 1 hu and 3 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 每斛加三升
一斛 = 1  # 1 hu
三升 = Fraction(3, 10)  # 3 sheng = 3/10 hu

# 每斛的總量
每斛總量 = 一斛 + 三升

# 以一斛三升乘之
總粟 = 粟 * 每斛總量

# 答案
a = 總粟

print(f"答曰：共粟 {a} 斛。")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
