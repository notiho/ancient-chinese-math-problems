"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which are similar to modern elimination techniques. Let's translate the problem and solution into Python code step by step.

### Problem Breakdown:
1. **Given**:
   - 3 bundles of upper millet (上禾) plus 6 dou of grain equals 10 bundles of lower millet (下禾).
   - 5 bundles of lower millet plus 1 dou of grain equals 2 bundles of upper millet.

2. **Question**:
   - What is the grain yield (in dou) of 1 bundle of upper millet (上禾) and 1 bundle of lower millet (下禾)?

3. **Procedure**:
   - Use the method of elimination (正負術) to solve the system of equations.

### Translation into Python Code:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 3上禾 - 10下禾 - 6 = 0
上禾1 = 3
下禾1 = -10
常數1 = -6

# Equation 2: -2上禾 + 5下禾 - 1 = 0
上禾2 = -2
下禾2 = 5
常數2 = -1

# Step 1: Eliminate one variable (e.g., 上禾)
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
上禾1, 下禾1, 常數1 = 2 * 上禾1, 2 * 下禾1, 2 * 常數1
上禾2, 下禾2, 常數2 = 3 * 上禾2, 3 * 下禾2, 3 * 常數2

# Subtract the second equation from the first to eliminate 上禾
下禾 = 下禾1 - 下禾2
常數 = 常數1 - 常數2

# Solve for 下禾 (grain yield of 1 bundle of lower millet)
下禾實 = Fraction(-常數, 下禾)

# Step 2: Solve for 上禾 using 下禾實
# Substitute 下禾實 into the first equation
常數 = 常數1 - 下禾1 * 下禾實
上禾實 = Fraction(-常數, 上禾1)

# Results
a = 上禾實  # Grain yield of 1 bundle of upper millet
b = 下禾實  # Grain yield of 1 bundle of lower millet

# Output the results
a, b


"""


### Explanation of the Code:
1. **Define the equations**: The coefficients of the two equations are defined based on the problem statement.
2. **Eliminate one variable**: The equations are manipulated to eliminate one variable (上禾) by aligning their coefficients and subtracting.
3. **Solve for the remaining variable**: After eliminating 上禾, the value of 下禾 is calculated.
4. **Back-substitute**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
5. **Output the results**: The grain yields of 1 bundle of upper millet (上禾) and lower millet (下禾) are returned as fractions.

### Final Answer:
The grain yield of 1 bundle of upper millet is `a` dou, and the grain yield of 1 bundle of lower millet is `b` dou.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 20/7
Variable 'b' has wrong value. Expected: 3, Actual: -9/35"""
