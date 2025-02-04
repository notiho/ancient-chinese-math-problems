"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""

"""


from fractions import Fraction

# 倉廣三丈
廣 = 3

# 袤四丈五尺 (convert to 丈, 1 丈 = 10 尺)
袤 = 4 + Fraction(5, 10)

# 容粟一萬斛
粟 = 10000

# 置粟一萬斛積尺為實 (1 斛 = 10 尺³)
實 = 10 * 粟

# 廣袤相乘為法
法 = 廣 * 袤

# 實如法而一，得高尺
高 = Fraction(實, 法)

# Convert 高 from 尺 to 丈 (1 丈 = 10 尺)
a = Fraction(高, 10)


"""

"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
