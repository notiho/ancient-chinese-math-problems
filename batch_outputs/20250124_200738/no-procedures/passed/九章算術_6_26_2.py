"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints:
- The outer checkpoint takes 1/3 of the rice.
- The middle checkpoint takes 1/5 of the remaining rice.
- The inner checkpoint takes 1/7 of the remaining rice.
After passing all three checkpoints, 5 dou of rice remain.

Question: How much rice did the person originally carry?

Answer: *a* dou.
"""

from fractions import Fraction

# Remaining rice after all checkpoints
remaining_rice = 5

# Let the original amount of rice be x
# After the inner checkpoint, 6/7 of the rice remains
after_inner = Fraction(7, 6) * remaining_rice

# After the middle checkpoint, 4/5 of the rice remains
after_middle = Fraction(5, 4) * after_inner

# After the outer checkpoint, 2/3 of the rice remains
original_rice = Fraction(3, 2) * after_middle

# The original amount of rice
a = original_rice

a  # Output the result#----- content ends here -----

"""
"""
