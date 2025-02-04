"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a wall with the following dimensions:
- Bottom width: 4 zhang
- Top width: 2 zhang
- Height: 5 zhang
- Length: 126 zhang and 5 chi (convert to chi for calculation)

Question: What is the total volume of the wall?

Answer: The volume is *a* chi³.
"""

# 城下廣四丈 (bottom width in chi)
bottom_width = 4 * 10  # 1 zhang = 10 chi

# 上廣二丈 (top width in chi)
top_width = 2 * 10  # 1 zhang = 10 chi

# 高五丈 (height in chi)
height = 5 * 10  # 1 zhang = 10 chi

# 袤一百二十六丈五尺 (length in chi)
length = 126 * 10 + 5  # 1 zhang = 10 chi

# The formula for the volume of a trapezoidal prism is:
# Volume = (1/2) * (bottom_width + top_width) * height * length
a = Fraction(1, 2) * (bottom_width + top_width) * height * length

# Result: a is the total volume in chi³
a
"""
"""
