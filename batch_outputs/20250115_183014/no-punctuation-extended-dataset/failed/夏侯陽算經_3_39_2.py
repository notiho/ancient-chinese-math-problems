"""
今有米三千四百五十六斛毎斗身内抽二升充腳問正腳各幾何
術曰先置米數去二得正米以二因退位得腳米
答曰正 a斛 腳 b斛
"""

"""
Suppose there are 3456 hu of rice. For every dou, 2 sheng are taken out for the "foot" (supporting portion).
Question: how much is the "proper" rice and how much is the "foot" rice?

The procedure says: First, place the total amount of rice. Remove 2 [sheng per dou] to obtain the proper rice.
Use 2 as the factor to calculate the "foot" rice by reversing the position.

Answer: the proper rice is *a* hu, and the "foot" rice is *b* hu.
"""

from fractions import Fraction

# 米三千四百五十六斛
總米 = 3456

# 每斗身內抽二升充腳
每斗抽升 = 2

# 1斛 = 10斗, 1斗 = 10升
每斛抽升 = 每斗抽升 * 10

# 先置米數，去二得正米
正米 = 總米 * (10 - Fraction(每斛抽升, 10)) / 10

# 以二因退位得腳米
腳米 = 總米 - 正米

a = 正米
b = 腳米
"""
Variable 'a' has wrong value. Expected: 2288, Actual: 13824/5
Variable 'b' has wrong value. Expected: 576, Actual: 3456/5"""
