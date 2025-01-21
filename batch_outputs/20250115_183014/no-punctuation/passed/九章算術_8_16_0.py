"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics, solved using the "fangcheng" (方程) method, which is an early form of solving simultaneous equations. Below is the Python implementation of the problem using the described procedure.

### Problem Setup:
We are given the following equations:
1. \( 5 \text{羊} + 4 \text{犬} + 3 \text{雞} + 2 \text{兔} = 1496 \)
2. \( 4 \text{羊} + 2 \text{犬} + 6 \text{雞} + 3 \text{兔} = 1175 \)
3. \( 3 \text{羊} + 1 \text{犬} + 7 \text{雞} + 5 \text{兔} = 958 \)
4. \( 2 \text{羊} + 3 \text{犬} + 5 \text{雞} + 1 \text{兔} = 861 \)

We need to solve for the values of \( \text{羊} \), \( \text{犬} \), \( \text{雞} \), and \( \text{兔} \).

### Procedure:
The "fangcheng" method involves systematically eliminating variables by multiplying rows and subtracting them, similar to Gaussian elimination. Below is the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Each row represents [羊, 犬, 雞, 兔, constant]
equations = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Step 1: Eliminate the first variable (羊) from all but the first equation
for i in range(1, 4):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(5):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Eliminate the second variable (犬) from all but the second equation
for i in range(2, 4):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(5):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Eliminate the third variable (雞) from the fourth equation
factor = Fraction(equations[3][2], equations[2][2])
for j in range(5):
    equations[3][j] -= factor * equations[2][j]

# Step 4: Back-substitute to solve for each variable
# Solve for 兔 (rabbit)
兔 = Fraction(equations[3][4], equations[3][3])

# Solve for 雞 (chicken)
雞 = Fraction(equations[2][4] - equations[2][3] * 兔, equations[2][2])

# Solve for 犬 (dog)
犬 = Fraction(equations[1][4] - equations[1][3] * 兔 - equations[1][2] * 雞, equations[1][1])

# Solve for 羊 (sheep)
羊 = Fraction(equations[0][4] - equations[0][3] * 兔 - equations[0][2] * 雞 - equations[0][1] * 犬, equations[0][0])

# Final results
a = 羊
b = 犬
c = 雞
d = 兔

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Initialization**: The equations are represented as a list of lists, where each sublist contains the coefficients of the variables and the constant term.
2. **Elimination**: Using the "fangcheng" method, variables are systematically eliminated by multiplying rows and subtracting them, ensuring that each step adheres to the procedure described in the problem.
3. **Back-substitution**: Once the system is in triangular form, the variables are solved starting from the last equation and substituting the results back into the previous equations.
4. **Output**: The values of \( \text{羊} \), \( \text{犬} \), \( \text{雞} \), and \( \text{兔} \) are output as fractions for exactness.

### Answer:
The values of \( \text{羊} \), \( \text{犬} \), \( \text{雞} \), and \( \text{兔} \) are:
- \( \text{羊價} = a \)
- \( \text{犬價} = b \)
- \( \text{雞價} = c \)
- \( \text{兔價} = d \)
"""


"""
"""
