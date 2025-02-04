"""
今有三人共車二車空二人共車九人步問人與車各幾何
術曰置二人以三乘之得六加步者九人得車一十五欲知人者以二乘車加九人即得
答曰 a 車 b人 
"""

#----- content starts here -----
"""
Suppose there are three people sharing two carts, and two people sharing one cart, while nine people walk.
Question: how many carts and people are there in total?

The procedure says: Place the two people and multiply by three, obtaining six. Add the nine walking people, obtaining fifteen carts.
To find the number of people, multiply the carts by two and add the nine walking people.

Answer: *a* carts and *b* people.
"""

# 二人共車
二人 = 2

# 三人共車
三人 = 3

# 空二人共車九人步
步人 = 9

# 置二人以三乘之，得六
車數 = 3 * 二人

# 加步者九人，得車一十五
車數 += 步人

# 欲知人者，以二乘車
總人數 = 2 * 車數

# 加九人，即得
總人數 += 步人

a = 車數
b = 總人數#----- content ends here -----

"""
"""
