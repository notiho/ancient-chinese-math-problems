"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we will translate the given system of linear equations into Python code. The equations represent the prices of sheep (`a`), dogs (`b`), chickens (`c`), and rabbits (`d`) in terms of their total values. We'll use the `Fraction` class to ensure precise calculations.

The equations are:
1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

Here is the Python code to solve for \( a \), \( b \), \( c \), and \( d \):


"""


from fractions import Fraction

# Coefficients of the equations
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Using elimination to solve the system of equations
# Step 1: Eliminate one variable at a time

# Multiply equations to align coefficients for elimination
eq1 = [5, 4, 3, 2, 1496]
eq2 = [4, 2, 6, 3, 1175]
eq3 = [3, 1, 7, 5, 958]
eq4 = [2, 3, 5, 1, 861]

# Eliminate 'a' from eq2, eq3, and eq4 using eq1
factor2 = Fraction(eq2[0], eq1[0])
factor3 = Fraction(eq3[0], eq1[0])
factor4 = Fraction(eq4[0], eq1[0])

eq2 = [eq2[i] - factor2 * eq1[i] for i in range(5)]
eq3 = [eq3[i] - factor3 * eq1[i] for i in range(5)]
eq4 = [eq4[i] - factor4 * eq1[i] for i in range(5)]

# Eliminate 'b' from eq3 and eq4 using eq2
factor3 = Fraction(eq3[1], eq2[1])
factor4 = Fraction(eq4[1], eq2[1])

eq3 = [eq3[i] - factor3 * eq2[i] for i in range(5)]
eq4 = [eq4[i] - factor4 * eq2[i] for i in range(5)]

# Eliminate 'c' from eq4 using eq3
factor4 = Fraction(eq4[2], eq3[2])

eq4 = [eq4[i] - factor4 * eq3[i] for i in range(5)]

# Back-substitute to solve for d, c, b, and a
d = Fraction(eq4[4], eq4[3])
c = Fraction(eq3[4] - eq3[3] * d, eq3[2])
b = Fraction(eq2[4] - eq2[3] * d - eq2[2] * c, eq2[1])
a = Fraction(eq1[4] - eq1[3] * d - eq1[2] * c - eq1[1] * b, eq1[0])

# Print the results
a, b, c, d


"""


### Explanation:
1. We start with the four equations and eliminate variables step by step using the method of substitution and elimination.
2. Fractions are used to ensure precise calculations without rounding errors.
3. After eliminating variables, we back-substitute to find the values of \( d \), \( c \), \( b \), and \( a \).

### Results:
The variables \( a \), \( b \), \( c \), and \( d \) will hold the respective prices of sheep, dogs, chickens, and rabbits in terms of money.
"""


"""
"""
