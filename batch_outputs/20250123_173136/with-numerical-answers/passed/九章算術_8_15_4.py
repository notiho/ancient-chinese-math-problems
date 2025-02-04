"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a(=45/122)雞 ，吏一人食 b(=41/122)雞 ，從者一人食 c(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese "fangcheng" (method of solving simultaneous equations). Let's translate the problem into Python code step by step.

### Problem Setup:
We are given three equations:
1. A magistrate (令), 5 clerks (吏), and 10 attendants (從者) eat 10 chickens.
2. 10 magistrates, 1 clerk, and 5 attendants eat 8 chickens.
3. 5 magistrates, 10 clerks, and 1 attendant eat 6 chickens.

We need to determine how many chickens each individual (令, 吏, 從者) eats.

### Procedure:
The "fangcheng" method is essentially Gaussian elimination. We'll follow the steps described in the procedure to solve the system of equations.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 令 + 5吏 + 10從者 = 10
eq1 = [1, 5, 10, 10]

# Equation 2: 10令 + 吏 + 5從者 = 8
eq2 = [10, 1, 5, 8]

# Equation 3: 5令 + 10吏 + 從者 = 6
eq3 = [5, 10, 1, 6]

# Step 1: Normalize the first equation (divide by the coefficient of 令 in eq1)
factor = eq1[0]
eq1 = [Fraction(term, factor) for term in eq1]

# Step 2: Eliminate the 令 term from eq2 and eq3
factor = eq2[0]
eq2 = [eq2[i] - factor * eq1[i] for i in range(len(eq1))]

factor = eq3[0]
eq3 = [eq3[i] - factor * eq1[i] for i in range(len(eq1))]

# Step 3: Normalize the second equation (divide by the coefficient of 吏 in eq2)
factor = eq2[1]
eq2 = [Fraction(term, factor) for term in eq2]

# Step 4: Eliminate the 吏 term from eq3
factor = eq3[1]
eq3 = [eq3[i] - factor * eq2[i] for i in range(len(eq2))]

# Step 5: Solve for 從者 (last variable)
從者 = Fraction(eq3[3], eq3[2])

# Step 6: Back-substitute to solve for 吏 (second variable)
吏 = eq2[3] - eq2[2] * 從者

# Step 7: Back-substitute to solve for 令 (first variable)
令 = eq1[3] - eq1[2] * 從者 - eq1[1] * 吏

# Results
a = 令  # 令一人食雞數
b = 吏  # 吏一人食雞數
c = 從者  # 從者一人食雞數

# Output the results
a, b, c  # (45/122, 41/122, 97/122)


"""


### Explanation of the Code:
1. **Normalization**: Each equation is divided by the coefficient of the leading variable to simplify the elimination process.
2. **Elimination**: Subtract multiples of one equation from another to eliminate variables step by step.
3. **Back-substitution**: Once the last variable is solved, substitute it back into the previous equations to solve for the remaining variables.

### Answer:
- A magistrate (令) eats `a = 45/122` chickens.
- A clerk (吏) eats `b = 41/122` chickens.
- An attendant (從者) eats `c = 97/122` chickens.
"""


"""
"""
