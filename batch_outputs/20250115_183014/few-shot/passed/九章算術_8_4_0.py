"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of "upper millet" (上禾) and one sheaf of "lower millet" (下禾). The procedure uses ancient Chinese methods for solving simultaneous equations, which is equivalent to Gaussian elimination in modern terms. Here's the solution:

### Problem Setup:
We are given:
1. 6 sheaves of upper millet (上禾) lose 1 dou and 8 sheng (1斗8升) of grain, which is equivalent to 18 sheng, and corresponds to 10 sheaves of lower millet (下禾).
2. 15 sheaves of lower millet lose 5 sheng of grain, which corresponds to 5 sheaves of upper millet.

We need to find the yield of one sheaf of upper millet and one sheaf of lower millet.

### Procedure:
The procedure involves setting up two equations based on the given relationships and solving them using the described ancient method.

### Solution in Python:


"""


from fractions import Fraction

# Given data
上禾_1 = 6  # 6 sheaves of upper millet
下禾_1 = -10  # Corresponds to 10 sheaves of lower millet (negative because it's on the other side of the equation)
損實_1 = 18  # 1斗8升 = 18升

上禾_2 = -5  # Corresponds to 5 sheaves of upper millet (negative because it's on the other side of the equation)
下禾_2 = 15  # 15 sheaves of lower millet
損實_2 = 5  # 5升

# Step 1: Eliminate one variable (use 上禾 as the pivot)
# Multiply the first equation by 5 and the second equation by 6 to align the coefficients of 上禾
eq1_上禾 = 5 * 上禾_1
eq1_下禾 = 5 * 下禾_1
eq1_損實 = 5 * 損實_1

eq2_上禾 = 6 * 上禾_2
eq2_下禾 = 6 * 下禾_2
eq2_損實 = 6 * 損實_2

# Add the two equations to eliminate 上禾
combined_下禾 = eq1_下禾 + eq2_下禾
combined_損實 = eq1_損實 + eq2_損實

# Solve for 下禾 (yield of one sheaf of lower millet)
下禾_實 = Fraction(combined_損實, combined_下禾)

# Step 2: Solve for 上禾 (yield of one sheaf of upper millet)
# Substitute 下禾_實 back into the first equation
上禾_損實 = 損實_1 - (下禾_1 * 下禾_實)
上禾_實 = Fraction(上禾_損實, 上禾_1)

# Convert results to dou and sheng
a = 1  # One sheaf of upper millet
b = 上禾_實  # Yield of one sheaf of upper millet in sheng
c = 1  # One sheaf of lower millet
d = 下禾_實  # Yield of one sheaf of lower millet in sheng

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Setting up the equations**: The two given relationships are translated into equations with coefficients for 上禾 (upper millet), 下禾 (lower millet), and 損實 (grain loss).
2. **Elimination**: The first variable (上禾) is eliminated by aligning its coefficients in both equations and adding them together.
3. **Solving for 下禾**: The combined equation is solved for 下禾 (yield of one sheaf of lower millet).
4. **Substitution**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾 (yield of one sheaf of upper millet).
5. **Conversion**: The results are presented in terms of dou and sheng.

### Final Answer:
- The yield of one sheaf of upper millet is `b` sheng.
- The yield of one sheaf of lower millet is `d` sheng.
"""


"""
"""
