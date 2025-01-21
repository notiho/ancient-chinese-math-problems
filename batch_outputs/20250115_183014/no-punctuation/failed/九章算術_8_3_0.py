"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 b升 下禾 c秉 d升 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "fangcheng" (similar to modern linear algebra). Let's break it down step by step and encode the solution in Python.

### Problem Description:
We are given:
1. 5 bundles of upper millet lose 1 dou and 1 sheng of grain when compared to 7 bundles of lower millet.
2. 7 bundles of upper millet lose 2 dou and 5 sheng of grain when compared to 5 bundles of lower millet.

We are tasked to find the amount of grain in one bundle of upper millet and one bundle of lower millet.

### Procedure:
The "fangcheng" method involves setting up equations and solving them systematically. The steps are:
1. Represent the problem as a system of equations.
2. Use elimination and substitution to solve for the unknowns.

The equations are:
- \( 5x - 7y = 1 \, \text{dou} \, 1 \, \text{sheng} \)
- \( 7x - 5y = 2 \, \text{dou} \, 5 \, \text{sheng} \)

Where:
- \( x \) is the grain in one bundle of upper millet.
- \( y \) is the grain in one bundle of lower millet.

### Python Code:

"""


from fractions import Fraction

# Convert dou and sheng into a single unit (sheng)
# 1 dou = 10 sheng
損實1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
損實2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Coefficients for the equations
# Equation 1: 5x - 7y = 損實1
# Equation 2: 7x - 5y = 損實2
上禾1 = 5
下禾1 = -7
上禾2 = 7
下禾2 = -5

# Step 1: Eliminate one variable (use the fangcheng method)
# Multiply the first equation by 7 (coefficient of x in the second equation)
# Multiply the second equation by 5 (coefficient of x in the first equation)
eq1_multiplier = 上禾2  # 7
eq2_multiplier = 上禾1  # 5

# New equations after elimination
new_eq1 = (eq1_multiplier * 上禾1, eq1_multiplier * 下禾1, eq1_multiplier * 損實1)
new_eq2 = (eq2_multiplier * 上禾2, eq2_multiplier * 下禾2, eq2_multiplier * 損實2)

# Subtract the two equations to eliminate x
# (7 * 5x - 7 * 7y) - (5 * 7x - 5 * 5y) = (7 * 損實1) - (5 * 損實2)
combined_coeff_y = new_eq1[1] - new_eq2[1]
combined_constant = new_eq1[2] - new_eq2[2]

# Solve for y (grain in one bundle of lower millet)
y = Fraction(combined_constant, combined_coeff_y)

# Step 2: Substitute y back into one of the original equations to solve for x
# Use the first equation: 5x - 7y = 損實1
x = Fraction(損實1 - 下禾1 * y, 上禾1)

# Convert x and y back to dou and sheng
a_dou = x // 10
a_sheng = x % 10
c_dou = y // 10
c_sheng = y % 10

# Output the results
a, b = a_dou, a_sheng  # Upper millet: a dou, b sheng
c, d = c_dou, c_sheng  # Lower millet: c dou, d sheng

print(f"上禾 {a}斗 {b}升 下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Unit Conversion**: Convert dou and sheng into a single unit (sheng) for easier calculations.
2. **Set Up Equations**: Represent the problem as two linear equations.
3. **Elimination**: Use the "fangcheng" method to eliminate one variable and solve for the other.
4. **Back Substitution**: Substitute the solved variable back into one of the original equations to find the other variable.
5. **Result Conversion**: Convert the results back into dou and sheng for the final answer.

### Final Answer:
The output will provide the amount of grain in one bundle of upper millet (\( a \) dou and \( b \) sheng) and one bundle of lower millet (\( c \) dou and \( d \) sheng).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
