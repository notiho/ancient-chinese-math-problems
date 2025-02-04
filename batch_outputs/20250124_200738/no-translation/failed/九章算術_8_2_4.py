"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step, adhering to the structure of the procedure ("術"). The problem involves solving a system of linear equations using the described method.


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the number of秉 (bundles) for each type of禾 (grain)
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# Step 2: Define the total斗 (volume) when the grains are redistributed
總斗數 = 39

# Step 3: Set up the equations based on the problem description
# Let a, b, c represent the斗 (volume) of one秉 (bundle) of上禾, 中禾, and下禾 respectively.
# The equations are:
# 2a + b = 39 (redistribution of上禾)
# 3b + c = 39 (redistribution of中禾)
# 4c + a = 39 (redistribution of下禾)

# Step 4: Solve the system of equations using the described method
# Initialize the coefficients and constants for the equations
A = [
    [2, 1, 0],  # Coefficients for the first equation
    [0, 3, 1],  # Coefficients for the second equation
    [1, 0, 4]   # Coefficients for the third equation
]
B = [39, 39, 39]  # Constants on the right-hand side of the equations

# Step 5: Use elimination to solve for c (下禾)
# Multiply the first equation by 4 (下禾秉數) and subtract the third equation
A[0] = [4 * x for x in A[0]]
B[0] = 4 * B[0]
A[0] = [A[0][i] - A[2][i] for i in range(3)]
B[0] = B[0] - B[2]

# Step 6: Use elimination to solve for b (中禾)
# Multiply the second equation by 4 (下禾秉數) and subtract the third equation
A[1] = [4 * x for x in A[1]]
B[1] = 4 * B[1]
A[1] = [A[1][i] - A[2][i] for i in range(3)]
B[1] = B[1] - B[2]

# Step 7: Solve for c (下禾)
c = Fraction(B[2], A[2][2])

# Step 8: Solve for b (中禾)
b = Fraction(B[1] - A[1][2] * c, A[1][1])

# Step 9: Solve for a (上禾)
a = Fraction(B[0] - A[0][1] * b - A[0][2] * c, A[0][0])

# Results
a斗 = a
b斗 = b
c斗 = c

# Output the results
a斗, b斗, c斗
#----- content ends here -----


"""


### Explanation of the Code:
1. **Setting up the equations**: The problem is translated into a system of three linear equations based on the redistribution of grains.
2. **Elimination method**: The described method is implemented step by step to eliminate variables and solve for each unknown.
3. **Fractions**: The `Fraction` class is used to ensure precise calculations without rounding errors.
4. **Results**: The斗 (volume) of one秉 (bundle) for each type of禾 (grain) is calculated and output.

### Final Answer:
- 上禾一秉實 `a斗`
- 中禾一秉實 `b斗`
- 下禾一秉實 `c斗`
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 117/7
Variable 'b' has wrong value. Expected: 7/25, Actual: 39/4
Variable 'c' has wrong value. Expected: 4/25, Actual: 39/4"""
