"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we will follow the ancient Chinese method described in the procedure ("術"). This involves setting up a system of linear equations and solving it step by step using elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Step 1: Define the equations based on the problem
# Equation 1: 3 * 上禾 - 10 * 下禾 = -6
# Equation 2: -2 * 上禾 + 5 * 下禾 = -1

# Coefficients for the equations
上禾_coeff_1 = 3
下禾_coeff_1 = -10
constant_1 = -6

上禾_coeff_2 = -2
下禾_coeff_2 = 5
constant_2 = -1

# Step 2: Eliminate one variable (e.g., 上禾) using the elimination method
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
multiplier_1 = 2
multiplier_2 = 3

上禾_coeff_1 *= multiplier_1
下禾_coeff_1 *= multiplier_1
constant_1 *= multiplier_1

上禾_coeff_2 *= multiplier_2
下禾_coeff_2 *= multiplier_2
constant_2 *= multiplier_2

# Subtract the second equation from the first to eliminate 上禾
下禾_coeff_final = 下禾_coeff_1 - 下禾_coeff_2
constant_final = constant_1 - constant_2

# Solve for 下禾
下禾 = Fraction(constant_final, 下禾_coeff_final)

# Step 3: Substitute 下禾 back into one of the original equations to solve for 上禾
上禾 = Fraction(-6 - (-10 * 下禾), 3)

# Step 4: The results are the values for 上禾 and 下禾
a = 上禾  # 上禾一秉實
b = 下禾  # 下禾一秉實

# Output the results
a, b


"""


### Explanation of the Code:
1. **Define the equations**: The problem gives two equations based on the relationships between 上禾 and 下禾. These are translated into coefficients and constants.
2. **Elimination method**: We eliminate one variable (上禾) by aligning its coefficients in both equations and subtracting them.
3. **Solve for the remaining variable**: After eliminating 上禾, we solve for 下禾.
4. **Back substitution**: Substitute the value of 下禾 into one of the original equations to solve for 上禾.
5. **Output the results**: The values of 上禾 and 下禾 represent the 实 (yield) per 秉 (bundle) for each type of crop.

### Final Answer:
- 上禾一秉實 `a` 斗
- 下禾一秉實 `b` 斗
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: -8/7
Variable 'b' has wrong value. Expected: 3, Actual: 9/35"""
