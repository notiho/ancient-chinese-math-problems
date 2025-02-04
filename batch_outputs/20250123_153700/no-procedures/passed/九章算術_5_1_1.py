"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a city wall with the following dimensions:
- Bottom width: 4 zhang
- Top width: 2 zhang
- Height: 5 zhang
- Length: 126 zhang and 5 chi

Question: What is the total volume of the wall?

Answer: The volume is *a* cubic chi.
"""

# 城下廣 (bottom width) = 4 丈
bottom_width = 4 * 10  # Convert to chi

# 城上廣 (top width) = 2 丈
top_width = 2 * 10  # Convert to chi

# 高 (height) = 5 丈
height = 5 * 10  # Convert to chi

# 袤 (length) = 126 丈 5 尺
length = 126 * 10 + 5  # Convert to chi

# Average width = (bottom width + top width) / 2
average_width = (bottom_width + top_width) / 2

# Volume = Average width * height * length
a = average_width * height * length

a  # The total volume in cubic chi
"""
"""
