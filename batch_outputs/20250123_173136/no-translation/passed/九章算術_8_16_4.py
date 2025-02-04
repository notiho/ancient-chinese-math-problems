"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to use a system of linear equations based on the given data. The equations are derived from the problem statement:

1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

Here, \(a\), \(b\), \(c\), and \(d\) represent the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔), respectively. We will solve this system using the elimination method described in the procedure.


"""


from fractions import Fraction

# Coefficients of the equations
eq1 = [5, 4, 3, 2, 1496]
eq2 = [4, 2, 6, 3, 1175]
eq3 = [3, 1, 7, 5, 958]
eq4 = [2, 3, 5, 1, 861]

# Step 1: Normalize the first equation (divide by the coefficient of a in eq1)
factor = eq1[0]
eq1 = [Fraction(x, factor) for x in eq1]

# Step 2: Eliminate 'a' from eq2, eq3, and eq4
factor = eq2[0]
eq2 = [eq2[i] - factor * eq1[i] for i in range(len(eq1))]

factor = eq3[0]
eq3 = [eq3[i] - factor * eq1[i] for i in range(len(eq1))]

factor = eq4[0]
eq4 = [eq4[i] - factor * eq1[i] for i in range(len(eq1))]

# Step 3: Normalize the second equation (divide by the coefficient of b in eq2)
factor = eq2[1]
eq2 = [Fraction(x, factor) for x in eq2]

# Step 4: Eliminate 'b' from eq3 and eq4
factor = eq3[1]
eq3 = [eq3[i] - factor * eq2[i] for i in range(len(eq2))]

factor = eq4[1]
eq4 = [eq4[i] - factor * eq2[i] for i in range(len(eq2))]

# Step 5: Normalize the third equation (divide by the coefficient of c in eq3)
factor = eq3[2]
eq3 = [Fraction(x, factor) for x in eq3]

# Step 6: Eliminate 'c' from eq4
factor = eq4[2]
eq4 = [eq4[i] - factor * eq3[i] for i in range(len(eq3))]

# Step 7: Solve for 'd' in eq4
d = eq4[4] / eq4[3]

# Step 8: Solve for 'c' in eq3
c = eq3[4] - eq3[3] * d

# Step 9: Solve for 'b' in eq2
b = eq2[4] - eq2[3] * d - eq2[2] * c

# Step 10: Solve for 'a' in eq1
a = eq1[4] - eq1[3] * d - eq1[2] * c - eq1[1] * b

# Results
a, b, c, d


"""


### Explanation of the Code:
1. Each equation is represented as a list of coefficients, including the constant term on the right-hand side.
2. The elimination method is applied step by step to reduce the system to a triangular form.
3. Back-substitution is used to solve for \(d\), \(c\), \(b\), and \(a\) in that order.
4. The results are stored in \(a\), \(b\), \(c\), and \(d\), which represent the prices of sheep, dogs, chickens, and rabbits, respectively.
"""


"""
"""
