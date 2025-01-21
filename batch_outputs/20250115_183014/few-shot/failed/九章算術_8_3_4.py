"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
This problem involves solving a system of linear equations to determine the yield per bundle of "upper millet" (上禾) and "lower millet" (下禾). The procedure follows the ancient Chinese method of solving simultaneous equations, which is akin to Gaussian elimination.

### Problem Breakdown:
- **Given:**
  - 5 bundles of upper millet lose 1 dou and 1 sheng of grain when exchanged for 7 bundles of lower millet.
  - 7 bundles of upper millet lose 2 dou and 5 sheng of grain when exchanged for 5 bundles of lower millet.
- **Question:**
  - What is the yield per bundle of upper millet and lower millet?

### Procedure:
The ancient method involves setting up the equations, performing elimination, and solving for the unknowns step by step.

### Solution in Python:


"""


from fractions import Fraction

# Convert dou and sheng to a single unit (sheng)
# 1 dou = 10 sheng
損實1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
損實2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Coefficients for the equations
# Equation 1: 5上禾 - 7下禾 = 11 (損實1)
上禾1 = 5
下禾1 = -7
常數1 = 損實1

# Equation 2: 7上禾 - 5下禾 = 25 (損實2)
上禾2 = 7
下禾2 = -5
常數2 = 損實2

# Eliminate one variable (下禾) using the ancient method
# Multiply the first equation by 5 (coefficient of 下禾 in the second equation)
# Multiply the second equation by 7 (coefficient of 下禾 in the first equation)
# Then subtract the two equations

上禾消去下禾 = 上禾1 * 5 - 上禾2 * 7
常數消去下禾 = 常數1 * 5 - 常數2 * 7

# Solve for 上禾 (yield per bundle of upper millet)
上禾實 = Fraction(常數消去下禾, 上禾消去下禾)

# Substitute 上禾實 back into one of the original equations to solve for 下禾
下禾實 = Fraction(常數1 - 上禾1 * 上禾實, 下禾1)

# Convert results back to dou and sheng
a = 上禾實 // 10  # dou for upper millet
b = 上禾實 % 10   # sheng for upper millet
c = 下禾實 // 10  # dou for lower millet
d = 下禾實 % 10   # sheng for lower millet

# Final answer
print(f"上禾 {a}斗 {b}升, 下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Convert Units:** The problem uses dou and sheng as units of volume. Since 1 dou = 10 sheng, we convert everything into sheng for easier calculations.
2. **Set Up Equations:** The two equations are derived from the problem statement:
   - \( 5 \cdot 上禾 - 7 \cdot 下禾 = 11 \) (Equation 1)
   - \( 7 \cdot 上禾 - 5 \cdot 下禾 = 25 \) (Equation 2)
3. **Elimination:** Using the ancient method (similar to Gaussian elimination), we eliminate one variable (下禾) by multiplying the equations and subtracting them.
4. **Solve for 上禾:** After eliminating 下禾, we solve for 上禾 (yield per bundle of upper millet).
5. **Substitute Back:** Substitute the value of 上禾 into one of the original equations to solve for 下禾.
6. **Convert Back to Dou and Sheng:** The results are converted back to dou and sheng for the final answer.

### Final Answer:
The yield per bundle of upper millet and lower millet is expressed in dou and sheng.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
