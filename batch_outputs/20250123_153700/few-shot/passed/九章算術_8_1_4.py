"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods. The procedure is akin to Gaussian elimination, where we manipulate rows of a matrix to solve for the unknowns. Let's translate the problem into Python code step by step.

### Problem Explanation:
We are given two equations:
1. For 7 bundles of upper millet (上禾), reducing 1 dou of grain, and adding 2 bundles of lower millet (下禾), the total grain is 10 dou.
2. For 8 bundles of lower millet (下禾), adding 1 dou of grain and 2 bundles of upper millet (上禾), the total grain is 10 dou.

We need to find the grain yield per bundle of upper millet (上禾) and lower millet (下禾).

### Procedure:
The procedure involves setting up the equations, manipulating them, and solving for the unknowns step by step.


"""


from fractions import Fraction

# Define the coefficients and constants of the equations
# Equation 1: 7 * 上禾 - 1 + 2 * 下禾 = 10
# Equation 2: 2 * 上禾 + 8 * 下禾 + 1 = 10

# Rewrite the equations in standard form:
# 7 * 上禾 + 2 * 下禾 = 11
# 2 * 上禾 + 8 * 下禾 = 9

# Coefficients of the equations
coefficients = [
    [7, 2],  # Coefficients of 上禾 and 下禾 in the first equation
    [2, 8]   # Coefficients of 上禾 and 下禾 in the second equation
]

# Constants on the right-hand side
constants = [11, 9]

# Step 1: Eliminate 上禾 from the second equation
# Multiply the first equation by 2 and the second equation by 7
# This makes the coefficients of 上禾 in both equations equal
multiplier1 = 2
multiplier2 = 7

# Scale the equations
scaled_eq1 = [coefficients[0][0] * multiplier1, coefficients[0][1] * multiplier1, constants[0] * multiplier1]
scaled_eq2 = [coefficients[1][0] * multiplier2, coefficients[1][1] * multiplier2, constants[1] * multiplier2]

# Subtract the scaled first equation from the scaled second equation
# This eliminates 上禾 from the second equation
eliminated_eq = [
    scaled_eq2[1] - scaled_eq1[1],  # Coefficient of 下禾
    scaled_eq2[2] - scaled_eq1[2]   # Constant
]

# Step 2: Solve for 下禾
下禾 = Fraction(eliminated_eq[1], eliminated_eq[0])

# Step 3: Solve for 上禾 using the first equation
# Substitute 下禾 into the first equation
上禾 = Fraction(constants[0] - coefficients[0][1] * 下禾, coefficients[0][0])

# Results
a = 上禾
b = 下禾

# Output the results
print(f"上禾一秉實 {a}斗 ，下禾一秉實 {b}斗 。")


"""


### Explanation of the Code:
1. **Equation Setup**: The equations are rewritten in standard form for easier manipulation.
2. **Elimination**: The first variable (上禾) is eliminated from the second equation by scaling and subtracting.
3. **Back Substitution**: The value of 下禾 is substituted back into the first equation to solve for 上禾.
4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Answer:
The output will provide the grain yield per bundle of upper millet (上禾) and lower millet (下禾) in dou.
"""


"""
"""
