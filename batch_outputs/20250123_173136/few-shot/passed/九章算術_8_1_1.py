"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of equations to determine the yield of one bundle of upper millet (上禾) and one bundle of lower millet (下禾). The procedure is described in terms of ancient Chinese "方程術" (method of solving equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾七秉，損實一斗，益之下禾二秉，而實一十斗
# Equation 1: 7 * 上禾 - 1 + 2 * 下禾 = 10
# Rearrange: 7 * 上禾 + 2 * 下禾 = 11

# 下禾八秉，益實一斗與上禾二秉，而實一十斗
# Equation 2: 8 * 下禾 + 1 + 2 * 上禾 = 10
# Rearrange: 2 * 上禾 + 8 * 下禾 = 9

# Representing the equations:
# 7 * 上禾 + 2 * 下禾 = 11
# 2 * 上禾 + 8 * 下禾 = 9

# Step 1: Eliminate one variable using the 方程術
# Multiply the first equation by 8 and the second equation by 2 to align 下禾 coefficients
eq1 = [7 * 8, 2 * 8, 11 * 8]  # 56 * 上禾 + 16 * 下禾 = 88
eq2 = [2 * 2, 8 * 2, 9 * 2]   # 4 * 上禾 + 16 * 下禾 = 18

# Subtract eq2 from eq1 to eliminate 下禾
eliminated_eq = [eq1[0] - eq2[0], eq1[1] - eq2[1], eq1[2] - eq2[2]]  # 52 * 上禾 = 70
# Simplify to find 上禾
上禾 = Fraction(eliminated_eq[2], eliminated_eq[0])  # 上禾 = 70 / 52 = 35 / 26

# Step 2: Substitute 上禾 back into one of the original equations to find 下禾
# Using the first equation: 7 * 上禾 + 2 * 下禾 = 11
下禾 = Fraction(11 - 7 * 上禾, 2)  # 下禾 = (11 - 7 * (35 / 26)) / 2

# Simplify 下禾
下禾 = Fraction(11 * 26 - 7 * 35, 2 * 26)  # 下禾 = (286 - 245) / 52 = 41 / 52

# Final results
a = 上禾  # 上禾一秉實
b = 下禾  # 下禾一秉實

# Output
a, b


"""


### Explanation of the Code:
1. **Equations Setup**:
   - The problem provides two equations based on the relationships between the bundles of millet and their yields.
   - These equations are expressed in terms of `上禾` (upper millet) and `下禾` (lower millet).

2. **Elimination**:
   - The coefficients of one variable (`下禾`) are aligned by multiplying the equations by appropriate factors.
   - Subtraction eliminates `下禾`, leaving an equation with only `上禾`.

3. **Substitution**:
   - The value of `上禾` is substituted back into one of the original equations to solve for `下禾`.

4. **Fraction Handling**:
   - The `Fraction` class is used to ensure exact arithmetic with rational numbers.

### Final Answer:
- 上禾一秉實: `a = 35/26` 斗
- 下禾一秉實: `b = 41/52` 斗
"""


"""
"""
