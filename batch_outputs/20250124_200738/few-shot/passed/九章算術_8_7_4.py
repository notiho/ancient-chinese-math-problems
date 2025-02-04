"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem can be translated into Python code as follows:

### Problem Setup:
We are given three equations based on the transactions:
1. \( 2牛 + 5羊 - 13豕 = 1000 \)
2. \( 3牛 - 9羊 + 3豕 = 0 \)
3. \( -5牛 + 6羊 + 8豕 = -600 \)

We need to solve for the prices of 牛 (a), 羊 (b), and 豕 (c).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Each row represents [牛系數, 羊系數, 豕系數, 常數項]
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Eliminate the first variable (牛) from the second and third equations
# Multiply rows to align coefficients of 牛, then subtract

# Scale row 1 to eliminate 牛 from row 2
factor = Fraction(matrix[1][0], matrix[0][0])
matrix[1] = [matrix[1][i] - factor * matrix[0][i] for i in range(4)]

# Scale row 1 to eliminate 牛 from row 3
factor = Fraction(matrix[2][0], matrix[0][0])
matrix[2] = [matrix[2][i] - factor * matrix[0][i] for i in range(4)]

# Step 2: Eliminate the second variable (羊) from the third equation
# Scale row 2 to align coefficients of 羊, then subtract

factor = Fraction(matrix[2][1], matrix[1][1])
matrix[2] = [matrix[2][i] - factor * matrix[1][i] for i in range(4)]

# Step 3: Back-substitution to solve for 豕 (c), 羊 (b), and 牛 (a)

# Solve for 豕 (c)
c = Fraction(matrix[2][3], matrix[2][2])

# Solve for 羊 (b)
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Solve for 牛 (a)
a = Fraction(matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b, matrix[0][0])

# Output the results
a = float(a)
b = float(b)
c = float(c)

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and each column corresponds to a variable or constant term.
2. **Elimination**: The first variable (牛) is eliminated from the second and third equations by scaling and subtracting rows. Then, the second variable (羊) is eliminated from the third equation.
3. **Back-Substitution**: After elimination, the system is in triangular form, and the variables are solved in reverse order (starting with 豕, then 羊, and finally 牛).
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

---

### Answer:
The values of \( a \), \( b \), and \( c \) represent the prices of 牛, 羊, and 豕, respectively. The output will display these values.
"""


"""
"""
