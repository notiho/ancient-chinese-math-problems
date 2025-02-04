"""
今有米一萬三千四百六十五斛四斗三升毎斗糶錢一百三十五文問錢幾何
術曰先置米數三九因之折半即得
答曰 a貫
"""

"""
Suppose there are 13,465 hu, 4 dou, and 3 sheng of rice. Each dou is sold for 135 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 39 and then halve it to obtain the result.

Answer: *a* guan.
"""

from fractions import Fraction

# 米一萬三千四百六十五斛四斗三升
米_斛 = 13465
米_斗 = 4
米_升 = 3

# 每斗糶錢一百三十五文
每斗錢 = 135

# Convert 米 to total 斗
# 1 斛 = 10 斗, 1 斗 = 10 升
總斗數 = 米_斛 * 10 + 米_斗 + Fraction(米_升, 10)

# 先置米數，三九因之
總錢數 = 總斗數 * 39

# 折半即得
總錢數 = 總錢數 / 2

# Convert 文 to 貫 (1 貫 = 1000 文)
a = Fraction(總錢數, 1000)  # Answer in 貫
"""
Variable 'a' has wrong value. Expected: 36356661/2000, Actual: 52515177/20000"""
