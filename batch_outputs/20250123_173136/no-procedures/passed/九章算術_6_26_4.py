"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
荅曰： a斗 。
"""

"""
Suppose someone carries rice through three checkpoints:
- At the outer checkpoint, for every 3 dou, 1 dou is taken.
- At the middle checkpoint, for every 5 dou, 1 dou is taken.
- At the inner checkpoint, for every 7 dou, 1 dou is taken.
After passing through all three checkpoints, 5 dou of rice remain.

Question: how much rice did the person originally carry?

Answer: *a* dou.
"""

from fractions import Fraction

# Remaining rice after all checkpoints
remaining_rice = 5

# Let the original amount of rice be x
# Outer checkpoint: for every 3 dou, 1 dou is taken, so 2/3 of the rice passes through
# Middle checkpoint: for every 5 dou, 1 dou is taken, so 4/5 of the rice passes through
# Inner checkpoint: for every 7 dou, 1 dou is taken, so 6/7 of the rice passes through

# The relationship is:
# remaining_rice = x * (2/3) * (4/5) * (6/7)

# Solve for x (original rice)
a = Fraction(remaining_rice) / (Fraction(2, 3) * Fraction(4, 5) * Fraction(6, 7))

# The answer is:
a
"""
"""
