"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to determine how many chickens each type of person (令, 吏, 從者) eats.

The equations are:
1. \( 1a + 5b + 10c = 10 \)
2. \( 10a + 1b + 5c = 8 \)
3. \( 5a + 10b + 1c = 6 \)

Here is the Python code to compute the values of \( a \), \( b \), and \( c \):


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: a + 5b + 10c = 10
# Equation 2: 10a + b + 5c = 8
# Equation 3: 5a + 10b + c = 6

# Solve using substitution/elimination
# Step 1: Eliminate one variable (e.g., c) from two equations
# Multiply equations to align coefficients of c
eq1 = [1, 5, 10, 10]  # a, b, c, constant
eq2 = [10, 1, 5, 8]
eq3 = [5, 10, 1, 6]

# Eliminate c using eq1 and eq2
factor1 = eq2[2]  # Coefficient of c in eq2
factor2 = eq1[2]  # Coefficient of c in eq1
eq1_scaled = [factor1 * x for x in eq1]
eq2_scaled = [factor2 * x for x in eq2]
eq1_eq2 = [eq2_scaled[i] - eq1_scaled[i] for i in range(4)]  # New equation without c

# Eliminate c using eq1 and eq3
factor1 = eq3[2]  # Coefficient of c in eq3
factor2 = eq1[2]  # Coefficient of c in eq1
eq1_scaled = [factor1 * x for x in eq1]
eq3_scaled = [factor2 * x for x in eq3]
eq1_eq3 = [eq3_scaled[i] - eq1_scaled[i] for i in range(4)]  # New equation without c

# Now we have two equations with two variables (a and b):
# eq1_eq2: [10, -49, 0, -42] -> 10a - 49b = -42
# eq1_eq3: [50, -95, 0, -54] -> 50a - 95b = -54

# Eliminate b to solve for a
factor1 = eq1_eq3[1]  # Coefficient of b in eq1_eq3
factor2 = eq1_eq2[1]  # Coefficient of b in eq1_eq2
eq1_eq2_scaled = [factor1 * x for x in eq1_eq2]
eq1_eq3_scaled = [factor2 * x for x in eq1_eq3]
eq2_eq3 = [eq1_eq3_scaled[i] - eq1_eq2_scaled[i] for i in range(4)]  # New equation without b

# eq2_eq3: [950, 0, 0, -114] -> 950a = -114
a = Fraction(eq2_eq3[3], eq2_eq3[0])  # Solve for a

# Substitute a back into eq1_eq2 to solve for b
b = Fraction(eq1_eq2[3] - eq1_eq2[0] * a, eq1_eq2[1])

# Substitute a and b back into eq1 to solve for c
c = Fraction(eq1[3] - eq1[0] * a - eq1[1] * b, eq1[2])

# Results
a = float(a)
b = float(b)
c = float(c)

print(f"a = {a}, b = {b}, c = {c}")
#----- content ends here -----


"""


This code solves the system of equations step by step using substitution and elimination. The results for \( a \), \( b \), and \( c \) represent the number of chickens each type of person eats.
"""


"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 0.36885245901639346
Variable 'b' has wrong value. Expected: 41/122, Actual: 0.3360655737704918
Variable 'c' has wrong value. Expected: 97/122, Actual: 0.7950819672131147"""
