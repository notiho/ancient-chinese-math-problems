"""
今有三人共車二車空二人共車九人步問人與車各幾何
術曰置二人以三乘之得六加步者九人得車一十五欲知人者以二乘車加九人即得
答曰 a 車 b人 
"""

#----- content starts here -----
"""
Suppose there are three people sharing two carts, and two people sharing one cart, with nine people walking.
Question: how many carts and people are there in total?

The procedure says: Place the two people and multiply by three, obtaining six.
Add the nine people walking, obtaining fifteen carts.
To find the number of people, multiply the carts by two and add the nine people walking, obtaining the total.

Answer: *a* carts and *b* people.
"""

# 三人共車二車
三人共車 = 2

# 空二人共車
二人共車 = 1

# 九人步
步人 = 9

# 置二人以三乘之，得六
二人乘三 = 2 * 3

# 加步者九人，得車一十五
總車 = 二人乘三 + 步人

# 欲知人者，以二乘車，加九人，即得
總人 = (總車 * 2) + 步人

a = 總車
b = 總人#----- content ends here -----

"""
"""
