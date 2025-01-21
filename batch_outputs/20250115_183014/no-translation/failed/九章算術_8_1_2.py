"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of linear equations based on the given relationships between the quantities of 上禾 (upper grain) and 下禾 (lower grain). Below is the Python implementation of the solution, following the described procedure:


"""


from fractions import Fraction

# Define the given relationships as equations:
# Let x = 实 of 上禾 per 秉, y = 实 of 下禾 per 秉

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Rearrange the equations:
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Solve using the 方程術:
# Step 1: Multiply Equation 1 by 8 and Equation 2 by 2 to align coefficients of x
eq1 = [7 * 8, 2 * 8, 11 * 8]  # 56x + 16y = 88
eq2 = [2 * 2, 8 * 2, 9 * 2]   # 4x + 16y = 18

# Step 2: Subtract Equation 2 from Equation 1 to eliminate y
eq3 = [eq1[0] - eq2[0], eq1[1] - eq2[1], eq1[2] - eq2[2]]  # 52x + 0y = 70
# Simplify: x = 70 / 52
x = Fraction(70, 52)

# Step 3: Substitute x back into one of the original equations to solve for y
# Using Equation 1: 7x + 2y = 11
y = Fraction(11 - 7 * x, 2)

# Results:
a = 7  # 上禾秉数
b = x  # 上禾实 per 秉
c = 8  # 下禾秉数
d = y  # 下禾实 per 秉

print(f"上禾 {a}秉 实 {b}斗 ，下禾 {c}秉 实 {d}斗 。")


"""


### Explanation of the Code:
1. The problem is translated into two linear equations based on the relationships provided.
2. The equations are solved step-by-step using elimination, as described in the 方程術.
3. The solution is expressed in terms of fractions to ensure accuracy.

### Final Answer:
- 上禾: `a = 7秉`, 实 `b = 35/26斗`
- 下禾: `c = 8秉`, 实 `d = 17/26斗`
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
