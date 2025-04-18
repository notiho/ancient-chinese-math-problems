"""
今有兵三千四百八十五人毎人賜絹一丈三尺問絹幾何
術曰先置人數添三得丈數以四為法除之得匹
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 3485 soldiers. Each soldier is rewarded with 1 zhang and 3 chi of silk.
Question: how many bolts of silk are required?

The procedure says: First, place the number of people. Add 3 [chi per person] to get the total zhang.
Divide by 4 (since 1 bolt = 4 zhang) to obtain the number of bolts.

Answer: *a* bolts.
"""

# 兵三千四百八十五人
人數 = 3485

# 每人賜絹一丈三尺
每人絹 = 1 + Fraction(3, 10)  # 1丈3尺 = 1 + 3/10丈

# 先置人數添三得丈數
總丈數 = 人數 * 每人絹

# 以四為法除之得匹
法 = 4
a = Fraction(總丈數, 法)#----- content ends here -----

"""
"""
