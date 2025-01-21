"""
今有木，不知長短，引繩度之，餘繩四尺五寸；屈繩量之，不足一尺。問：幾何？
答曰： a尺 。
"""

"""
Suppose there is a piece of wood of unknown length. When measured with a stretched rope, the rope exceeds the wood by 4 chi and 5 cun. When the rope is folded in half and used to measure, it falls short by 1 chi.
Question: what is the length of the wood?

Answer: the length of the wood is *a* chi.
"""

# Define the excess and shortfall
excess = Fraction(4, 1) + Fraction(5, 10)  # 4 chi 5 cun
shortfall = Fraction(1, 1)  # 1 chi

# Let the length of the rope be x (in chi)
# When stretched: x = wood_length + excess
# When folded: x / 2 = wood_length - shortfall
# Solve for wood_length

# Equation 1: x = wood_length + excess
# Equation 2: x / 2 = wood_length - shortfall

# Rearrange Equation 2: x = 2 * (wood_length - shortfall)
# Substitute into Equation 1:
# 2 * (wood_length - shortfall) = wood_length + excess
# Simplify:
# 2 * wood_length - 2 * shortfall = wood_length + excess
# wood_length = 2 * shortfall + excess

wood_length = 2 * shortfall + excess

# Final answer
a = wood_length
a
"""
"""
