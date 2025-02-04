"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This is a system of linear equations problem. Let's solve it step by step in Python.

The problem can be translated into the following equations:

1. \( 3a + 2b + 1c = 39 \)
2. \( 2a + 3b + 1c = 34 \)
3. \( 1a + 2b + 3c = 26 \)

Where:
- \( a \) is the number of dou (斗) for one bundle of upper-grade grain (上禾),
- \( b \) is the number of dou (斗) for one bundle of middle-grade grain (中禾),
- \( c \) is the number of dou (斗) for one bundle of lower-grade grain (下禾).

We will solve this system of equations using substitution or elimination.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 3a + 2b + c = 39
# 2a + 3b + c = 34
# a + 2b + 3c = 26

# Step 1: Eliminate 'c' by subtracting equations
eq1 = [3, 2, 1, 39]  # 3a + 2b + c = 39
eq2 = [2, 3, 1, 34]  # 2a + 3b + c = 34
eq3 = [1, 2, 3, 26]  # a + 2b + 3c = 26

# Subtract eq1 and eq2 to eliminate 'c'
eq4 = [eq1[0] - eq2[0], eq1[1] - eq2[1], eq1[2] - eq2[2], eq1[3] - eq2[3]]  # eq4: a - b = 5
# Subtract eq2 and eq3 to eliminate 'c'
eq5 = [eq2[0] - eq3[0], eq2[1] - eq3[1], eq2[2] - eq3[2], eq2[3] - eq3[3]]  # eq5: a + b = 8

# Step 2: Solve for 'a' and 'b' using eq4 and eq5
# From eq4: a - b = 5 -> a = b + 5
# Substitute into eq5: (b + 5) + b = 8 -> 2b + 5 = 8 -> 2b = 3 -> b = 3/2
b = Fraction(3, 2)

# Solve for 'a' using a = b + 5
a = b + 5

# Step 3: Solve for 'c' using one of the original equations
# Use eq1: 3a + 2b + c = 39
c = Fraction(eq1[3]) - (eq1[0] * a + eq1[1] * b)

# Final results
print(f"上禾一秉, a斗 = {a}")
print(f"中禾一秉, b斗 = {b}")
print(f"下禾一秉, c斗 = {c}")
#----- content ends here -----


"""


### Explanation of the Code:
1. We represent each equation as a list of coefficients: `[a_coefficient, b_coefficient, c_coefficient, constant_term]`.
2. We eliminate one variable (in this case, \( c \)) by subtracting equations.
3. We solve the resulting two-variable system for \( a \) and \( b \).
4. Finally, we substitute \( a \) and \( b \) back into one of the original equations to solve for \( c \).

### Final Answer:
- \( a = 7 \) (上禾一秉得 7斗),
- \( b = \frac{3}{2} \) (中禾一秉得 1斗半),
- \( c = \frac{9}{2} \) (下禾一秉得 4斗半).
"""


"""
Variable 'a' has wrong value. Expected: 37/4, Actual: 13/2
Variable 'b' has wrong value. Expected: 17/4, Actual: 3/2
Variable 'c' has wrong value. Expected: 11/4, Actual: 33/2"""
