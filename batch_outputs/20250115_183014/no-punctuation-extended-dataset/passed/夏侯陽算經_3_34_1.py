"""
今有米一萬三千四百六十五斛四斗三升毎斗糶錢一百三十五文問錢幾何
術曰先置米數三九因之折半即得
答曰 a貫
"""

"""
Suppose there are 13,465 hu, 4 dou, and 3 sheng of rice. 
Each dou is sold for 135 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 39, then divide it by 2, and the result is obtained.

The answer says: *a* guan.
"""

from fractions import Fraction

# 米一萬三千四百六十五斛四斗三升
米斛 = 13465
米斗 = 4
米升 = 3

# Convert everything to dou (1 hu = 10 dou, 1 dou = 10 sheng)
總米斗 = 米斛 * 10 + 米斗 + Fraction(米升, 10)

# 每斗糶錢一百三十五文
每斗錢 = 135

# 先置米數，三九因之
總錢文 = 總米斗 * 每斗錢

# 折半即得
總錢貫 = Fraction(總錢文, 1000)  # 1 貫 = 1000 文

a = 總錢貫
"""
"""
