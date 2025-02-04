"""
今有三人共車二車空二人共車九人步問人與車各幾何
術曰置二人以三乘之得六加步者九人得車一十五欲知人者以二乘車加九人即得
答曰 a 車 b人 
"""

"""
Suppose there are three people sharing two carts, leaving two people sharing one cart, and nine people walking.
Question: how many carts and how many people are there in total?

The procedure says: Place the two people and multiply by three, obtaining six.
Add the nine people walking, obtaining fifteen carts.
To find the number of people, multiply the carts by two and add the nine people walking.

Answer: *a* carts and *b* people.
"""

# 二人共車
二人 = 2

# 三人共車二車
三人 = 3
車 = 2

# 空二人共車九人步
步行人 = 9

# 置二人以三乘之，得六
六 = 二人 * 3

# 加步者九人，得車一十五
總車 = 六 + 步行人

# 欲知人者，以二乘車，加九人，即得
總人 = 2 * 總車 + 步行人

a = 總車
b = 總人
"""
"""
