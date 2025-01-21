"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem is to determine the prices of cows, sheep, and pigs. Let's translate the problem and procedure into Python code step by step.

### Problem Setup:
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over.
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs to buy 5 cows, but 600 money is short.

We need to find the prices of cows (`牛`), sheep (`羊`), and pigs (`豕`).

### Procedure:
The ancient Chinese elimination method ("正負術") is described, which is equivalent to solving a system of linear equations using elimination. The equations are represented in matrix form, and the solution is derived step by step.

Here is the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
# Equation 2: 3牛 - 9羊 + 3豕 = 0
# Equation 3: -5牛 + 6羊 + 8豕 = -600

# Representing the system of equations as a matrix
# Each row is [牛, 羊, 豕, constant]
matrix = [
    [2, 5, -13, 1000],
    [3, -9, 3, 0],
    [-5, 6, 8, -600]
]

# Step 1: Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (牛) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (羊) from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Solve for the third variable (豕)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]
豕 = matrix[2][3]

# Step 6: Back-substitute to solve for the second variable (羊)
羊 = matrix[1][3] - matrix[1][2] * 豕

# Step 7: Back-substitute to solve for the first variable (牛)
牛 = matrix[0][3] - matrix[0][1] * 羊 - matrix[0][2] * 豕

# Final results
a = 牛
b = 羊
c = 豕

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and the columns represent the coefficients of the variables (`牛`, `羊`, `豕`) and the constant term.
2. **Normalization**: Each row is normalized by dividing through by the leading coefficient to simplify calculations.
3. **Elimination**: Variables are eliminated step by step using row operations, following the ancient Chinese elimination method.
4. **Back-Substitution**: Once the matrix is in row-echelon form, the variables are solved by back-substitution.
5. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Output:
The code will output the prices of cows (`牛`), sheep (`羊`), and pigs (`豕`) as fractions or integers, depending on the solution.
"""


"""
"""
