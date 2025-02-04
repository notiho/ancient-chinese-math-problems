"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square-based frustum (a truncated pyramid) with the following dimensions:
- The bottom square has a side length of 5 zhang.
- The top square has a side length of 4 zhang.
- The height of the frustum is 5 zhang.

Question: What is the volume of the frustum?

Answer: The volume is *a* cubic chi.
"""

# Dimensions of the frustum
下方邊長 = 5  # in zhang
上方邊長 = 4  # in zhang
高 = 5  # in zhang

# Convert all dimensions to chi (1 zhang = 10 chi)
下方邊長 *= 10
上方邊長 *= 10
高 *= 10

# Formula for the volume of a square-based frustum:
# V = (1/3) * 高 * (下方面積 + 上方面積 + sqrt(下方面積 * 上方面積))
下方面積 = 下方邊長**2
上方面積 = 上方邊長**2

# Calculate the volume
a = Fraction(1, 3) * 高 * (下方面積 + 上方面積 + (下方面積 * 上方面積)**0.5)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 101666.66666666667"""
