"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints:
- At the outer checkpoint, 1/3 of the rice is taken.
- At the middle checkpoint, 1/5 of the remaining rice is taken.
- At the inner checkpoint, 1/7 of the remaining rice is taken.
After passing all three checkpoints, 5 dou of rice remain.

Question: How much rice did the person originally carry?

Answer: *a* dou.
"""

from fractions import Fraction

# Remaining rice after all checkpoints
remaining_rice = 5

# Work backward through the checkpoints
# At the inner checkpoint, 1/7 of the rice is taken, so 6/7 remains
rice_after_middle = remaining_rice / Fraction(6, 7)

# At the middle checkpoint, 1/5 of the rice is taken, so 4/5 remains
rice_after_outer = rice_after_middle / Fraction(4, 5)

# At the outer checkpoint, 1/3 of the rice is taken, so 2/3 remains
original_rice = rice_after_outer / Fraction(2, 3)

# The original amount of rice
a = original_rice

a  # Output the result#----- content ends here -----

"""
"""
