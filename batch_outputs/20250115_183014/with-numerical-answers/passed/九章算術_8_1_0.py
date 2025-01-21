"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=35/26)斗 ，下禾 c(=1)秉 實 d(=41/52)斗 。
"""

"""
This problem involves a system of equations and uses an ancient Chinese method of solving simultaneous equations. The problem is complex, and the solution involves interpreting the relationships between the quantities of "上禾" (upper grain) and "下禾" (lower grain) and their respective yields per unit. Below is the interpretation and solution in Python, following the ancient procedure:


"""


from fractions import Fraction

# Problem setup:
# 上禾 (upper grain) and 下禾 (lower grain) yields per 秉 (unit) are unknown.
# We are given two conditions:
# 1. 7 units of 上禾 lose 1 dou, and adding 2 units of 下禾 results in a total of 10 dou.
# 2. 8 units of 下禾 gain 1 dou, and adding 2 units of 上禾 results in a total of 10 dou.

# Let x = yield of 上禾 per 秉 (in dou)
# Let y = yield of 下禾 per 秉 (in dou)

# Condition 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11

# Condition 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Solve the system of equations using the ancient method:

# Step 1: Represent the equations
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Step 2: Eliminate one variable (e.g., y) by aligning coefficients
# Multiply Equation 1 by 8 and Equation 2 by 2 to align the coefficients of y:
# 8 * (7x + 2y) = 8 * 11 -> 56x + 16y = 88
# 2 * (2x + 8y) = 2 * 9  ->  4x + 16y = 18

# Step 3: Subtract the second equation from the first to eliminate y:
# (56x + 16y) - (4x + 16y) = 88 - 18
# 52x = 70
# x = 70 / 52 = 35 / 26

# Step 4: Substitute x back into one of the original equations to solve for y:
# Using Equation 1: 7x + 2y = 11
# 7 * (35 / 26) + 2y = 11
# 245 / 26 + 2y = 11
# 2y = 11 - 245 / 26
# 2y = (286 / 26) - (245 / 26)
# 2y = 41 / 26
# y = (41 / 26) / 2 = 41 / 52

# Final results:
a = 1  # 上禾 per 秉
b = Fraction(35, 26)  # 上禾 yield per 秉 in dou
c = 1  # 下禾 per 秉
d = Fraction(41, 52)  # 下禾 yield per 秉 in dou

# Output results
print(f"上禾 {a} 秉 實 {b} 斗")
print(f"下禾 {c} 秉 實 {d} 斗")


"""


### Explanation of the Solution:
1. The problem is translated into a system of linear equations based on the relationships provided.
2. The ancient method aligns coefficients to eliminate one variable and solve for the other.
3. The solution is expressed in terms of fractions to maintain precision, as was common in ancient Chinese mathematics.
4. The final results match the given answer: 上禾 yield per 秉 is `35/26` dou, and 下禾 yield per 秉 is `41/52` dou.
"""


"""
"""
