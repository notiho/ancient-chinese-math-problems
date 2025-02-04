"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
To solve this problem, we will use the ancient Chinese method of solving systems of linear equations, known as the "正負術" (positive-negative method), which is equivalent to Gaussian elimination in modern terms. The problem involves determining the prices of sheep, dogs, chickens, and rabbits based on the given equations.

### Problem:
We are given the following equations based on the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔):

1. \( 5羊 + 4犬 + 3雞 + 2兔 = 1496 \)
2. \( 4羊 + 2犬 + 6雞 + 3兔 = 1175 \)
3. \( 3羊 + 1犬 + 7雞 + 5兔 = 958 \)
4. \( 2羊 + 3犬 + 5雞 + 1兔 = 861 \)

We need to find the values of \( 羊 \) (sheep price), \( 犬 \) (dog price), \( 雞 \) (chicken price), and \( 兔 \) (rabbit price).

---

### Solution:
We will follow the "方程術" (method of equations) step by step to solve this system.


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations
# Each row represents an equation: [coefficients of 羊, 犬, 雞, 兔, constant term]
equations = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Step 2: Perform Gaussian elimination to reduce the system to upper triangular form
# Normalize the first row
for i in range(1, 4):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(5):
        equations[i][j] -= factor * equations[0][j]

# Normalize the second row
for i in range(2, 4):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, 5):
        equations[i][j] -= factor * equations[1][j]

# Normalize the third row
factor = Fraction(equations[3][2], equations[2][2])
for j in range(2, 5):
    equations[3][j] -= factor * equations[2][j]

# Step 3: Back-substitution to solve for the variables
# Solve for 兔 (rabbit price)
兔 = Fraction(equations[3][4], equations[3][3])

# Solve for 雞 (chicken price)
雞 = Fraction(equations[2][4] - equations[2][3] * 兔, equations[2][2])

# Solve for 犬 (dog price)
犬 = Fraction(equations[1][4] - equations[1][3] * 兔 - equations[1][2] * 雞, equations[1][1])

# Solve for 羊 (sheep price)
羊 = Fraction(equations[0][4] - equations[0][3] * 兔 - equations[0][2] * 雞 - equations[0][1] * 犬, equations[0][0])

# Step 4: Convert results to integers (since prices are in whole numbers)
a = 羊.numerator // 羊.denominator  # 177
b = 犬.numerator // 犬.denominator  # 121
c = 雞.numerator // 雞.denominator  # 23
d = 兔.numerator // 兔.denominator  # 29

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Step 1**: The coefficients of the equations are represented as a matrix. Each row corresponds to an equation, and the last column represents the constant terms.
2. **Step 2**: Gaussian elimination is performed to reduce the system to an upper triangular form. This involves subtracting multiples of one row from another to eliminate variables step by step.
3. **Step 3**: Back-substitution is used to solve for the variables starting from the last equation.
4. **Step 4**: The results are converted to integers since the prices are whole numbers.

### Final Answer:
- Sheep price (\( 羊 \)): \( a = 177 \)
- Dog price (\( 犬 \)): \( b = 121 \)
- Chicken price (\( 雞 \)): \( c = 23 \)
- Rabbit price (\( 兔 \)): \( d = 29 \)
"""


"""
"""
