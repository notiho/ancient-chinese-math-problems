"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a circular fort with a circumference of 4 zhang 8 chi and a height of 1 zhang 1 chi.
Question: what is the volume of the fort?

Answer: the volume is *a* cubic chi.
"""

# 周四丈八尺 (circumference = 4 zhang 8 chi)
周 = 4 * 10 + 8  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈一尺 (height = 1 zhang 1 chi)
高 = 1 * 10 + 1  # Convert zhang to chi

# 圓的直徑 = 周 / π (approximate π as 3)
直徑 = Fraction(周, 3)

# 圓的半徑 = 直徑 / 2
半徑 = Fraction(直徑, 2)

# 圓的面積 = π * 半徑^2 (approximate π as 3)
圓面積 = 3 * 半徑 * 半徑

# 積 (volume) = 圓的面積 * 高
a = 圓面積 * 高

a  # The volume in cubic chi
"""
"""
