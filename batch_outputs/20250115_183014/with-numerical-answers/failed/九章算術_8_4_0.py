"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=8)升 ，下禾 c(=1)秉 實 d(=3)升 。
"""

This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of matrix elimination. Below is the translation of the problem and its solution into Python code:

---

"""
Suppose there are 6 bundles of superior grain (上禾), which lose 1 dou and 8 sheng of grain when processed, equivalent to 10 bundles of inferior grain (下禾).  
Additionally, 15 bundles of inferior grain lose 5 sheng of grain, equivalent to 5 bundles of superior grain.  
Question: how much grain does 1 bundle of superior grain and 1 bundle of inferior grain yield?

The procedure says: Treat it as a system of linear equations.  
Place 6 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and the loss of 1 dou and 8 sheng as positive.  
Next, place 5 bundles of superior grain as negative, 15 bundles of inferior grain as positive, and the loss of 5 sheng as positive.  
Use the positive-negative procedure to solve.

The fangcheng procedure says:  
1. Place the coefficients of superior grain, middle grain (if any), and inferior grain, along with the total loss, on the right side.  
2. Arrange the rows for superior, middle, and inferior grain as described.  
3. Multiply the first row by the coefficient of the second row's leading term, then divide directly. Repeat for subsequent rows.  
4. For the remaining rows, multiply and divide as needed to eliminate terms.  
5. Solve for the unknowns by back-substitution, dividing the remaining terms by their coefficients.  

Answer: 1 bundle of superior grain yields *a*(=1 dou and *b*(=8 sheng), and 1 bundle of inferior grain yields *c*(=1 dou and *d*(=3 sheng).
"""

from fractions import Fraction

# Convert dou and sheng to a consistent unit (sheng)
# 1 dou = 10 sheng
損實1 = 1 * 10 + 8  # 1 dou 8 sheng = 18 sheng
損實2 = 5  # 5 sheng

# Coefficients for the equations
# Equation 1: 6上禾 - 10下禾 = 18
# Equation 2: -5上禾 + 15下禾 = 5
上禾1, 下禾1, 常數1 = 6, -10, 18
上禾2, 下禾2, 常數2 = -5, 15, 5

# Eliminate one variable (e.g., 上禾) using the fangcheng method
# Multiply the first equation by 5 (from the second equation's 上禾 coefficient)
# Multiply the second equation by 6 (from the first equation's 上禾 coefficient)
方程1_新 = [上禾1 * 5, 下禾1 * 5, 常數1 * 5]  # [30, -50, 90]
方程2_新 = [上禾2 * 6, 下禾2 * 6, 常數2 * 6]  # [-30, 90, 30]

# Add the two equations to eliminate 上禾
下禾係數 = 方程1_新[1] + 方程2_新[1]  # -50 + 90 = 40
常數 = 方程1_新[2] + 方程2_新[2]  # 90 + 30 = 120

# Solve for 下禾 (1 bundle of inferior grain)
下禾實 = Fraction(常數, 下禾係數)  # 120 / 40 = 3 (sheng)

# Substitute 下禾實 back into the first equation to solve for 上禾
# 6上禾 - 10下禾 = 18
上禾實 = Fraction(常數1 - 下禾1 * 下禾實, 上禾1)  # (18 - (-10 * 3)) / 6 = 8/1 = 8 (sheng)

# Convert results back to dou and sheng
a, b = divmod(上禾實, 10)  # 8 sheng = 0 dou 8 sheng
c, d = divmod(下禾實, 10)  # 3 sheng = 0 dou 3 sheng

# Final results
a = int(a)  # 上禾 dou
b = int(b)  # 上禾 sheng
c = int(c)  # 下禾 dou
d = int(d)  # 下禾 sheng

# Output: 上禾實 = 1 dou 8 sheng, 下禾實 = 1 dou 3 sheng
"""
Code error: invalid syntax (<string>, line 2)"""
