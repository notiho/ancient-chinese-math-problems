"""
今有米三千四百五十六斛毎斗身内抽二升充腳問正腳各幾何
術曰先置米數去二得正米以二因退位得腳米
答曰正 a斛 腳 b斛
"""

"""
Suppose there are 3456 hu of rice. For every dou, 2 sheng are taken out for the "foot" (supporting portion).
Question: how much is the "correct" rice and how much is the "foot" rice?

The procedure says: First, place the total amount of rice. Remove 2 [sheng per dou] to obtain the correct rice.
Use 2 as a factor to calculate the "foot" rice by backward calculation.

Answer: the correct rice is *a* hu, and the "foot" rice is *b* hu.
"""

# 米三千四百五十六斛
總米 = 3456

# 每斛有10斗，每斗有10升
每斛斗數 = 10
每斗升數 = 10

# 每斗身內抽二升充腳
抽升 = 2

# 每斛抽出的升數
每斛抽升 = 每斛斗數 * 抽升

# 每斛剩下的正米升數
每斛正升 = 每斛斗數 * 每斗升數 - 每斛抽升

# 先置米數，去二得正米
正米 = Fraction(每斛正升, 每斛斗數 * 每斗升數) * 總米

# 以二因退位得腳米
腳米 = 總米 - 正米

a = 正米
b = 腳米
"""
Variable 'a' has wrong value. Expected: 2288, Actual: 13824/5
Variable 'b' has wrong value. Expected: 576, Actual: 3456/5"""
