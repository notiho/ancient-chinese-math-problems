"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This problem involves solving a system of linear equations to determine the prices of cows, sheep, and pigs. The ancient Chinese method described here is essentially a form of Gaussian elimination, which is used to solve systems of linear equations. Below is the Python implementation of the problem using the described procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# 1. 2牛 + 5羊 - 13豕 = 1000
# 2. 3牛 - 9羊 + 3豕 = 0
# 3. 5牛 - 6羊 - 8豕 = -600

# Coefficients of the equations
equations = [
    [2, 5, -13, 1000],  # First equation
    [3, -9, 3, 0],      # Second equation
    [5, -6, -8, -600]   # Third equation
]

# Step 1: Normalize the first equation (make the first coefficient 1)
factor = equations[0][0]
equations[0] = [Fraction(x, factor) for x in equations[0]]

# Step 2: Eliminate the first variable from the second and third equations
for i in range(1, 3):
    factor = equations[i][0]
    equations[i] = [equations[i][j] - factor * equations[0][j] for j in range(4)]

# Step 3: Normalize the second equation (make the second coefficient 1)
factor = equations[1][1]
equations[1] = [Fraction(x, factor) for x in equations[1]]

# Step 4: Eliminate the second variable from the third equation
factor = equations[2][1]
equations[2] = [equations[2][j] - factor * equations[1][j] for j in range(4)]

# Step 5: Solve for the third variable (豕價)
c = Fraction(equations[2][3], equations[2][2])

# Step 6: Back-substitute to solve for the second variable (羊價)
b = Fraction(equations[1][3] - equations[1][2] * c, equations[1][1])

# Step 7: Back-substitute to solve for the first variable (牛價)
a = Fraction(equations[0][3] - equations[0][2] * c - equations[0][1] * b, equations[0][0])

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equations Setup**: The problem is represented as a system of three linear equations with three variables (牛價, 羊價, 豕價).
2. **Gaussian Elimination**: The procedure described in the problem is implemented step-by-step:
   - Normalize the first equation.
   - Eliminate the first variable from the second and third equations.
   - Normalize the second equation.
   - Eliminate the second variable from the third equation.
   - Solve for the third variable and back-substitute to find the other variables.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient Chinese method.

### Answer:
The values of `a`, `b`, and `c` represent the prices of cows, sheep, and pigs, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 6300
Variable 'b' has wrong value. Expected: 500, Actual: 2750
Variable 'c' has wrong value. Expected: 300, Actual: 1950"""
