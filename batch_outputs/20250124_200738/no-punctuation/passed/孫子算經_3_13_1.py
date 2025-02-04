"""
今有三人共車二車空二人共車九人步問人與車各幾何
術曰置二人以三乘之得六加步者九人得車一十五欲知人者以二乘車加九人即得
答曰 a 車 b人 
"""

#----- content starts here -----
"""
Suppose there are three people sharing two carts, leaving two people sharing one cart, and nine people walking.
Question: how many carts and how many people are there in total?

The procedure says: Place the two people and multiply by three, obtaining six. Add the nine people walking, obtaining fifteen carts.
To know the number of people, multiply the number of carts by two, then add the nine people walking, obtaining the total.

Answer: *a* carts and *b* people.
"""

# 二人共車
二人 = 2

# 三乘之得六
六 = 3 * 二人

# 加步者九人
步者 = 9
車 = 六 + 步者

# 以二乘車
人 = 2 * 車

# 加九人即得
人 += 步者

a = 車
b = 人#----- content ends here -----

"""
"""
