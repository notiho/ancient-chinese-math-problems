"""
今有兵三千四百八十五人毎人賜絹一丈三尺問絹幾何
術曰先置人數添三得丈數以四為法除之得匹
答曰 a匹
"""

"""
Suppose there are 3485 soldiers, and each soldier is given 1 zhang and 3 chi of silk.
Question: how much silk is needed in total?

The procedure says: First, place the number of people. Add 3 [chi] to get the total zhang count.
Divide by 4 (as 1 zhang = 10 chi, and 1 bolt of silk = 40 chi) to get the number of bolts.

Answer: *a* bolts.
"""

# 兵三千四百八十五人
人數 = 3485

# 每人賜絹一丈三尺
每人絹 = 1 * 10 + 3  # Convert 1 zhang and 3 chi to chi (1 zhang = 10 chi)

# 先置人數，添三得丈數
總絹尺 = 每人絹 * 人數

# 以四為法除之，得匹
法 = 40  # 1 bolt = 40 chi
a = Fraction(總絹尺, 法)
"""
"""
