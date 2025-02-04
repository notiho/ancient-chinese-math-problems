"""
今有小麥五萬六千四百七十三斛五斗毎斗造麴五斤問麴幾何
術曰先置麥數從下五因之即得
答曰 a斤
"""

"""
Suppose there are 56,473 hu and 5 dou of wheat. Each dou is used to make 5 jin of malt.
Question: how much malt is made?

The procedure says: First, place the amount of wheat. Multiply it by 5 from below, and the result is obtained.

Answer: *a* jin.
"""

# 小麥五萬六千四百七十三斛五斗
小麥斛 = 56473
小麥斗 = 5

# 每斛有10斗
總斗數 = (小麥斛 * 10) + 小麥斗

# 每斗造麴五斤
每斗麴 = 5

# 先置麥數，從下五因之，即得
a = 總斗數 * 每斗麴
"""
"""
