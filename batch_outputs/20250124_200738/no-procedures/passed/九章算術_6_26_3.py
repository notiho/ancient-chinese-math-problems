"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints:
- The outer checkpoint takes 1/3 of the rice.
- The middle checkpoint takes 1/5 of the rice.
- The inner checkpoint takes 1/7 of the rice.
After passing all three checkpoints, 5 dou of rice remain.

Question: How much rice did the person originally carry?

Answer: *a* dou.
"""

from fractions import Fraction

# Remaining rice after all checkpoints
remaining_rice = 5

# Let the original amount of rice be x
# After the inner checkpoint, 6/7 of the rice remains.
# After the middle checkpoint, 4/5 of the rice remains.
# After the outer checkpoint, 2/3 of the rice remains.

# The relationship is:
# remaining_rice = x * (2/3) * (4/5) * (6/7)

# Solve for x (original rice):
x = remaining_rice / (Fraction(2, 3) * Fraction(4, 5) * Fraction(6, 7))

# The original amount of rice
a = x

a  # Output the result#----- content ends here -----

"""
"""
