"""
今有米三千四百六十三斛四斗四升七合一勺毎斗身内抽三合充腳問正腳各幾何
術曰先置米數以一斗三合除之得正米以三因之得腳米
答曰正 a斛 腳 b斛
"""

"""
Suppose there are 3463 hu, 4 dou, 4 sheng, 7 ge, and 1 jue of rice.
For every dou, 3 ge are taken out to form the "foot rice" (additional rice).
Question: how much is the "correct rice" and how much is the "foot rice"?

The procedure says: First, place the total amount of rice.
Divide it by 1 dou and 3 ge, obtaining the "correct rice."
Multiply it by 3, obtaining the "foot rice."

Answer: the correct rice is *a* hu, and the foot rice is *b* hu.
"""

from fractions import Fraction

# 米數：3463斛4斗4升7合1勺
米數 = (
    3463  # 斛
    + Fraction(4, 10)  # 斗 (1斗 = 1/10斛)
    + Fraction(4, 100)  # 升 (1升 = 1/100斛)
    + Fraction(7, 1000)  # 合 (1合 = 1/1000斛)
    + Fraction(1, 10000)  # 勺 (1勺 = 1/10000斛)
)

# 每斗抽3合，1斗3合 = 1/10斛 + 3/1000斛
一斗三合 = Fraction(1, 10) + Fraction(3, 1000)

# 以米數除以1斗3合，得正米
正米 = 米數 / 一斗三合

# 以正米乘3，得腳米
腳米 = 正米 * 3

# 答案
a = 正米
b = 腳米
"""
Variable 'a' has wrong value. Expected: 336257/100, Actual: 336257/10
Variable 'b' has wrong value. Expected: 1008771/10000, Actual: 1008771/10"""
