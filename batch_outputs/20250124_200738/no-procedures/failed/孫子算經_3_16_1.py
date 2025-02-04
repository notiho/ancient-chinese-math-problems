"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
答曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood of unknown length. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. When the rope is folded in half and used to measure the wood, it falls short by 1 chi.
Question: What is the length of the wood?

Answer: The length of the wood is *a* chi.
"""

# Let the length of the rope be x (in chi)
# The length of the wood is y (in chi)

# When the rope is stretched:
# x = y + 4 + 5/10 (4 chi and 5 cun)
# x = y + 4.5

# When the rope is folded in half:
# y = (x / 2) - 1

# Solve these two equations for y:
# From the first equation: x = y + 4.5
# Substitute into the second equation: y = ((y + 4.5) / 2) - 1

from fractions import Fraction

# Solve for y
y = Fraction(2 * (4.5 - 1), 1)
a = y

# The length of the wood is:
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
