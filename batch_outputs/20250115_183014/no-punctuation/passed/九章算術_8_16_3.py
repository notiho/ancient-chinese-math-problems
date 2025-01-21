"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This is a classic simultaneous equations problem, solved using the ancient Chinese method of elimination, known as the "fangcheng" method. The problem involves determining the prices of sheep, dogs, chickens, and rabbits based on the given equations.

The equations are as follows:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + w = 861 \)

Where:
- \( x \) is the price of a sheep,
- \( y \) is the price of a dog,
- \( z \) is the price of a chicken,
- \( w \) is the price of a rabbit.

We will solve this step by step using the "fangcheng" elimination method.


"""


from fractions import Fraction

# Coefficients and constants from the equations
equations = [
    [5, 4, 3, 2, 1496],  # 5x + 4y + 3z + 2w = 1496
    [4, 2, 6, 3, 1175],  # 4x + 2y + 6z + 3w = 1175
    [3, 1, 7, 5, 958],   # 3x + y + 7z + 5w = 958
    [2, 3, 5, 1, 861]    # 2x + 3y + 5z + w = 861
]

# Step 1: Eliminate the first variable (x) from all but the first equation
for i in range(1, 4):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(5):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Eliminate the second variable (y) from all but the second equation
for i in range(2, 4):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, 5):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Eliminate the third variable (z) from the fourth equation
factor = Fraction(equations[3][2], equations[2][2])
for j in range(2, 5):
    equations[3][j] -= factor * equations[2][j]

# Step 4: Back-substitute to solve for the variables
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
1. **Initialization**: The equations are represented as a list of lists, where each sublist contains the coefficients of the variables and the constant term.
2. **Elimination**: The "fangcheng" method eliminates variables step by step by subtracting multiples of one equation from another.
3. **Back-substitution**: After reducing the system to a triangular form, the variables are solved starting from the last equation.
4. **Results**: The prices of the sheep, dog, chicken, and rabbit are stored in `a`, `b`, `c`, and `d`, respectively.

### Final Answer:
The prices of the animals are:
- Sheep: \( a \) chi
- Dog: \( b \) chi
- Chicken: \( c \) chi
- Rabbit: \( d \) chi
"""


"""
"""
