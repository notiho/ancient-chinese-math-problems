"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square-based frustum (a truncated pyramid) with the following dimensions:
- Bottom side length: 5 zhang
- Top side length: 4 zhang
- Height: 5 zhang

Question: What is the volume of the frustum?

Answer: *a* cubic chi.
"""

# Dimensions
下方 = 5  # Bottom side length in zhang
上方 = 4  # Top side length in zhang
高 = 5    # Height in zhang

# Convert zhang to chi (1 zhang = 10 chi)
下方 = 下方 * 10
上方 = 上方 * 10
高 = 高 * 10

# Volume of a frustum formula: V = (1/3) * 高 * (底面積 + 頂面積 + sqrt(底面積 * 頂面積))
底面積 = 下方 * 下方
頂面積 = 上方 * 上方

# Calculate the volume
a = Fraction(1, 3) * 高 * (底面積 + 頂面積 + (底面積 * 頂面積) ** 0.5)  # Volume in cubic chi

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 101666.66666666667"""
