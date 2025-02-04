"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

#----- content starts here -----
"""
Suppose there are three people sharing a cart, and two carts are empty.
If two people share a cart, nine people are walking.
Question: how many people and carts are there?

The procedure says: Take 2 people and multiply by 3, obtaining 6. Add the 9 people walking, obtaining 15 carts.
To find the number of people, multiply the number of carts by 2, then add 9 people.

Answer: *a* carts, *b* people.
"""

# Step 1: Calculate the number of carts
# 置二人以三乘之，得六，加步者九人，得車一十五
步者 = 9
車 = 2 * 3 + 步者

# Step 2: Calculate the number of people
# 欲知人者，以二乘車，加九人即得
人 = 2 * 車 + 步者

# Final answer
a = 車
b = 人#----- content ends here -----

"""
"""
