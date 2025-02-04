"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a valley with the following dimensions:
- Upper width: 2 zhang
- Upper length: 7 zhang
- Lower width: 8 chi
- Lower length: 4 zhang
- Depth: 6 zhang 5 chi

Question: What is the volume of the valley?

Answer: The volume is *a* cubic chi.
"""

# Convert all dimensions to chi (1 zhang = 10 chi)
上廣 = 2 * 10  # Upper width in chi
上袤 = 7 * 10  # Upper length in chi
下廣 = 8       # Lower width in chi
下袤 = 4 * 10  # Lower length in chi
深 = 6 * 10 + 5  # Depth in chi

# Calculate the average width and length
平均廣 = (上廣 + 下廣) / 2
平均袤 = (上袤 + 下袤) / 2

# Calculate the volume
a = 平均廣 * 平均袤 * 深

a  # The volume in cubic chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 52000, Actual: 50050.0"""
