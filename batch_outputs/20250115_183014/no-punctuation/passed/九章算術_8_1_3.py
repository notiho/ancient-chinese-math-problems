"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This problem involves solving a system of equations to determine the yield of one sheaf of upper and lower millet. The procedure provided is essentially a method for solving simultaneous equations, akin to Gaussian elimination. Let's translate the problem and procedure into Python code.

### Problem Explanation:
- There are two types of millet: upper millet (上禾) and lower millet (下禾).
- The relationships between the sheaves and yields are given:
  1. 7 sheaves of upper millet lose 1 dou, but when 2 sheaves of lower millet are added, the total yield is 10 dou.
  2. 8 sheaves of lower millet gain 1 dou, but when 2 sheaves of upper millet are added, the total yield is 10 dou.
- The goal is to find the yield of one sheaf of upper millet and one sheaf of lower millet.

### Procedure:
The procedure describes a method for solving the equations step by step. Here's the Python implementation:


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem:
# Equation 1: 7 * (upper millet yield) - 1 + 2 * (lower millet yield) = 10
# Equation 2: 8 * (lower millet yield) + 1 + 2 * (upper millet yield) = 10

# Coefficients for the equations
upper_coeff_1 = 7  # Coefficient of upper millet in equation 1
lower_coeff_1 = 2  # Coefficient of lower millet in equation 1
constant_1 = 10 + 1  # Adjust for the "loss of 1 dou"

lower_coeff_2 = 8  # Coefficient of lower millet in equation 2
upper_coeff_2 = 2  # Coefficient of upper millet in equation 2
constant_2 = 10 - 1  # Adjust for the "gain of 1 dou"

# Solve the system of equations using the procedure described:
# Step 1: Eliminate one variable (e.g., lower millet yield) by multiplying and subtracting equations.

# Multiply equation 1 by the lower coefficient of equation 2 (8)
# Multiply equation 2 by the lower coefficient of equation 1 (2)
# This aligns the coefficients of the lower millet variable for elimination.

multiplier_1 = lower_coeff_2  # 8
multiplier_2 = lower_coeff_1  # 2

# Adjusted equations:
# Equation 1: 8 * (7 * upper millet) + 8 * (2 * lower millet) = 8 * constant_1
# Equation 2: 2 * (2 * upper millet) + 2 * (8 * lower millet) = 2 * constant_2

upper_term_1 = multiplier_1 * upper_coeff_1  # 8 * 7
lower_term_1 = multiplier_1 * lower_coeff_1  # 8 * 2
result_1 = multiplier_1 * constant_1  # 8 * constant_1

upper_term_2 = multiplier_2 * upper_coeff_2  # 2 * 2
lower_term_2 = multiplier_2 * lower_coeff_2  # 2 * 8
result_2 = multiplier_2 * constant_2  # 2 * constant_2

# Subtract the two equations to eliminate the lower millet variable:
# (upper_term_1 - upper_term_2) * upper millet = result_1 - result_2
upper_coefficient = upper_term_1 - upper_term_2
result_difference = result_1 - result_2

# Solve for the yield of one sheaf of upper millet:
upper_millet_yield = Fraction(result_difference, upper_coefficient)

# Substitute the value of upper millet yield back into one of the original equations to solve for lower millet yield:
# Using equation 1: 7 * (upper millet yield) - 1 + 2 * (lower millet yield) = 10
lower_millet_yield = Fraction(constant_1 - upper_coeff_1 * upper_millet_yield, lower_coeff_1)

# Results:
a = 1  # Upper millet sheaf count
b = upper_millet_yield  # Yield of one upper millet sheaf
c = 1  # Lower millet sheaf count
d = lower_millet_yield  # Yield of one lower millet sheaf

# Output the results
print(f"上禾 {a}秉 實 {b}斗 下禾 {c}秉 實 {d}斗")


"""


### Explanation of the Code:
1. The coefficients of the equations are derived from the problem statement.
2. The system of equations is solved step by step using elimination, as described in the procedure.
3. The results are expressed as fractions to ensure accuracy.

### Answer:
The yield of one sheaf of upper millet is `b` dou, and the yield of one sheaf of lower millet is `d` dou.
"""


"""
"""
