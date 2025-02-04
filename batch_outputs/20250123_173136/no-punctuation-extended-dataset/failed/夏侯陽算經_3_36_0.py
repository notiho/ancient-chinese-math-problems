"""
今有米三千四百六十三斛四斗四升七合一勺毎斗身内抽三合充腳問正腳各幾何
術曰先置米數以一斗三合除之得正米以三因之得腳米
答曰正 a斛 腳 b斛
"""

"""
Suppose there are 3463 hu, 4 dou, 4 sheng, 7 ge, and 1 jue of rice. 
For every dou, 3 ge are taken out as "foot rice" (extra rice). 
Question: how much is the "correct rice" and how much is the "foot rice"?

The procedure says: First, place the total amount of rice. 
Divide it by 1 dou and 3 ge to obtain the correct rice. 
Multiply it by 3 to obtain the foot rice.

Answer: the correct rice is *a* hu, and the foot rice is *b* hu.
"""

from fractions import Fraction

# 米三千四百六十三斛四斗四升七合一勺
米數 = (
    3463  # 斛
    + Fraction(4, 10)  # 斗 (1 斗 = 1/10 斛)
    + Fraction(4, 100)  # 升 (1 升 = 1/100 斛)
    + Fraction(7, 1000)  # 合 (1 合 = 1/1000 斛)
    + Fraction(1, 10000)  # 勺 (1 勺 = 1/10000 斛)
)

# 每斗身內抽三合充腳
# 1 斗 3 合 = 1 斗 + 3 合 = 1/10 斛 + 3/1000 斛
一斗三合 = Fraction(1, 10) + Fraction(3, 1000)

# 以一斗三合除之，得正米
正米 = 米數 / 一斗三合

# 以三因之，得腳米
腳米 = 正米 * 3

# 答曰正 a斛，腳 b斛
a = 正米
b = 腳米
"""
Variable 'a' has wrong value. Expected: 336257/100, Actual: 336257/10
Variable 'b' has wrong value. Expected: 1008771/10000, Actual: 1008771/10"""
