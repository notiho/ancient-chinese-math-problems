"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which are similar to modern elimination techniques. Let's translate the problem and solution into Python code.

### Problem Breakdown:
- There are two types of grain: "上禾" (upper grain) and "下禾" (lower grain).
- The relationships between their quantities and losses are given:
  1. 6 bundles of upper grain and 10 bundles of lower grain lose 1 dou 8 sheng (18 sheng).
  2. 5 bundles of upper grain and 15 bundles of lower grain lose 5 sheng.
- The goal is to find the actual amount of grain per bundle for both upper and lower grain.

### Procedure:
The procedure uses a method similar to Gaussian elimination:
1. Represent the problem as two equations.
2. Use elimination to solve for the unknowns step by step.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1_upper = 6  # Coefficient of 上禾 in the first equation
eq1_lower = -10  # Coefficient of 下禾 in the first equation
eq1_result = 18  # Result of the first equation (1 dou 8 sheng = 18 sheng)

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_upper = -5  # Coefficient of 上禾 in the second equation
eq2_lower = 15  # Coefficient of 下禾 in the second equation
eq2_result = 5  # Result of the second equation (5 sheng)

# Step 1: Eliminate one variable (下禾) using the two equations
# Multiply the first equation by 15 (to match 下禾 coefficient in eq2)
# Multiply the second equation by 10 (to match 下禾 coefficient in eq1)
factor1 = 15
factor2 = 10

new_eq1_upper = eq1_upper * factor1
new_eq1_lower = eq1_lower * factor1
new_eq1_result = eq1_result * factor1

new_eq2_upper = eq2_upper * factor2
new_eq2_lower = eq2_lower * factor2
new_eq2_result = eq2_result * factor2

# Subtract the second equation from the first to eliminate 下禾
final_upper = new_eq1_upper - new_eq2_upper
final_result = new_eq1_result - new_eq2_result

# Step 2: Solve for 上禾 (upper grain per bundle)
a = Fraction(final_result, final_upper)  # 上禾 per bundle in sheng

# Step 3: Solve for 下禾 (lower grain per bundle)
# Substitute the value of 上禾 back into one of the original equations
b = Fraction(eq1_result - eq1_upper * a, -eq1_lower)  # 下禾 per bundle in sheng

# Results
print(f"上禾一秉實 {a} 升")  # Upper grain per bundle
print(f"下禾一秉實 {b} 升")  # Lower grain per bundle
#----- content ends here -----


"""


### Explanation of the Code:
1. The equations are set up based on the problem description.
2. The coefficients are adjusted to eliminate one variable (下禾).
3. The remaining variable (上禾) is solved directly.
4. The value of 上禾 is substituted back into one of the original equations to solve for 下禾.
5. The results are expressed as fractions to ensure precision.

### Answer:
The output will provide the amount of grain per bundle for both upper and lower grain:
- 上禾一秉實 `a` 升
- 下禾一秉實 `b` 升
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 11/7
Variable 'b' has wrong value. Expected: 3, Actual: 6/7"""
