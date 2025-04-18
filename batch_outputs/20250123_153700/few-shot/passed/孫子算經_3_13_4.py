"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

"""
Suppose there are three people sharing a cart, leaving two carts empty. 
If two people share a cart, nine people are left walking.
Question: how many people and carts are there?

The procedure says: Place 2 people and multiply by 3, obtaining 6. 
Add the 9 people walking, obtaining 15 carts. 
To find the number of people, multiply the carts by 2, then add the 9 walking people.

Answer: *a* carts, *b* people.
"""

# 置二人以三乘之，得六
二人 = 2
三 = 3
六 = 二人 * 三

# 加步者九人，得車一十五
步者 = 9
車 = 六 + 步者

# 欲知人者，以二乘車
人 = 2 * 車

# 加九人即得
人 += 步者

a = 車
b = 人
"""
"""
