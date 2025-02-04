"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

#----- content starts here -----
"""
Suppose there are three people sharing a cart, leaving two carts empty. When two people share a cart, nine people are walking.
Question: how many people and carts are there?

The procedure says: Place the two people and multiply by three, obtaining six. Add the nine people walking, obtaining fifteen carts.
To find the number of people, multiply the carts by two, and add the nine people walking.

Answer: *a* carts, *b* people.
"""

# 置二人以三乘之，得六
兩人 = 2
三乘 = 3
六 = 兩人 * 三乘

# 加步者九人，得車一十五
步者 = 9
車 = 六 + 步者

# 欲知人者，以二乘車，加九人即得
a = 車
b = 2 * 車 + 步者#----- content ends here -----

"""
"""
