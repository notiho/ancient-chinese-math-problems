"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=35/26)斗 ，下禾 c(=1)秉 實 d(=41/52)斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of linear algebra. Below is the Python implementation of the problem and its solution.


"""


from fractions import Fraction

# Problem setup:
# 上禾 (upper millet) = 7 秉, 損實 1 斗, 益之下禾 2 秉, 實 10 斗
# 下禾 (lower millet) = 8 秉, 益實 1 斗, 與上禾 2 秉, 實 10 斗

# Let x = 实 (yield per 秉 of 上禾)
# Let y = 实 (yield per 秉 of 下禾)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Rewrite the equations:
# 7x + 2y = 11  (Equation 1)
# 2x + 8y = 9   (Equation 2)

# Solve using the fangcheng method:

# Step 1: Eliminate one variable (e.g., y) by aligning coefficients.
# Multiply Equation 1 by 8 and Equation 2 by 2 to align the coefficients of y:
# 56x + 16y = 88  (Equation 1 scaled)
# 4x + 16y = 18   (Equation 2 scaled)

# Step 2: Subtract the second equation from the first to eliminate y:
# (56x + 16y) - (4x + 16y) = 88 - 18
# 52x = 70
x = Fraction(70, 52)  # Simplify to x = 35/26

# Step 3: Substitute x back into one of the original equations to solve for y.
# Using Equation 1: 7x + 2y = 11
# 7(35/26) + 2y = 11
# 245/26 + 2y = 11
# 2y = 11 - 245/26
# 2y = 286/26 - 245/26
# 2y = 41/26
y = Fraction(41, 52)  # Simplify to y = 41/52

# Final results:
a = 1  # 上禾实 per 秉
b = x  # 实 = 35/26 斗
c = 1  # 下禾实 per 秉
d = y  # 实 = 41/52 斗

# Output the results:
print(f"上禾 a({a})秉 实 b({b})斗")
print(f"下禾 c({c})秉 实 d({d})斗")


"""


### Explanation of the Solution:
1. **Equation Setup**: The problem is translated into two linear equations based on the relationships between the yields of 上禾 (upper millet) and 下禾 (lower millet).
2. **Fangcheng Method**: The ancient Chinese method of elimination is used to solve the system of equations. This involves scaling equations to align coefficients, subtracting to eliminate one variable, and back-substituting to find the other variable.
3. **Fraction Representation**: The `Fraction` class is used to ensure exact arithmetic, as the results involve fractions.

### Final Answer:
- 上禾实 per 秉: \( \frac{35}{26} \) 斗
- 下禾实 per 秉: \( \frac{41}{52} \) 斗
"""


"""
"""
