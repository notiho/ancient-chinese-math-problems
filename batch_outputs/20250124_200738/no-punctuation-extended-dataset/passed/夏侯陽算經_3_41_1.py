"""
今有兵三千四百八十五人毎人賜絹一丈三尺問絹幾何
術曰先置人數添三得丈數以四為法除之得匹
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 3485 soldiers, and each soldier is given 1 zhang and 3 chi of silk.
Question: how much silk is needed in total?

The procedure says: First, place the number of people. Add 3 to obtain the number of zhang.
Divide by 4 (the divisor) to obtain the number of bolts of silk.

Answer: *a* bolts.
"""

# 兵三千四百八十五人
兵 = 3485

# 每人賜絹一丈三尺
每人丈 = 1
每人尺 = 3

# 先置人數添三得丈數
總丈數 = 兵 * (每人丈 + Fraction(每人尺, 10))

# 以四為法除之得匹
法 = 4
a = Fraction(總丈數, 法)#----- content ends here -----

"""
"""
