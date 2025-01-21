"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=35/26)斗 ，下禾 c(=1)秉 實 d(=41/52)斗 。
"""

"""
This problem involves solving a system of equations to determine the yield per bundle of upper and lower millet. The procedure is described as a "方程術" (method of equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Problem setup:
# 上禾 (upper millet) and 下禾 (lower millet) yields per bundle are unknown.
# We are given two conditions:
# 1. 7 bundles of 上禾, losing 1 dou, and adding 2 bundles of 下禾 yield 10 dou.
# 2. 8 bundles of 下禾, gaining 1 dou, and adding 2 bundles of 上禾 yield 10 dou.

# Let x = yield per bundle of 上禾 (in dou)
# Let y = yield per bundle of 下禾 (in dou)

# Condition 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11

# Condition 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Solve the system of equations:
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Step 1: Eliminate one variable (e.g., y) by aligning coefficients.
# Multiply Equation 1 by 4 and Equation 2 by 1 to align the coefficients of y:
# 4 * (7x + 2y) = 4 * 11 -> 28x + 8y = 44
# 1 * (2x + 8y) = 1 * 9  ->  2x + 8y = 9

# Step 2: Subtract the second equation from the first:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 28x - 2x = 35
# 26x = 35
x = Fraction(35, 26)  # Yield per bundle of 上禾

# Step 3: Substitute x into one of the original equations to solve for y.
# Using Equation 1: 7x + 2y = 11
# 7 * (35/26) + 2y = 11
# 245/26 + 2y = 11
# 2y = 11 - 245/26
# 2y = (286/26) - (245/26)
# 2y = 41/26
# y = (41/26) / 2
y = Fraction(41, 52)  # Yield per bundle of 下禾

# Final results:
a = 1  # 上禾 per bundle
b = x  # 上禾 yield per bundle in dou
c = 1  # 下禾 per bundle
d = y  # 下禾 yield per bundle in dou

# Output:
print(f"上禾 {a}秉 實 {b}斗")
print(f"下禾 {c}秉 實 {d}斗")


"""


### Explanation of the Solution:
1. The problem is modeled as a system of linear equations based on the conditions provided.
2. The equations are solved step-by-step using elimination and substitution, adhering to the "方程術" described in the procedure.
3. The results are expressed as fractions (`Fraction` class) to maintain exactness, as required by the problem.

### Answer:
- 上禾 \( a = 1 \) 秉, 實 \( b = \frac{35}{26} \) 斗
- 下禾 \( c = 1 \) 秉, 實 \( d = \frac{41}{52} \) 斗
"""


"""
"""
