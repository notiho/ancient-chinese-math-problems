"""
今有兵三千八百三十七人人給錢五百五十六文問計㡬何
術曰列兵三千八百三十七人以五百五十六文乘之即得
答曰 a貫 
"""

"""
Suppose there are 3837 soldiers, and each is given 556 wen.
Question: what is the total amount?

The procedure says: Place the 3837 soldiers, multiply it by 556 wen, and the result is obtained.

The answer says: *a* guan.
"""

# 兵三千八百三十七人
兵 = 3837

# 每人給錢五百五十六文
每人錢 = 556

# 以五百五十六文乘之，即得
總錢文 = 兵 * 每人錢

# 1貫 = 1000文
a = Fraction(總錢文, 1000)
"""
"""
