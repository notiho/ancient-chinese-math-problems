"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a(=45/122)雞 ，吏一人食 b(=41/122)雞 ，從者一人食 c(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Here's the solution translated into Python code:

### Problem Description:
We are tasked with determining how many chickens are eaten by a single "Ling" (令), a single "Li" (吏), and a single "Follower" (從者), given the following constraints:

1. 1 Ling, 5 Li, and 10 Followers eat 10 chickens.
2. 10 Ling, 1 Li, and 5 Followers eat 8 chickens.
3. 5 Ling, 10 Li, and 1 Follower eat 6 chickens.

### Procedure:
The ancient method involves systematically eliminating variables to solve the system of equations. Below is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 令 (Ling), 吏 (Li), 從者 (Follower)
# Equation 1: 1令 + 5吏 + 10從者 = 10
eq1 = [1, 5, 10, 10]

# Equation 2: 10令 + 1吏 + 5從者 = 8
eq2 = [10, 1, 5, 8]

# Equation 3: 5令 + 10吏 + 1從者 = 6
eq3 = [5, 10, 1, 6]

# Step 1: Eliminate the first variable (令) from eq2 and eq3
factor1 = Fraction(eq2[0], eq1[0])  # Factor to eliminate 令 from eq2
factor2 = Fraction(eq3[0], eq1[0])  # Factor to eliminate 令 from eq3

# Subtract eq1 * factor1 from eq2
eq2 = [eq2[i] - factor1 * eq1[i] for i in range(4)]

# Subtract eq1 * factor2 from eq3
eq3 = [eq3[i] - factor2 * eq1[i] for i in range(4)]

# Step 2: Eliminate the second variable (吏) from eq3
factor3 = Fraction(eq3[1], eq2[1])  # Factor to eliminate 吏 from eq3

# Subtract eq2 * factor3 from eq3
eq3 = [eq3[i] - factor3 * eq2[i] for i in range(4)]

# Step 3: Solve for 從者 (Follower) in eq3
c = Fraction(eq3[3], eq3[2])  # 從者 = eq3[3] / eq3[2]

# Step 4: Solve for 吏 (Li) in eq2
b = Fraction(eq2[3] - eq2[2] * c, eq2[1])  # 吏 = (eq2[3] - eq2[2] * 從者) / eq2[1]

# Step 5: Solve for 令 (Ling) in eq1
a = Fraction(eq1[3] - eq1[2] * c - eq1[1] * b, eq1[0])  # 令 = (eq1[3] - eq1[2] * 從者 - eq1[1] * 吏) / eq1[0]

# Results
a, b, c  # 令, 吏, 從者
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initialization**: The equations are represented as lists, where the first three elements are the coefficients of the variables (令, 吏, 從者), and the last element is the constant term.
2. **Elimination**: Using the ancient method, variables are systematically eliminated by subtracting scaled versions of one equation from another.
3. **Back-Substitution**: After eliminating variables, the remaining equations are solved in reverse order to find the values of the variables.

### Final Answer:
- 令 (Ling) eats \( a = \frac{45}{122} \) chickens.
- 吏 (Li) eats \( b = \frac{41}{122} \) chickens.
- 從者 (Follower) eats \( c = \frac{97}{122} \) chickens.
"""


"""
"""
