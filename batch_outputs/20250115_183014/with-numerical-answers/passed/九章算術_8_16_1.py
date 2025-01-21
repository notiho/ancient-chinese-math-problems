"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
To solve this problem, we will use a system of linear equations based on the given values for sheep (羊), dogs (犬), chickens (雞), and rabbits (兔). The problem is essentially a linear algebra problem, and we will solve it step by step using the method described in the procedure.

The equations are as follows:
1. \( 5羊 + 4犬 + 3雞 + 2兔 = 1496 \)
2. \( 4羊 + 2犬 + 6雞 + 3兔 = 1175 \)
3. \( 3羊 + 1犬 + 7雞 + 5兔 = 958 \)
4. \( 2羊 + 3犬 + 5雞 + 1兔 = 861 \)

We will solve for the values of \( 羊 \) (sheep), \( 犬 \) (dog), \( 雞 \) (chicken), and \( 兔 \) (rabbit).


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 5羊 + 4犬 + 3雞 + 2兔 = 1496
eq1 = [5, 4, 3, 2, 1496]

# Equation 2: 4羊 + 2犬 + 6雞 + 3兔 = 1175
eq2 = [4, 2, 6, 3, 1175]

# Equation 3: 3羊 + 1犬 + 7雞 + 5兔 = 958
eq3 = [3, 1, 7, 5, 958]

# Equation 4: 2羊 + 3犬 + 5雞 + 1兔 = 861
eq4 = [2, 3, 5, 1, 861]

# Step 1: Eliminate the first variable (羊) from eq2, eq3, and eq4
# Multiply eq1 by 4 and subtract eq2
eq2 = [eq2[i] * 5 - eq1[i] * 4 for i in range(5)]

# Multiply eq1 by 3 and subtract eq3
eq3 = [eq3[i] * 5 - eq1[i] * 3 for i in range(5)]

# Multiply eq1 by 2 and subtract eq4
eq4 = [eq4[i] * 5 - eq1[i] * 2 for i in range(5)]

# Step 2: Eliminate the second variable (犬) from eq3 and eq4
# Multiply eq2 by 1 and subtract eq3
eq3 = [eq3[i] * eq2[1] - eq2[i] * eq3[1] for i in range(5)]

# Multiply eq2 by 3 and subtract eq4
eq4 = [eq4[i] * eq2[1] - eq2[i] * eq4[1] for i in range(5)]

# Step 3: Eliminate the third variable (雞) from eq4
# Multiply eq3 by 5 and subtract eq4
eq4 = [eq4[i] * eq3[2] - eq3[i] * eq4[2] for i in range(5)]

# Step 4: Back-substitute to solve for each variable
# Solve for 兔 (rabbit)
兔 = Fraction(eq4[4], eq4[3])

# Solve for 雞 (chicken) using eq3
雞 = Fraction(eq3[4] - eq3[3] * 兔, eq3[2])

# Solve for 犬 (dog) using eq2
犬 = Fraction(eq2[4] - eq2[3] * 兔 - eq2[2] * 雞, eq2[1])

# Solve for 羊 (sheep) using eq1
羊 = Fraction(eq1[4] - eq1[3] * 兔 - eq1[2] * 雞 - eq1[1] * 犬, eq1[0])

# Convert to integers
a = 羊.numerator  # 177
b = 犬.numerator  # 121
c = 雞.numerator  # 23
d = 兔.numerator  # 29

# Final results
a, b, c, d


"""
 

### Explanation:
1. We use elimination to systematically reduce the system of equations to a single variable.
2. Back-substitution is then used to solve for the remaining variables.
3. The final values are:
   - \( 羊價 = a = 177 \)
   - \( 犬價 = b = 121 \)
   - \( 雞價 = c = 23 \)
   - \( 兔價 = d = 29 \)
"""


"""
"""
