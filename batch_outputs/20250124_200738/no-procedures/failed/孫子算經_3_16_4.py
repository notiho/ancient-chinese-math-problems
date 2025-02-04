"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
答曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, and its length is unknown. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. When the rope is folded in half and used to measure, it falls short by 1 chi.
Question: What is the length of the wood?

Answer: The length of the wood is *a* chi.
"""

# Define the excess and shortfall
excess = Fraction(4, 1) + Fraction(5, 10)  # 4 chi 5 cun
shortfall = Fraction(1, 1)  # 1 chi

# Let the length of the rope be x, and the length of the wood be y.
# From the problem:
# 1. x = y + excess
# 2. y = (x / 2) - shortfall

# Solve the equations:
# Substitute x = y + excess into y = (x / 2) - shortfall
# y = ((y + excess) / 2) - shortfall
# Multiply through by 2:
# 2y = y + excess - 2 * shortfall
# y = excess - 2 * shortfall

# Calculate y
excess = Fraction(45, 10)  # 4 chi 5 cun = 45/10 chi
shortfall = Fraction(1, 1)  # 1 chi

a = excess - 2 * shortfall  # Length of the wood

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/2, Actual: 5/2"""
