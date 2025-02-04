"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method described in the "方程術" (method of solving simultaneous equations). The problem provides the total cost of different combinations of animals (sheep, dogs, chickens, and rabbits), and we need to determine the price of each animal.

The equations can be written as follows:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + 1y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + 1w = 861 \)

Here, \(x\) is the price of a sheep, \(y\) is the price of a dog, \(z\) is the price of a chicken, and \(w\) is the price of a rabbit.

We will solve this system step by step using the described ancient method.


"""


from fractions import Fraction

# Coefficients of the equations
equations = [
    [5, 4, 3, 2, 1496],  # 5x + 4y + 3z + 2w = 1496
    [4, 2, 6, 3, 1175],  # 4x + 2y + 6z + 3w = 1175
    [3, 1, 7, 5, 958],   # 3x + 1y + 7z + 5w = 958
    [2, 3, 5, 1, 861]    # 2x + 3y + 5z + 1w = 861
]

# Step 1: Eliminate the first variable (x) from the second, third, and fourth equations
for i in range(1, 4):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(5):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Eliminate the second variable (y) from the third and fourth equations
for i in range(2, 4):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, 5):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Eliminate the third variable (z) from the fourth equation
factor = Fraction(equations[3][2], equations[2][2])
for j in range(2, 5):
    equations[3][j] -= factor * equations[2][j]

# Step 4: Back-substitution to solve for w, z, y, and x
w = Fraction(equations[3][4], equations[3][3])
z = Fraction(equations[2][4] - equations[2][3] * w, equations[2][2])
y = Fraction(equations[1][4] - equations[1][2] * z - equations[1][3] * w, equations[1][1])
x = Fraction(equations[0][4] - equations[0][1] * y - equations[0][2] * z - equations[0][3] * w, equations[0][0])

# Results
a = x  # Price of a sheep
b = y  # Price of a dog
c = z  # Price of a chicken
d = w  # Price of a rabbit

a, b, c, d


"""


### Explanation of the Code:
1. **Initialization**: The coefficients of the equations are stored in a list of lists, where each sublist represents an equation.
2. **Elimination**: The first variable (\(x\)) is eliminated from the second, third, and fourth equations by subtracting a multiple of the first equation. Similarly, the second variable (\(y\)) is eliminated from the third and fourth equations, and the third variable (\(z\)) is eliminated from the fourth equation.
3. **Back-Substitution**: Starting from the last equation, the values of \(w\), \(z\), \(y\), and \(x\) are calculated step by step.
4. **Results**: The prices of the animals are stored in variables \(a\), \(b\), \(c\), and \(d\).

### Answer:
The prices of the animals are:
- Sheep (\(a\)): \(x\)
- Dog (\(b\)): \(y\)
- Chicken (\(c\)): \(z\)
- Rabbit (\(d\)): \(w\)
"""


"""
"""
