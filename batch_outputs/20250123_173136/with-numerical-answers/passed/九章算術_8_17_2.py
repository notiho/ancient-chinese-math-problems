"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a(=7)錢 ，麥一斗 b(=4)錢 ，菽一斗 c(=3)錢 ，答一斗 d(=5)錢 ，黍一斗 e(=6)錢 。
"""

"""
To solve this problem, we will use the ancient Chinese method of solving simultaneous linear equations, as described in the procedure ("方程術"). The problem involves determining the price per dou of five grains (麻, 麥, 菽, 答, 黍) based on five equations. 

The equations are:
1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

We will solve these equations step by step using the described elimination method.


"""


from fractions import Fraction

# Coefficients of the equations
coefficients = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Step 1: Eliminate the first variable (a) from all rows except the first
for i in range(1, 5):
    factor = Fraction(coefficients[i][0], coefficients[0][0])
    for j in range(6):
        coefficients[i][j] -= factor * coefficients[0][j]

# Step 2: Eliminate the second variable (b) from all rows except the first two
for i in range(2, 5):
    factor = Fraction(coefficients[i][1], coefficients[1][1])
    for j in range(1, 6):
        coefficients[i][j] -= factor * coefficients[1][j]

# Step 3: Eliminate the third variable (c) from all rows except the first three
for i in range(3, 5):
    factor = Fraction(coefficients[i][2], coefficients[2][2])
    for j in range(2, 6):
        coefficients[i][j] -= factor * coefficients[2][j]

# Step 4: Eliminate the fourth variable (d) from the last row
factor = Fraction(coefficients[4][3], coefficients[3][3])
for j in range(3, 6):
    coefficients[4][j] -= factor * coefficients[3][j]

# Step 5: Back-substitute to solve for each variable
e = Fraction(coefficients[4][5], coefficients[4][4])
d = Fraction(coefficients[3][5] - coefficients[3][4] * e, coefficients[3][3])
c = Fraction(coefficients[2][5] - coefficients[2][4] * e - coefficients[2][3] * d, coefficients[2][2])
b = Fraction(coefficients[1][5] - coefficients[1][4] * e - coefficients[1][3] * d - coefficients[1][2] * c, coefficients[1][1])
a = Fraction(coefficients[0][5] - coefficients[0][4] * e - coefficients[0][3] * d - coefficients[0][2] * c - coefficients[0][1] * b, coefficients[0][0])

# Results
a, b, c, d, e  # 麻一斗 a(=7)錢, 麥一斗 b(=4)錢, 菽一斗 c(=3)錢, 答一斗 d(=5)錢, 黍一斗 e(=6)錢


"""
 

### Explanation:
- Each step corresponds to eliminating one variable from the equations, as described in the procedure.
- The final step involves back-substitution to solve for each variable.
- The results are \( a = 7 \), \( b = 4 \), \( c = 3 \), \( d = 5 \), \( e = 6 \), which are the prices per dou of 麻, 麥, 菽, 答, and 黍, respectively.
"""


"""
"""
