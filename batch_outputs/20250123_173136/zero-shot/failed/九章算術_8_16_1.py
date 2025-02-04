"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into a system of linear equations and solve for the unknowns \( a \), \( b \), \( c \), and \( d \), which represent the prices of sheep, dogs, chickens, and rabbits, respectively. Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem statement:
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Solve the system of equations using substitution/elimination:

# Step 1: Eliminate one variable (e.g., "a") from all but one equation.
# Multiply equations to align coefficients of "a" and subtract:
# Multiply the first equation by 4 and the second equation by 5:
eq1 = [5, 4, 3, 2, 1496]
eq2 = [4, 2, 6, 3, 1175]
eq3 = [3, 1, 7, 5, 958]
eq4 = [2, 3, 5, 1, 861]

# Eliminate "a" between eq1 and eq2:
eq1_scaled = [x * 4 for x in eq1]
eq2_scaled = [x * 5 for x in eq2]
eq5 = [eq1_scaled[i] - eq2_scaled[i] for i in range(5)]  # Resulting equation

# Eliminate "a" between eq1 and eq3:
eq1_scaled = [x * 3 for x in eq1]
eq3_scaled = [x * 5 for x in eq3]
eq6 = [eq1_scaled[i] - eq3_scaled[i] for i in range(5)]  # Resulting equation

# Eliminate "a" between eq1 and eq4:
eq1_scaled = [x * 2 for x in eq1]
eq4_scaled = [x * 5 for x in eq4]
eq7 = [eq1_scaled[i] - eq4_scaled[i] for i in range(5)]  # Resulting equation

# Step 2: Eliminate another variable (e.g., "b") from the resulting equations.
# Use eq5, eq6, and eq7 to eliminate "b":
# Multiply equations to align coefficients of "b" and subtract:
eq5_scaled = [x * 3 for x in eq5]
eq6_scaled = [x * 2 for x in eq6]
eq8 = [eq5_scaled[i] - eq6_scaled[i] for i in range(5)]  # Resulting equation

eq5_scaled = [x * 3 for x in eq5]
eq7_scaled = [x * 4 for x in eq7]
eq9 = [eq5_scaled[i] - eq7_scaled[i] for i in range(5)]  # Resulting equation

# Step 3: Solve for one variable (e.g., "d") using the resulting equations.
# Use eq8 and eq9 to solve for "d":
# Multiply equations to align coefficients of "d" and subtract:
eq8_scaled = [x * 7 for x in eq8]
eq9_scaled = [x * 6 for x in eq9]
eq10 = [eq8_scaled[i] - eq9_scaled[i] for i in range(5)]  # Resulting equation

# Solve for "d":
d = Fraction(eq10[4], eq10[3])

# Step 4: Back-substitute to solve for "c", "b", and "a":
# Substitute "d" into eq8 to solve for "c":
c = Fraction(eq8[4] - eq8[3] * d, eq8[2])

# Substitute "c" and "d" into eq5 to solve for "b":
b = Fraction(eq5[4] - eq5[3] * d - eq5[2] * c, eq5[1])

# Substitute "b", "c", and "d" into eq1 to solve for "a":
a = Fraction(eq1[4] - eq1[3] * d - eq1[2] * c - eq1[1] * b, eq1[0])

# The results:
a = float(a)
b = float(b)
c = float(c)
d = float(d)


"""

"""


"""
Variable 'a' has wrong value. Expected: 177, Actual: 4954.226244343891
Variable 'b' has wrong value. Expected: 121, Actual: -4631.06334841629
Variable 'c' has wrong value. Expected: 23, Actual: -1502.3076923076924
Variable 'd' has wrong value. Expected: 29, Actual: -121.97737556561086"""
