"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to determine the "實" (yield per unit) for both 上禾 (upper grain) and 下禾 (lower grain).

### Problem Setup:
- Equation 1: 上禾 6秉 - 下禾 10秉 = 1斗8升 (18升)
- Equation 2: -上禾 5秉 + 下禾 15秉 = 5升

We will solve this system of equations using the described method.

### Python Code:


"""


from fractions import Fraction

# Convert units to consistent scale (1斗 = 10升)
斗_to_升 = 10
損實1 = 1 * 斗_to_升 + 8  # 1斗8升 = 18升
損實2 = 5  # 5升

# Coefficients of the equations
# Equation 1: 6上禾 - 10下禾 = 18
# Equation 2: -5上禾 + 15下禾 = 5
上禾1, 下禾1, 常數1 = 6, -10, 損實1
上禾2, 下禾2, 常數2 = -5, 15, 損實2

# Step 1: Eliminate one variable (use 上禾 as the pivot)
# Multiply equations to align 上禾 coefficients
factor1 = 上禾2
factor2 = 上禾1

# Scale equations
eq1_scaled = [上禾1 * factor1, 下禾1 * factor1, 常數1 * factor1]
eq2_scaled = [上禾2 * factor2, 下禾2 * factor2, 常數2 * factor2]

# Subtract equations to eliminate 上禾
下禾_coeff = eq1_scaled[1] - eq2_scaled[1]
常數_coeff = eq1_scaled[2] - eq2_scaled[2]

# Solve for 下禾實 (yield per unit of 下禾)
下禾_實 = Fraction(常數_coeff, 下禾_coeff)

# Step 2: Solve for 上禾實 using one of the original equations
# Substitute 下禾_實 into the first equation
上禾_實 = Fraction(常數1 - 下禾1 * 下禾_實, 上禾1)

# Results
a = 1  # 上禾 per 秉
b = 上禾_實  # 上禾實 (升 per 秉)
c = 1  # 下禾 per 秉
d = 下禾_實  # 下禾實 (升 per 秉)

# Output
print(f"上禾 {a}秉 實 {b}升")
print(f"下禾 {c}秉 實 {d}升")


"""


### Explanation:
1. **Convert Units**: All measurements are converted to the same unit (升) for consistency.
2. **Set Up Equations**: The problem is represented as a system of linear equations.
3. **Eliminate Variables**: Using the described method, one variable (上禾 or 下禾) is eliminated by scaling and subtracting equations.
4. **Solve for Remaining Variables**: The remaining variable is solved, and the result is substituted back to find the other variable.
5. **Output Results**: The yield per 秉 for both 上禾 and 下禾 is calculated and displayed.

### Final Answer:
The values of `a`, `b`, `c`, and `d` will be computed and printed as the solution to the problem.
"""


"""
"""
