"""
今有米一萬三千四百六十四斛五斗毎斗糶錢一百二十文問錢幾何
術曰先置米數二六因之即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 13,464 hu and 5 dou of rice. Each dou is sold for 120 wen.
Question: how much money is obtained?

The procedure says: First, place the amount of rice. Multiply it by 26, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 米一萬三千四百六十四斛五斗
米數_斛 = 13464
米數_斗 = 5

# Convert the total rice to dou (1 hu = 10 dou)
總米數_斗 = 米數_斛 * 10 + 米數_斗

# 每斗糶錢一百二十文
每斗錢 = 120

# 先置米數，二六因之即得
總錢文 = 總米數_斗 * 每斗錢

# Convert to 貫 (1 貫 = 1000 文)
a = Fraction(總錢文, 1000)#----- content ends here -----

"""
"""
