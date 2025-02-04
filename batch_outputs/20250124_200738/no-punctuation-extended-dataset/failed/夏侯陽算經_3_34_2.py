"""
今有米一萬三千四百六十五斛四斗三升毎斗糶錢一百三十五文問錢幾何
術曰先置米數三九因之折半即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 13,465 hu, 4 dou, and 3 sheng of rice. Each dou sells for 135 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 135. Divide by 2, and then divide by 1,000 to convert to guan (strings of cash).

Answer: *a* guan.
"""

from fractions import Fraction

# 米數：一萬三千四百六十五斛四斗三升
米_斛 = 13465
米_斗 = 4
米_升 = 3

# 每斛有10斗，每斗有10升
總斗數 = 米_斛 * 10 + 米_斗 + Fraction(米_升, 10)

# 每斗糶錢一百三十五文
每斗錢 = 135

# 先置米數，三九因之
總錢數 = 總斗數 * 每斗錢

# 折半
總錢數 = 總錢數 / 2

# 以千為一貫
a = Fraction(總錢數, 1000)  # 答曰 a貫#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36356661/2000, Actual: 36356661/4000"""
