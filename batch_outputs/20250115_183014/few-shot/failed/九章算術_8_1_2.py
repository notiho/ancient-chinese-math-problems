"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of equations to determine the yield of one sheaf of upper and lower millet. The procedure describes using a method akin to Gaussian elimination to solve the equations. Here's the solution encoded in Python:


"""


"""
Suppose there are 7 sheaves of upper millet, which lose 1 dou of yield, and when combined with 2 sheaves of lower millet, the total yield is 10 dou.
Similarly, 8 sheaves of lower millet, when combined with 2 sheaves of upper millet, produce a total yield of 10 dou.
Question: what is the yield of one sheaf of upper millet and one sheaf of lower millet?

The procedure says: Treat the problem as a system of equations. Loss is treated as gain, and gain is treated as loss.
If the yield loses 1 dou, it means the actual yield exceeds 10 dou.
If the yield gains 1 dou, it means the actual yield is less than 10 dou.

The method for solving systems of equations says:
1. Place the coefficients of the upper millet, middle millet, and lower millet in rows, along with their respective yields.
2. Perform row operations to eliminate variables and solve for the unknowns.

Answer: The yield of one sheaf of upper millet is *a* dou, and the yield of one sheaf of lower millet is *b* dou.
"""

from fractions import Fraction

# Coefficients for the equations
# 7上禾 - 1斗 + 2下禾 = 10斗
# 2上禾 + 8下禾 + 1斗 = 10斗

# Adjust the equations to account for the "loss" and "gain" as described in the procedure:
# 7上禾 + 2下禾 = 11斗
# 2上禾 + 8下禾 = 9斗

# Represent the system of equations as a matrix
# [7  2 | 11]
# [2  8 |  9]

# Step 1: Eliminate the first variable (上禾) from the second equation
# Multiply the first row by 2 and the second row by 7, then subtract
# [7  2 | 11] * 2 -> [14  4 | 22]
# [2  8 |  9] * 7 -> [14 56 | 63]
# Subtract:
# [0 -52 | -41]

# The system now becomes:
# [7   2 | 11]
# [0 -52 | -41]

# Step 2: Solve for 下禾 (lower millet yield)
下禾 = Fraction(-41, -52)  # Simplify the fraction
下禾 = Fraction(41, 52)

# Step 3: Solve for 上禾 (upper millet yield)
# Use the first equation: 7上禾 + 2下禾 = 11
# 7上禾 = 11 - 2下禾
# 上禾 = (11 - 2下禾) / 7
上禾 = Fraction(11 - 2 * 下禾, 7)

# Results
a = 上禾  # Yield of one sheaf of upper millet
b = 下禾  # Yield of one sheaf of lower millet


"""


### Explanation of the Solution:
1. The problem is translated into a system of linear equations based on the relationships given.
2. Gaussian elimination is used to solve the system step by step, eliminating variables and solving for the unknowns.
3. The results are expressed as fractions to ensure precision.

### Final Answer:
- The yield of one sheaf of upper millet is `a` dou.
- The yield of one sheaf of lower millet is `b` dou.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 35/26
Variable 'b' has wrong value. Expected: 35/26, Actual: 41/52
Missing variable in output: 'c'
Missing variable in output: 'd'"""
