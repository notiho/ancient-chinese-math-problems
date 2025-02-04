"""
今有米一萬三千四百六十四斛五斗毎斗糶錢一百二十文問錢幾何
術曰先置米數二六因之即得
答曰 a貫
"""

"""
Suppose there are 13,464 hu and 5 dou of rice. Each dou sells for 120 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 26, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 米一萬三千四百六十四斛五斗
米數 = 13464 + Fraction(5, 10)  # Convert 5 dou to hu (1 hu = 10 dou)

# 每斗糶錢一百二十文
每斗錢 = 120

# 每斛有10斗，因此每斛的錢數為：
每斛錢 = 每斗錢 * 10

# 術曰先置米數，二六因之即得
總錢數 = 米數 * 26  # 每斛錢數 (120 * 10 = 1200) / 46 simplifies to multiplying 米數 by 26

# Convert to 貫 (1 貫 = 1000 文)
a = Fraction(總錢數, 1000)  # Convert total wen to guan
"""
Variable 'a' has wrong value. Expected: 80787/5, Actual: 350077/1000"""
