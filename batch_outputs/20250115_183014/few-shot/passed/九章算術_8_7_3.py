"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem, as described in ancient Chinese mathematics. The problem involves solving for the prices of cows, sheep, and pigs based on the given transactions. Below is the Python implementation of the solution using the described method.


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2牛 + 5羊 - 13豕 = 1000
# 3牛 - 9羊 + 3豕 = 0
# -5牛 + 6羊 + 8豕 = -600

# Represent the coefficients of 牛, 羊, 豕, and the constants on the right-hand side
equations = [
    [2, 5, -13, 1000],  # First equation
    [3, -9, 3, 0],      # Second equation
    [-5, 6, 8, -600]    # Third equation
]

# Step 1: Normalize the first row (make the leading coefficient of the first row 1)
def normalize_row(row, leading_index):
    factor = row[leading_index]
    return [Fraction(x, factor) for x in row]

equations[0] = normalize_row(equations[0], 0)

# Step 2: Eliminate the first variable (牛) from the second and third rows
def eliminate_variable(equations, target_row, source_row, variable_index):
    factor = equations[target_row][variable_index]
    equations[target_row] = [
        equations[target_row][i] - factor * equations[source_row][i]
        for i in range(len(equations[target_row]))
    ]

eliminate_variable(equations, 1, 0, 0)  # Eliminate 牛 from the second row
eliminate_variable(equations, 2, 0, 0)  # Eliminate 牛 from the third row

# Step 3: Normalize the second row (make the leading coefficient of the second row 1)
equations[1] = normalize_row(equations[1], 1)

# Step 4: Eliminate the second variable (羊) from the first and third rows
eliminate_variable(equations, 0, 1, 1)  # Eliminate 羊 from the first row
eliminate_variable(equations, 2, 1, 1)  # Eliminate 羊 from the third row

# Step 5: Normalize the third row (make the leading coefficient of the third row 1)
equations[2] = normalize_row(equations[2], 2)

# Step 6: Eliminate the third variable (豕) from the first and second rows
eliminate_variable(equations, 0, 2, 2)  # Eliminate 豕 from the first row
eliminate_variable(equations, 1, 2, 2)  # Eliminate 豕 from the second row

# The final matrix is now in reduced row echelon form, and we can extract the solutions
牛價 = equations[0][3]
羊價 = equations[1][3]
豕價 = equations[2][3]

# Output the results
a = 牛價
b = 羊價
c = 豕價

# 牛價 a, 羊價 b, 豕價 c


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix, where each row corresponds to an equation, and each column corresponds to a variable or the constant on the right-hand side.
2. **Row Operations**: The algorithm follows the ancient Chinese method of elimination (similar to Gaussian elimination) to reduce the matrix to row echelon form.
3. **Normalization**: Each row is normalized by dividing by the leading coefficient to make it 1.
4. **Elimination**: Variables are eliminated from other rows by subtracting appropriate multiples of the normalized row.
5. **Solution Extraction**: Once the matrix is in reduced row echelon form, the solutions for 牛價 (price of cows), 羊價 (price of sheep), and 豕價 (price of pigs) can be directly read from the matrix.

### Final Answer:
The prices of 牛 (cows), 羊 (sheep), and 豕 (pigs) are given by `a`, `b`, and `c` respectively.
"""


"""
"""
