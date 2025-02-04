"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of upper, middle, and lower grade grain. Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# 3a + 2b + 1c = 39
# 2a + 3b + 1c = 34
# 1a + 2b + 3c = 26

# Coefficients of the equations
coefficients = [
    [3, 2, 1],
    [2, 3, 1],
    [1, 2, 3]
]

# Results of the equations
results = [39, 34, 26]

# Solve using substitution or elimination
# We'll use a manual approach to solve this system of equations.

# Step 1: Eliminate 'a' from the second and third equations
factor1 = Fraction(coefficients[1][0], coefficients[0][0])  # Factor to eliminate 'a' from the second equation
factor2 = Fraction(coefficients[2][0], coefficients[0][0])  # Factor to eliminate 'a' from the third equation

# Update the second equation
coefficients[1] = [
    coefficients[1][i] - factor1 * coefficients[0][i] for i in range(3)
]
results[1] -= factor1 * results[0]

# Update the third equation
coefficients[2] = [
    coefficients[2][i] - factor2 * coefficients[0][i] for i in range(3)
]
results[2] -= factor2 * results[0]

# Step 2: Eliminate 'b' from the third equation
factor3 = Fraction(coefficients[2][1], coefficients[1][1])  # Factor to eliminate 'b' from the third equation

coefficients[2] = [
    coefficients[2][i] - factor3 * coefficients[1][i] for i in range(3)
]
results[2] -= factor3 * results[1]

# Step 3: Solve for 'c'
c = Fraction(results[2], coefficients[2][2])

# Step 4: Solve for 'b'
b = Fraction(results[1] - coefficients[1][2] * c, coefficients[1][1])

# Step 5: Solve for 'a'
a = Fraction(results[0] - coefficients[0][1] * b - coefficients[0][2] * c, coefficients[0][0])

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. We represent the system of equations as a matrix of coefficients and a results vector.
2. Using substitution and elimination, we reduce the system step by step to solve for `a`, `b`, and `c`.
3. The final values of `a`, `b`, and `c` represent the yield of one sheaf of upper, middle, and lower grade grain, respectively, in dou.

### Answer:
- 上禾一秉: `a` dou
- 中禾一秉: `b` dou
- 下禾一秉: `c` dou
"""


"""
"""
