"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a(=15) 車， b(=39)人 。
"""

#----- content starts here -----
"""
Suppose there are three people sharing a cart, leaving two carts empty.
When two people share a cart, nine people walk.
Question: how many people and carts are there?

The procedure says: Place 2 people and multiply by 3, obtaining 6.
Add the 9 people walking, obtaining 15 carts.
To find the number of people, multiply the carts by 2, then add the 9 people walking.

Answer: *a*(=15) carts, *b*(=39) people.
"""

# 三人共車，二車空
三人共車 = 3
二車空 = 2

# 二人共車，九人步
二人共車 = 2
九人步 = 9

# 置二人以三乘之，得六
兩人乘三 = 2 * 3

# 加步者九人，得車一十五
車 = 兩人乘三 + 九人步

# 欲知人者，以二乘車，加九人即得
人 = 2 * 車 + 九人步

a = 車  # 15 carts
b = 人  # 39 people#----- content ends here -----

"""
"""
