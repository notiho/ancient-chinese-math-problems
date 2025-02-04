"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
荅曰： a丈 。
"""

"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It can hold 10,000 hu of grain.
Question: how high is the granary?

Answer: the height is *a* zhang.
"""

# 倉廣三丈
廣 = 3  # in zhang

# 袤四丈五尺 (convert 4 zhang 5 chi into zhang)
袤 = 4 + Fraction(5, 10)  # 5 chi = 0.5 zhang

# 容粟一萬斛
容積 = 10000  # in hu

# The formula for volume is: 容積 = 廣 × 袤 × 高
# Rearrange to find 高 (height): 高 = 容積 / (廣 × 袤)
a = Fraction(容積, 廣 * 袤)

# The height `a` is in zhang.
"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
