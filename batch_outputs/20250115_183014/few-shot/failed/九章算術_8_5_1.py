"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of equations to determine the yield of one bundle of upper millet (上禾) and one bundle of lower millet (下禾). The procedure is described as a method similar to solving simultaneous equations using elimination.

### Problem Restatement:
- 3 bundles of upper millet (上禾) plus an additional 6 dou of grain are equivalent to 10 bundles of lower millet (下禾).
- 5 bundles of lower millet (下禾) plus an additional 1 dou of grain are equivalent to 2 bundles of upper millet (上禾).
- Question: What is the yield (實) of one bundle of upper millet (上禾) and one bundle of lower millet (下禾)?

### Procedure:
The procedure involves setting up the equations, eliminating variables, and solving for the yield of each type of millet.

---


"""


from fractions import Fraction

# Define the equations:
# Equation 1: 3上禾 - 10下禾 = -6 (converted to standard form)
# Equation 2: -2上禾 + 5下禾 = -1 (converted to standard form)

# Coefficients for the equations
上禾1, 下禾1, 常數1 = 3, -10, -6  # First equation
上禾2, 下禾2, 常數2 = -2, 5, -1   # Second equation

# Eliminate one variable (e.g., 上禾) using the elimination method
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
上禾1, 下禾1, 常數1 = 2 * 上禾1, 2 * 下禾1, 2 * 常數1
上禾2, 下禾2, 常數2 = 3 * 上禾2, 3 * 下禾2, 3 * 常數2

# Subtract the second equation from the first to eliminate 上禾
下禾系數 = 下禾1 - 下禾2
常數項 = 常數1 - 常數2

# Solve for 下禾 (yield of one bundle of lower millet)
下禾實 = Fraction(-常數項, 下禾系數)

# Substitute 下禾實 back into one of the original equations to solve for 上禾
# Using the first equation: 3上禾 - 10下禾 = -6
上禾實 = Fraction(-常數1 - 下禾1 * 下禾實, 上禾1)

# Results
a = 1  # One bundle of upper millet
b = 上禾實  # Yield of one bundle of upper millet
c = 1  # One bundle of lower millet
d = 下禾實  # Yield of one bundle of lower millet

# Output results
a, b, c, d


"""


### Explanation of the Code:
1. **Equations Setup**: The problem is converted into two linear equations:
   - \( 3 \cdot 上禾 - 10 \cdot 下禾 = -6 \)
   - \( -2 \cdot 上禾 + 5 \cdot 下禾 = -1 \)

2. **Elimination Method**: The coefficients of \( 上禾 \) are aligned by multiplying the first equation by 2 and the second by 3. Subtracting the second equation from the first eliminates \( 上禾 \), leaving an equation with only \( 下禾 \).

3. **Solve for \( 下禾 \)**: The resulting equation is solved for \( 下禾 \) (yield of one bundle of lower millet).

4. **Substitute Back**: The value of \( 下禾 \) is substituted back into one of the original equations to solve for \( 上禾 \) (yield of one bundle of upper millet).

5. **Results**: The yields of one bundle of upper millet (\( b \)) and one bundle of lower millet (\( d \)) are calculated and returned.

---

### Final Answer:
- \( 上禾 a = 1 \) bundle, \( 實 b = \text{calculated value in dou} \)
- \( 下禾 c = 1 \) bundle, \( 實 d = \text{calculated value in dou} \)
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 8/7
Variable 'd' has wrong value. Expected: 3, Actual: -9/35"""
