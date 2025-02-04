"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a haystack (芻童) with the following dimensions:
- Bottom width: 2 zhang
- Bottom length: 3 zhang
- Top width: 3 zhang
- Top length: 4 zhang
- Height: 3 zhang

Question: What is the volume of the haystack?

Answer: The volume is *a* cubic chi.
"""

# Dimensions of the haystack
下廣 = 2  # Bottom width in zhang
下袤 = 3  # Bottom length in zhang
上廣 = 3  # Top width in zhang
上袤 = 4  # Top length in zhang
高 = 3    # Height in zhang

# Convert all dimensions from zhang to chi (1 zhang = 10 chi)
下廣 *= 10
下袤 *= 10
上廣 *= 10
上袤 *= 10
高 *= 10

# Calculate the average base area (top and bottom)
平均底面積 = Fraction((下廣 * 下袤) + (上廣 * 上袤), 2)

# Calculate the volume of the haystack
a = 平均底面積 * 高

a  # The volume in cubic chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 27000"""
