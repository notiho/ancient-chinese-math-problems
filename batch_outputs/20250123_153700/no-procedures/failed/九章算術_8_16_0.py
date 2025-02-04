"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. Let's translate this into Python code.


"""


from fractions import Fraction

# Let the prices of sheep, dogs, chickens, and rabbits be a, b, c, and d respectively.
# The equations based on the problem are:
# 1. 5a + 4b + 3c + 2d = 1496
# 2. 4a + 2b + 6c + 3d = 1175
# 3. 3a + 1b + 7c + 5d = 958
# 4. 2a + 3b + 5c + 1d = 861

# Solve the system of equations using substitution or elimination.

# Step 1: Express the equations in terms of a, b, c, and d.
# We'll use elimination to solve this step by step.

# Multiply the equations to align coefficients for elimination:
# Multiply the first equation by 2 and the second equation by 4 to eliminate b.

eq1 = [5, 4, 3, 2, 1496]  # 5a + 4b + 3c + 2d = 1496
eq2 = [4, 2, 6, 3, 1175]  # 4a + 2b + 6c + 3d = 1175
eq3 = [3, 1, 7, 5, 958]   # 3a + 1b + 7c + 5d = 958
eq4 = [2, 3, 5, 1, 861]   # 2a + 3b + 5c + 1d = 861

# Eliminate b from eq1 and eq2
eq1 = [Fraction(x) for x in eq1]
eq2 = [Fraction(x) for x in eq2]
eq3 = [Fraction(x) for x in eq3]
eq4 = [Fraction(x) for x in eq4]

# Scale equations to align b coefficients
eq1_scaled = [x * 2 for x in eq1]  # 10a + 8b + 6c + 4d = 2992
eq2_scaled = [x * 4 for x in eq2]  # 16a + 8b + 24c + 12d = 4700

# Subtract eq1_scaled from eq2_scaled to eliminate b
eq5 = [eq2_scaled[i] - eq1_scaled[i] for i in range(5)]  # 6a + 18c + 8d = 1708

# Eliminate b from eq3 and eq4
eq3_scaled = [x * 3 for x in eq3]  # 9a + 3b + 21c + 15d = 2874
eq4_scaled = [x * 1 for x in eq4]  # 2a + 3b + 5c + 1d = 861

# Subtract eq4_scaled from eq3_scaled to eliminate b
eq6 = [eq3_scaled[i] - eq4_scaled[i] for i in range(5)]  # 7a + 16c + 14d = 2013

# Now we have two equations (eq5 and eq6) with three variables (a, c, d):
# 1. 6a + 18c + 8d = 1708
# 2. 7a + 16c + 14d = 2013

# Eliminate one variable (e.g., a) from eq5 and eq6
eq5_scaled = [x * 7 for x in eq5]  # 42a + 126c + 56d = 11956
eq6_scaled = [x * 6 for x in eq6]  # 42a + 96c + 84d = 12078

# Subtract eq5_scaled from eq6_scaled to eliminate a
eq7 = [eq6_scaled[i] - eq5_scaled[i] for i in range(5)]  # -30c + 28d = 122

# Solve for c in terms of d
c = Fraction(-122, -30) + Fraction(28, 30)



"""

"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 23, Actual: 5
Missing variable in output: 'd'"""
