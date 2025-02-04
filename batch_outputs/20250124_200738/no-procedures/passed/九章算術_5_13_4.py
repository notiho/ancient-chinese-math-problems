"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular fort with a circumference of 4 zhang and 8 chi, and a height of 1 zhang and 1 chi.
Question: what is the volume of the fort?

Answer: the volume is *a* cubic chi.
"""

# 周四丈八尺
周 = 4 * 10 + 8  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈一尺
高 = 1 * 10 + 1  # Convert zhang to chi (1 zhang = 10 chi)

# The formula for the volume of a cylinder is: V = (C^2) / (4π) * H
# In ancient Chinese math, π is approximated as 3.

# Calculate the radius (r = C / (2π), where π = 3)
半徑 = 周 / (2 * 3)

# Calculate the area of the base (A = π * r^2, where π = 3)
底面積 = 3 * 半徑 * 半徑

# Calculate the volume (V = A * H)
a = 底面積 * 高

a  # The volume in cubic chi#----- content ends here -----

"""
"""
