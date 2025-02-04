"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
荅曰： a丈 。
"""

"""
Suppose there is a door that, when opened, leaves a gap of 1 chi from the threshold and does not close by 2 cun.
Question: how wide is the door?

Answer: the door is *a* zhang wide.
"""

# Definitions:
# 1 zhang = 10 chi
# 1 chi = 10 cun

# The total width of the door is the sum of the gap when opened (1 chi) and the gap when not closed (2 cun).

# Convert 1 chi to cun
gap_open = 1 * 10  # 1 chi = 10 cun

# Add the gap when not closed
total_width_cun = gap_open + 2  # Total width in cun

# Convert total width back to zhang
a = Fraction(total_width_cun, 10 * 10)  # Convert cun to zhang (1 zhang = 100 cun)

a  # The width of the door in zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 3/25"""
