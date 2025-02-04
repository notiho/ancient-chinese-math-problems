"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""

"""


from fractions import Fraction

# Given equations:
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Represent the equations
eq1 = [3, 2, 1, 39]  # Coefficients for 上, 中, 下, and the result
eq2 = [2, 3, 1, 34]
eq3 = [1, 2, 3, 26]

# Step 2: Eliminate 下禾 (下) from eq1 and eq2
# Multiply eq1 by 1 (coefficient of 下 in eq2) and eq2 by 1 (coefficient of 下 in eq1)
eq1_scaled = [3, 2, 1, 39]
eq2_scaled = [2, 3, 1, 34]

# Subtract eq2_scaled from eq1_scaled to eliminate 下
eq4 = [
    eq1_scaled[0] - eq2_scaled[0],  # 上 coefficient
    eq1_scaled[1] - eq2_scaled[1],  # 中 coefficient
    eq1_scaled[2] - eq2_scaled[2],  # 下 coefficient (should be 0)
    eq1_scaled[3] - eq2_scaled[3],  # Result
]  # eq4: 上 + (-1)中 = 5
# eq4 becomes: 上 - 中 = 5

# Step 3: Eliminate 下禾 (下) from eq2 and eq3
# Multiply eq2 by 3 (coefficient of 下 in eq3) and eq3 by 1 (coefficient of 下 in eq2)
eq2_scaled = [6, 9, 3, 102]
eq3_scaled = [1, 2, 3, 26]

# Subtract eq3_scaled from eq2_scaled to eliminate 下
eq5 = [
    eq2_scaled[0] - eq3_scaled[0],  # 上 coefficient
    eq2_scaled[1] - eq3_scaled[1],  # 中 coefficient
    eq2_scaled[2] - eq3_scaled[2],  # 下 coefficient (should be 0)
    eq2_scaled[3] - eq3_scaled[3],  # Result
]  # eq5: 5上 + 7中 = 76
# eq5 becomes: 5上 + 7中 = 76

# Step 4: Solve the system of two equations (eq4 and eq5)
# eq4: 上 - 中 = 5
# eq5: 5上 + 7中 = 76

# From eq4, express 上 in terms of 中
# 上 = 中 + 5
上_in_terms_of_中 = lambda 中: 中 + 5

# Substitute 上 into eq5
# 5(中 + 5) + 7中 = 76
# 5中 + 25 + 7中 = 76
# 12中 = 51
中 = Fraction(51, 12)

# Solve for 上 using 上 = 中 + 5
上 = 上_in_terms_of_中(中)

# Step 5: Solve for 下 using any original equation (e.g., eq1)
# 3上 + 2中 + 1下 = 39
下 = Fraction(39) - 3 * 上 - 2 * 中

# Final results
a = 上
b = 中
c = 下


"""

"""


"""
"""
