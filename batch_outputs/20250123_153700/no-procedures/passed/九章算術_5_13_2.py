"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a circular embankment with a circumference of 4 zhang 8 chi and a height of 1 zhang 1 chi.
Question: what is the volume of the embankment?

Answer: it is *a* cubic chi.
"""

# 周四丈八尺 (circumference = 4 zhang 8 chi)
周 = 4 * 10 + 8  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈一尺 (height = 1 zhang 1 chi)
高 = 1 * 10 + 1  # Convert zhang to chi

# Formula for the volume of a cylinder: V = (C^2 / (4π)) * H
# Ancient Chinese approximation for π is 3, so the formula becomes: V = (C^2 / 12) * H

積 = Fraction(周**2, 12) * 高  # Volume in cubic chi

a = 積  # The volume of the embankment in cubic chi

# Output the result
a
"""
"""
