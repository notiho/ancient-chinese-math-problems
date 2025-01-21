"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾 a秉  b斗 中禾 c秉  d斗 下禾 e秉  f斗 
"""

"""
This problem involves solving a system of linear equations to determine the yield of each type of grain (upper, middle, and lower) per bundle. The procedure described corresponds to solving the equations step by step. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Given equations:
# 3上禾 + 2中禾 + 1下禾 = 39斗
# 2上禾 + 3中禾 + 1下禾 = 34斗
# 1上禾 + 2中禾 + 3下禾 = 26斗

# Step 1: Represent the coefficients and constants
coefficients = [
    [3, 2, 1],  # Coefficients for the first equation
    [2, 3, 1],  # Coefficients for the second equation
    [1, 2, 3]   # Coefficients for the third equation
]
constants = [39, 34, 26]  # Constants on the right-hand side

# Step 2: Eliminate the first variable (上禾) from the second and third equations
# Multiply the first row by 2 and subtract from the second row
coefficients[1] = [
    coefficients[1][i] * 3 - coefficients[0][i] * 2 for i in range(3)
]
constants[1] = constants[1] * 3 - constants[0] * 2

# Multiply the first row by 1 and subtract from the third row
coefficients[2] = [
    coefficients[2][i] * 3 - coefficients[0][i] * 1 for i in range(3)
]
constants[2] = constants[2] * 3 - constants[0] * 1

# Step 3: Eliminate the second variable (中禾) from the third equation
# Multiply the second row by 3 and subtract from the third row
coefficients[2] = [
    coefficients[2][i] * 3 - coefficients[1][i] * 1 for i in range(3)
]
constants[2] = constants[2] * 3 - constants[1] * 1

# Step 4: Solve for the third variable (下禾)
下禾 = Fraction(constants[2], coefficients[2][2])

# Step 5: Solve for the second variable (中禾)
中禾 = Fraction(constants[1] - coefficients[1][2] * 下禾, coefficients[1][1])

# Step 6: Solve for the first variable (上禾)
上禾 = Fraction(constants[0] - coefficients[0][2] * 下禾 - coefficients[0][1] * 中禾, coefficients[0][0])

# Results
a, b = 1, 上禾  # 上禾 per bundle
c, d = 1, 中禾  # 中禾 per bundle
e, f = 1, 下禾  # 下禾 per bundle

# Output
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Step 1:** The coefficients of the equations and the constants are represented as lists.
2. **Step 2:** The first variable (上禾) is eliminated from the second and third equations using row operations.
3. **Step 3:** The second variable (中禾) is eliminated from the third equation.
4. **Step 4:** The third variable (下禾) is solved using the simplified third equation.
5. **Step 5:** The second variable (中禾) is solved using the simplified second equation.
6. **Step 6:** The first variable (上禾) is solved using the simplified first equation.

### Answer:
The result will give the yield per bundle for each type of grain:
- 上禾: `a` bundles, `b` dou
- 中禾: `c` bundles, `d` dou
- 下禾: `e` bundles, `f` dou
"""


"""
Variable 'b' has wrong value. Expected: 37/4, Actual: 1034/115
Variable 'd' has wrong value. Expected: 17/4, Actual: 459/115
Variable 'f' has wrong value. Expected: 11/4, Actual: 93/23"""
