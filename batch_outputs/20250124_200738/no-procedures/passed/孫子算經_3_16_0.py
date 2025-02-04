"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
答曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, but its length is unknown. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. When the rope is bent in half, it is 1 chi short of the wood.
Question: What is the length of the wood?

Answer: The wood is *a* chi.
"""

# Let the length of the rope be x (in chi)
# The length of the wood is x - 4 chi 5 cun when the rope is stretched
# The length of the wood is x/2 + 1 chi when the rope is bent in half

# Convert 4 chi 5 cun to fractional chi (1 chi = 10 cun)
excess_length = 4 + Fraction(5, 10)

# Set up the equation:
# x - excess_length = x/2 + 1
# Solve for x
from fractions import Fraction

x = 2 * (1 + excess_length)

# The length of the wood is x - excess_length
a = x - excess_length

# Output the result
a#----- content ends here -----

"""
"""
