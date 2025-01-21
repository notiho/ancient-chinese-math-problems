"""
今有米一萬三千四百六十五斛四斗三升毎斗糶錢一百三十五文問錢幾何
術曰先置米數三九因之折半即得
答曰 a貫
"""

"""
Suppose there are 13,465 hu, 4 dou, and 3 sheng of rice. Each dou is sold for 135 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 39, then divide it in half, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 米數：一萬三千四百六十五斛四斗三升
米_斛 = 13465
米_斗 = 4
米_升 = 3

# 每斛有10斗，每斗有10升
總米數_斗 = 米_斛 * 10 + 米_斗 + Fraction(米_升, 10)

# 每斗糶錢一百三十五文
每斗價錢 = 135

# 置米數，三九因之
總價錢_文 = 總米數_斗 * 39

# 折半即得
總價錢_貫 = Fraction(總價錢_文, 2)

a = 總價錢_貫
"""
Variable 'a' has wrong value. Expected: 36356661/2000, Actual: 52515177/20"""
