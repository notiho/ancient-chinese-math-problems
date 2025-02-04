"""
今有五家共井甲二綆不足如乙一綆乙三綆不足如丙一綆丙四綆不足如丁一綆丁五綆不足如戊一綆戊六綆不足如甲一綆如各得所不足一綆皆逮問井深綆長各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰井深 a丈 甲綆長 b丈 乙綆長 c丈 丙綆長 d丈 丁綆長 e丈 戊綆長 f尺 
"""

"""
This problem involves a system of equations, and the solution is derived using the ancient Chinese "fangcheng" (方程) method, which is an early form of solving linear equations. Below is the translation of the problem and its solution into Python code.

### Problem Translation:

"""
There are five families sharing a well. 
- Family A's rope is 2 *geng* short of reaching the water, as Family B's rope is 1 *geng* too long.
- Family B's rope is 3 *geng* short of reaching the water, as Family C's rope is 1 *geng* too long.
- Family C's rope is 4 *geng* short of reaching the water, as Family D's rope is 1 *geng* too long.
- Family D's rope is 5 *geng* short of reaching the water, as Family E's rope is 1 *geng* too long.
- Family E's rope is 6 *geng* short of reaching the water, as Family A's rope is 1 *geng* too long.

If each family receives exactly the length of rope they are short by (1 *geng*), how deep is the well, and how long is each family's rope?

The procedure says: Use the "fangcheng" method to solve the system of equations.
"""

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations based on the problem
# Let the unknowns be:
# x1 = depth of the well (井深)
# x2 = length of A's rope (甲綆長)
# x3 = length of B's rope (乙綆長)
# x4 = length of C's rope (丙綆長)
# x5 = length of D's rope (丁綆長)
# x6 = length of E's rope (戊綆長)

# Coefficients matrix (augmented for the constant terms)
# Each row corresponds to an equation derived from the problem
matrix = [
    [1, -1,  0,  0,  0,  0, 2],  # Equation for A
    [1,  0, -1,  0,  0,  0, 3],  # Equation for B
    [1,  0,  0, -1,  0,  0, 4],  # Equation for C
    [1,  0,  0,  0, -1,  0, 5],  # Equation for D
    [1,  0,  0,  0,  0, -1, 6],  # Equation for E
    [0,  1, -1,  1, -1,  1, 0]   # Rope lengths cycle back to A
]

# Solve the system of equations using Gaussian elimination
def gaussian_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        # Make the diagonal element 1
        diag = matrix[i][i]
        for j in range(len(matrix[i])):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        
        # Eliminate the current column for all other rows
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(len(matrix[k])):
                    matrix[k][j] -= factor * matrix[i][j]
    
    # Extract the solutions
    return [row[-1] for row in matrix]

# Solve the system
solutions = gaussian_elimination(matrix)

# Extract the results
a = solutions[0]  #井深
b = solutions[1]  #甲綆長
c = solutions[2]  #乙綆長
d = solutions[3]  #丙綆長
e = solutions[4]  #丁綆長
f = solutions[5]  #戊綆長

# Print the results
print(f"井深 a = {a} 丈")
print(f"甲綆長 b = {b} 丈")
print(f"乙綆長 c = {c} 丈")
print(f"丙綆長 d = {d} 丈")
print(f"丁綆長 e = {e} 丈")
print(f"戊綆長 f = {f} 丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations, where each equation corresponds to the relationships between the well depth and the rope lengths.
2. **Gaussian Elimination**: The system is solved using Gaussian elimination, which is implemented step-by-step in the `gaussian_elimination` function.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves precise proportional relationships.
4. **Results**: The solution gives the depth of the well and the length of each family's rope in terms of *zhang* (丈).

### Final Answer:
The depth of the well and the lengths of the ropes are calculated and printed as fractions or integers, depending on the result.
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 4
Variable 'b' has wrong value. Expected: 53/20, Actual: 2
Variable 'c' has wrong value. Expected: 191/100, Actual: 1
Variable 'd' has wrong value. Expected: 37/25, Actual: 0
Variable 'e' has wrong value. Expected: 129/100, Actual: -1
Variable 'f' has wrong value. Expected: 38/5, Actual: -2"""
