"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese "fangcheng" (方程) method is essentially a precursor to modern linear algebra. Below is the Python implementation of the procedure described:


"""


from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
coefficients = [
    [5, 4, 3, 2],  # First equation
    [4, 2, 6, 3],  # Second equation
    [3, 1, 7, 5],  # Third equation
    [2, 3, 5, 1]   # Fourth equation
]

# Constants on the right-hand side
constants = [1496, 1175, 958, 861]

# Step 1: Normalize the first row
for i in range(4):
    coefficients[0][i] = Fraction(coefficients[0][i], coefficients[0][0])
constants[0] = Fraction(constants[0], coefficients[0][0])

# Step 2: Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    for j in range(4):
        coefficients[i][j] -= factor * coefficients[0][j]
    constants[i] -= factor * constants[0]

# Step 3: Normalize the second row
for i in range(1, 4):
    coefficients[1][i] = Fraction(coefficients[1][i], coefficients[1][1])
constants[1] = Fraction(constants[1], coefficients[1][1])

# Step 4: Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    for j in range(1, 4):
        coefficients[i][j] -= factor * coefficients[1][j]
    constants[i] -= factor * constants[1]

# Step 5: Normalize the third row
for i in range(2, 4):
    coefficients[2][i] = Fraction(coefficients[2][i], coefficients[2][2])
constants[2] = Fraction(constants[2], coefficients[2][2])

# Step 6: Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    for j in range(2, 4):
        coefficients[i][j] -= factor * coefficients[2][j]
    constants[i] -= factor * constants[2]

# Step 7: Solve for the fourth variable
constants[3] = Fraction(constants[3], coefficients[3][3])

# Step 8: Back-substitute to solve for the other variables
constants[2] -= coefficients[2][3] * constants[3]
constants[1] -= coefficients[1][2] * constants[2] + coefficients[1][3] * constants[3]
constants[0] -= coefficients[0][1] * constants[1] + coefficients[0][2] * constants[2] + coefficients[0][3] * constants[3]

# The solutions are:
a = constants[0]  # Price of a sheep
b = constants[1]  # Price of a dog
c = constants[2]  # Price of a chicken
d = constants[3]  # Price of a rabbit

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Normalization**: Each row is normalized by dividing through by the leading coefficient of the variable being eliminated.
2. **Elimination**: Variables are eliminated from other rows by subtracting a multiple of the normalized row.
3. **Back-substitution**: Once the system is in triangular form, the variables are solved in reverse order.

### Final Answer:
The prices of the animals are:
- Sheep price: `a`
- Dog price: `b`
- Chicken price: `c`
- Rabbit price: `d`
"""


"""
Variable 'a' has wrong value. Expected: 177, Actual: 32945/98
Variable 'b' has wrong value. Expected: 121, Actual: -32293/196
Variable 'c' has wrong value. Expected: 23, Actual: -453/7
Variable 'd' has wrong value. Expected: 29, Actual: 197275/196"""
