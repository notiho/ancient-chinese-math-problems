"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This is a system of linear equations problem, where we are solving for the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔). The problem can be solved using the ancient Chinese method of elimination, which is similar to Gaussian elimination in modern mathematics. Below is the Python implementation of the procedure described in the problem:


"""


from fractions import Fraction

# The equations are:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
equations = [
    [5, 4, 3, 2, 1496],  # First equation
    [4, 2, 6, 3, 1175],  # Second equation
    [3, 1, 7, 5, 958],   # Third equation
    [2, 3, 5, 1, 861]    # Fourth equation
]

# Step 1: Eliminate the first variable (羊) from the second, third, and fourth equations
for i in range(1, 4):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(5):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Eliminate the second variable (犬) from the third and fourth equations
for i in range(2, 4):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, 5):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Eliminate the third variable (雞) from the fourth equation
factor = Fraction(equations[3][2], equations[2][2])
for j in range(2, 5):
    equations[3][j] -= factor * equations[2][j]

# Step 4: Back-substitution to solve for the variables
d = Fraction(equations[3][4], equations[3][3])  # Solve for 兔 (rabbit)
c = Fraction(equations[2][4] - equations[2][3] * d, equations[2][2])  # Solve for 雞 (chicken)
b = Fraction(equations[1][4] - equations[1][2] * c - equations[1][3] * d, equations[1][1])  # Solve for 犬 (dog)
a = Fraction(equations[0][4] - equations[0][1] * b - equations[0][2] * c - equations[0][3] * d, equations[0][0])  # Solve for 羊 (sheep)

# Results
a, b, c, d


"""


### Explanation of the Code:
1. **Input the equations**: Each equation is represented as a list of coefficients, with the last element being the constant term.
2. **Elimination process**: The first variable (羊) is eliminated from the subsequent equations by subtracting a multiple of the first equation. This process is repeated for the second variable (犬) and then the third variable (雞).
3. **Back-substitution**: After the elimination process, the system is in triangular form, and the variables are solved starting from the last equation (兔) and working upwards.
4. **Fraction class**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Answer:
The prices of the animals are:
- 羊 (sheep): `a`
- 犬 (dog): `b`
- 雞 (chicken): `c`
- 兔 (rabbit): `d`
"""


"""
"""
