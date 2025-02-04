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
# Ancient Chinese math approximates π as 3, so the formula becomes: V = (C^2) / 12 * H

# Calculate the volume
a = Fraction(周**2, 12) * 高  # Volume in cubic chi

a  # Output the result#----- content ends here -----

"""
"""
