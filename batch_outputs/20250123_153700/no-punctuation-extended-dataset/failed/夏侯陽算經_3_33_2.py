"""
今有米一萬三千四百六十四斛五斗毎斗糶錢一百二十文問錢幾何
術曰先置米數二六因之即得
答曰 a貫
"""

"""
Suppose there are 13,464 hu and 5 dou of rice. Each dou is sold for 120 wen.
Question: how much money is obtained?

The procedure says: First place the amount of rice. Multiply it by 26, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 米一萬三千四百六十四斛五斗
米數 = 13464 + Fraction(5, 10)  # Convert 5 dou to hu (1 hu = 10 dou)

# 每斗糶錢一百二十文
每斗錢 = 120

# 每斛有10斗，計算每斛的錢
每斛錢 = 每斗錢 * 10

# 術曰先置米數，二六因之即得
總錢文 = 米數 * 26  # 因為 120文/斗 = 26貫/斛

# 答曰 a貫
a = 總錢文  # 單位為貫
"""
Variable 'a' has wrong value. Expected: 80787/5, Actual: 350077"""
