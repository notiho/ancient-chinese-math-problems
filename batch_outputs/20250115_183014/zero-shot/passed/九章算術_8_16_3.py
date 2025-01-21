"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to translate the ancient Chinese mathematical problem into a system of linear equations and solve for the unknowns \(a\), \(b\), \(c\), and \(d\), which represent the prices of sheep, dogs, chickens, and rabbits, respectively.

The problem gives us four equations:

1. \(5a + 4b + 3c + 2d = 1496\)
2. \(4a + 2b + 6c + 3d = 1175\)
3. \(3a + b + 7c + 5d = 958\)
4. \(2a + 3b + 5c + d = 861\)

We will solve this system of linear equations using Python. Here's the code:


"""


from fractions import Fraction

# Define the coefficients of the equations
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a +  b + 7c + 5d =  958
# 2a + 3b + 5c +  d =  861

# Using elimination to solve the system of equations step by step

# Step 1: Eliminate 'a' from the second, third, and fourth equations
factor1 = Fraction(4, 5)  # Multiply the first equation by 4/5
factor2 = Fraction(3, 5)  # Multiply the first equation by 3/5
factor3 = Fraction(2, 5)  # Multiply the first equation by 2/5

eq2 = [4 - factor1 * 5, 2 - factor1 * 4, 6 - factor1 * 3, 3 - factor1 * 2, 1175 - factor1 * 1496]
eq3 = [3 - factor2 * 5, 1 - factor2 * 4, 7 - factor2 * 3, 5 - factor2 * 2, 958 - factor2 * 1496]
eq4 = [2 - factor3 * 5, 3 - factor3 * 4, 5 - factor3 * 3, 1 - factor3 * 2, 861 - factor3 * 1496]

# Step 2: Eliminate 'b' from the third and fourth equations
factor4 = Fraction(eq3[1], eq2[1])  # Multiply the second equation by eq3[1] / eq2[1]
factor5 = Fraction(eq4[1], eq2[1])  # Multiply the second equation by eq4[1] / eq2[1]

eq3 = [eq3[0] - factor4 * eq2[0], 0, eq3[2] - factor4 * eq2[2], eq3[3] - factor4 * eq2[3], eq3[4] - factor4 * eq2[4]]
eq4 = [eq4[0] - factor5 * eq2[0], 0, eq4[2] - factor5 * eq2[2], eq4[3] - factor5 * eq2[3], eq4[4] - factor5 * eq2[4]]

# Step 3: Eliminate 'c' from the fourth equation
factor6 = Fraction(eq4[2], eq3[2])  # Multiply the third equation by eq4[2] / eq3[2]

eq4 = [eq4[0] - factor6 * eq3[0], 0, 0, eq4[3] - factor6 * eq3[3], eq4[4] - factor6 * eq3[4]]

# Step 4: Back-substitute to solve for 'd', 'c', 'b', and 'a'
d = Fraction(eq4[4], eq4[3])
c = Fraction(eq3[4] - eq3[3] * d, eq3[2])
b = Fraction(eq2[4] - eq2[3] * d - eq2[2] * c, eq2[1])
a = Fraction(1496 - 4 * b - 3 * c - 2 * d, 5)

# The solutions
a, b, c, d


"""


This code solves the system of equations step by step using the elimination method and represents the solutions as fractions for exactness. The variables \(a\), \(b\), \(c\), and \(d\) will contain the prices of the sheep, dogs, chickens, and rabbits, respectively.
"""


"""
"""
