"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using a method similar to Gaussian elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Problem setup
# Equation 1: 6上禾 - 10下禾 = 1斗8升 (convert 1斗8升 to total 升)
eq1_upper = 6  # Coefficient for 上禾
eq1_lower = -10  # Coefficient for 下禾
eq1_result = 10 * 1 + 8  # 1斗8升 = 10升 * 1斗 + 8升 = 18升

# Equation 2: -5上禾 + 15下禾 = 5升
eq2_upper = -5  # Coefficient for 上禾
eq2_lower = 15  # Coefficient for 下禾
eq2_result = 5  # 5升

# Step 1: Eliminate one variable (use 上禾 as the pivot)
# Multiply eq1 by 5 and eq2 by 6 to align coefficients of 上禾
eq1_upper_scaled = eq1_upper * 5
eq1_lower_scaled = eq1_lower * 5
eq1_result_scaled = eq1_result * 5

eq2_upper_scaled = eq2_upper * 6
eq2_lower_scaled = eq2_lower * 6
eq2_result_scaled = eq2_result * 6

# Subtract eq2 from eq1 to eliminate 上禾
final_lower = eq1_lower_scaled - eq2_lower_scaled
final_result = eq1_result_scaled - eq2_result_scaled

# Step 2: Solve for 下禾 (final_lower * 下禾 = final_result)
下禾 = Fraction(final_result, final_lower)

# Step 3: Substitute 下禾 back into one of the original equations to solve for 上禾
# Using eq1: eq1_upper * 上禾 + eq1_lower * 下禾 = eq1_result
上禾 = Fraction(eq1_result - eq1_lower * 下禾, eq1_upper)

# Convert results to 升 per 秉
a = 上禾  # 上禾 per 秉
b = 上禾  # 上禾實 in 升
c = 下禾  # 下禾 per 秉
d = 下禾  # 下禾實 in 升

# Output results
print(f"上禾每秉實: {a}升")
print(f"下禾每秉實: {c}升")


"""


### Explanation of the Code:
1. **Equation Setup**: The problem provides two equations based on the relationships between 上禾 and 下禾. These are converted into coefficients and constants.
2. **Elimination**: The coefficients of 上禾 are aligned by scaling the equations, and then 上禾 is eliminated by subtraction.
3. **Solve for 下禾**: The resulting equation is solved for 下禾.
4. **Substitute Back**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
5. **Results**: The results are expressed as the amount of grain (in 升) per 秉 for both 上禾 and 下禾.

This code follows the ancient procedure described in the problem and provides the solution for the amount of grain per 秉 for both 上禾 and 下禾.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 16/7
Variable 'b' has wrong value. Expected: 8, Actual: 16/7
Variable 'c' has wrong value. Expected: 1, Actual: -3/7
Variable 'd' has wrong value. Expected: 3, Actual: -3/7"""
