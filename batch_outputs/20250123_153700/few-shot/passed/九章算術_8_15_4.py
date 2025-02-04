"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step.

### Problem Setup
We are given three equations:
1. 1令 + 5吏 + 10從者 = 10雞
2. 10令 + 1吏 + 5從者 = 8雞
3. 5令 + 10吏 + 1從者 = 6雞

We need to solve for how many chickens each person (令, 吏, 從者) consumes.

### Procedure
The procedure uses elimination to reduce the system of equations step by step, eventually solving for each variable.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 令 + 5吏 + 10從者 = 10
eq1 = [1, 5, 10, 10]

# Equation 2: 10令 + 1吏 + 5從者 = 8
eq2 = [10, 1, 5, 8]

# Equation 3: 5令 + 10吏 + 1從者 = 6
eq3 = [5, 10, 1, 6]

# Step 1: Normalize the first equation (divide by the coefficient of 令 in eq1)
factor = eq1[0]
eq1 = [Fraction(term, factor) for term in eq1]

# Step 2: Eliminate 令 from eq2 and eq3
factor = eq2[0]
eq2 = [eq2[i] - factor * eq1[i] for i in range(4)]

factor = eq3[0]
eq3 = [eq3[i] - factor * eq1[i] for i in range(4)]

# Step 3: Normalize the second equation (divide by the coefficient of 吏 in eq2)
factor = eq2[1]
eq2 = [Fraction(term, factor) for term in eq2]

# Step 4: Eliminate 吏 from eq3
factor = eq3[1]
eq3 = [eq3[i] - factor * eq2[i] for i in range(4)]

# Step 5: Solve for 從者 (last variable)
c = Fraction(eq3[3], eq3[2])

# Step 6: Solve for 吏 (second variable)
b = eq2[3] - eq2[2] * c

# Step 7: Solve for 令 (first variable)
a = eq1[3] - eq1[2] * c - eq1[1] * b

# Results
print(f"令一人食 {a} 雞")
print(f"吏一人食 {b} 雞")
print(f"從者一人食 {c} 雞")


"""


### Explanation of the Code
1. **Normalization**: Each equation is divided by the coefficient of the leading variable to simplify calculations.
2. **Elimination**: Variables are systematically eliminated from the equations below the current one.
3. **Back-substitution**: Once the last variable is solved, substitute it back into the previous equations to solve for the remaining variables.

### Answer
The output will give the number of chickens consumed by each person:
- 令 (a)
- 吏 (b)
- 從者 (c)
"""


"""
"""
