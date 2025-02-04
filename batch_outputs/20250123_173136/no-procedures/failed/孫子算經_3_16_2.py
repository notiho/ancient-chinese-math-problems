"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
答曰： a尺 。
"""

"""
Suppose there is a piece of wood of unknown length. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. When the rope is folded in half and used to measure, it falls short by 1 chi.
Question: What is the length of the wood?

Answer: The wood is *a* chi.
"""

# Define the excess and shortfall
excess = Fraction(4, 1) + Fraction(5, 10)  # 4 chi and 5 cun (1 chi = 10 cun)
shortfall = Fraction(1, 1)  # 1 chi

# Let the length of the rope be R (in chi), and the length of the wood be W (in chi).
# From the problem:
# 1. R = W + excess
# 2. W = (R / 2) - shortfall

# Substitute R from the first equation into the second equation:
# W = ((W + excess) / 2) - shortfall

# Solve for W:
# 2W = W + excess - 2 * shortfall
# W = excess - 2 * shortfall

# Calculate W
W = excess - 2 * shortfall

# The length of the wood
a = W

# Result
a  # The length of the wood in chi
"""
Variable 'a' has wrong value. Expected: 13/2, Actual: 5/2"""
