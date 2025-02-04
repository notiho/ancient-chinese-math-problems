"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose a person carries rice through three checkpoints:
- The outer checkpoint takes 1/3 of the rice.
- The middle checkpoint takes 1/5 of the rice.
- The inner checkpoint takes 1/7 of the rice.
After passing all three checkpoints, 5 dou of rice remains.

Question: How much rice did the person originally carry?

Answer: *a* dou.
"""

# Remaining rice after all checkpoints
remaining_rice = 5

# Let the original amount of rice be "x"
# After the inner checkpoint, the remaining rice is (6/7) of what was left after the middle checkpoint.
# After the middle checkpoint, the remaining rice is (4/5) of what was left after the outer checkpoint.
# After the outer checkpoint, the remaining rice is (2/3) of the original amount.

# Working backwards:
# Remaining rice after the inner checkpoint:
after_inner = Fraction(remaining_rice, 6) * 7

# Remaining rice after the middle checkpoint:
after_middle = Fraction(after_inner, 4) * 5

# Remaining rice after the outer checkpoint:
original_rice = Fraction(after_middle, 2) * 3

# The original amount of rice
a = original_rice

a  # Output the result#----- content ends here -----

"""
"""
