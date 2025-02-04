"""
今有米一萬三千四百六十五斛四斗三升毎斗糶錢一百三十五文問錢幾何
術曰先置米數三九因之折半即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 13,465 hu, 4 dou, and 3 sheng of rice. 
Each dou is sold for 135 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 39 and then halve it, obtaining the result.

Answer: *a* guan (strings of 1,000 wen).
"""

from fractions import Fraction

# 米一萬三千四百六十五斛四斗三升
米_斛 = 13465
米_斗 = 4
米_升 = 3

# Convert everything to dou (1 hu = 10 dou, 1 dou = 10 sheng)
總米斗 = 米_斛 * 10 + 米_斗 + Fraction(米_升, 10)

# 每斗糶錢一百三十五文
每斗錢 = 135

# 先置米數，三九因之
總錢 = 總米斗 * 39

# 折半即得
總錢 = 總錢 / 2

# Convert to 貫 (1 貫 = 1000 文)
a = Fraction(總錢, 1000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36356661/2000, Actual: 52515177/20000"""
