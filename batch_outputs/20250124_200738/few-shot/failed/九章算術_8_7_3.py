"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem, where we solve for the prices of cows, sheep, and pigs. The procedure described corresponds to the ancient Chinese method of solving simultaneous linear equations, which is essentially Gaussian elimination. Let's translate the problem and solution into Python code.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement:
# 2牛 + 5羊 - 13豕 = 1000 (余錢)
# 3牛 - 9羊 + 3豕 = 0 (錢適足)
# -5牛 + 6羊 + 8豕 = -600 (錢不足)

# Coefficients of the equations
equations = [
    [2, 5, -13, 1000],  # First equation
    [3, -9, 3, 0],      # Second equation
    [-5, 6, 8, -600]    # Third equation
]

# Perform Gaussian elimination
# Step 1: Normalize the first row
for i in range(4):
    equations[0][i] = Fraction(equations[0][i], equations[0][0])

# Step 2: Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = equations[i][0]
    for j in range(4):
        equations[i][j] -= factor * equations[0][j]

# Step 3: Normalize the second row
for i in range(1, 4):
    equations[1][i] = Fraction(equations[1][i], equations[1][1])

# Step 4: Eliminate the second variable from the third row
factor = equations[2][1]
for i in range(1, 4):
    equations[2][i] -= factor * equations[1][i]

# Step 5: Solve for the third variable
c = Fraction(equations[2][3], equations[2][2])

# Step 6: Back-substitute to solve for the second variable
b = equations[1][3] - equations[1][2] * c

# Step 7: Back-substitute to solve for the first variable
a = equations[0][3] - equations[0][2] * c - equations[0][1] * b

# Output the results
print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equations Setup**: The coefficients of the three equations are set up in a matrix form, where each row represents an equation.
2. **Gaussian Elimination**: The process of elimination is performed step by step:
   - Normalize the first row to make the coefficient of the first variable 1.
   - Use the first row to eliminate the first variable from the second and third rows.
   - Normalize the second row to make the coefficient of the second variable 1.
   - Use the second row to eliminate the second variable from the third row.
   - Solve for the third variable, then back-substitute to find the second and first variables.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.
4. **Output**: The prices of cows (`a`), sheep (`b`), and pigs (`c`) are printed as fractions.

This code follows the ancient Chinese method described in the problem, translated into a modern computational approach.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 23800/1359
Variable 'b' has wrong value. Expected: 500, Actual: 4600/453
Variable 'c' has wrong value. Expected: 300, Actual: -97400/1359"""
