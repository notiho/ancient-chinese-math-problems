"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This problem involves solving a system of linear equations using an ancient Chinese method described in the "Nine Chapters on the Mathematical Art" (九章算術), specifically the method of elimination for solving simultaneous equations. Below is the Python implementation of the described procedure.


"""


from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
coefficients = [
    [5, 4, 3, 2, 1496],  # First equation
    [4, 2, 6, 3, 1175],  # Second equation
    [3, 1, 7, 5, 958],   # Third equation
    [2, 3, 5, 1, 861]    # Fourth equation
]

# Step 1: Eliminate the first variable (羊)
for i in range(1, 4):
    factor = Fraction(coefficients[i][0], coefficients[0][0])
    for j in range(5):
        coefficients[i][j] -= factor * coefficients[0][j]

# Step 2: Eliminate the second variable (犬)
for i in range(2, 4):
    factor = Fraction(coefficients[i][1], coefficients[1][1])
    for j in range(5):
        coefficients[i][j] -= factor * coefficients[1][j]

# Step 3: Eliminate the third variable (雞)
factor = Fraction(coefficients[3][2], coefficients[2][2])
for j in range(5):
    coefficients[3][j] -= factor * coefficients[2][j]

# Step 4: Back substitution to solve for the variables
d = Fraction(coefficients[3][4], coefficients[3][3])  # Solve for 兔 (rabbit)
c = Fraction(coefficients[2][4] - coefficients[2][3] * d, coefficients[2][2])  # Solve for 雞 (chicken)
b = Fraction(coefficients[1][4] - coefficients[1][2] * c - coefficients[1][3] * d, coefficients[1][1])  # Solve for 犬 (dog)
a = Fraction(coefficients[0][4] - coefficients[0][1] * b - coefficients[0][2] * c - coefficients[0][3] * d, coefficients[0][0])  # Solve for 羊 (sheep)

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Input the coefficients**: The coefficients of the variables (羊, 犬, 雞, 兔) and the constants on the right-hand side of the equations are stored in a list of lists.
2. **Elimination process**:
   - The first variable (羊) is eliminated from the second, third, and fourth equations by subtracting a multiple of the first equation.
   - The second variable (犬) is eliminated from the third and fourth equations by subtracting a multiple of the second equation.
   - The third variable (雞) is eliminated from the fourth equation by subtracting a multiple of the third equation.
3. **Back substitution**:
   - Starting from the last equation, solve for one variable at a time, substituting the known values into the previous equations.
4. **Output the results**: The values of 羊 (a), 犬 (b), 雞 (c), and 兔 (d) are displayed as fractions.

### Answer:
The values of the variables are:
- 羊價 (price of a sheep): `a`
- 犬價 (price of a dog): `b`
- 雞價 (price of a chicken): `c`
- 兔價 (price of a rabbit): `d`
"""


"""
"""
