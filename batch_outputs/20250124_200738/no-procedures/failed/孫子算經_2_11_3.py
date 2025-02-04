"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular pit with a circumference of 5 zhang 4 chi and a depth of 1 zhang 8 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu of millet.
"""

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang and chi to total chi

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang and chi to total chi

# The formula for the volume of a circular pit is:
# V = (C^2 * D) / (4 * π), where C is the circumference and D is the depth.
# For simplicity, ancient Chinese calculations approximate π as 3.

# Calculate the volume in cubic chi
體積 = (周 ** 2 * 深) / (4 * 3)

# Convert cubic chi to hu (1 hu = 1000 cubic chi)
a = Fraction(體積, 1000)  # Result in hu#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
