"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
This is a system of linear equations problem, where the goal is to determine the price per dou (斗) of 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), and 黍 (shu). The problem is solved using the ancient Chinese method of elimination, which is similar to Gaussian elimination.

### Problem Setup:
We are given the following system of equations:

1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

Where \( a, b, c, d, e \) are the prices per dou of 麻, 麥, 菽, 答, and 黍, respectively.

We will solve this system step by step using the ancient elimination method.

---


"""


from fractions import Fraction

# Coefficients of the equations
equations = [
    [9, 7, 3, 2, 5, 140],  # 9a + 7b + 3c + 2d + 5e = 140
    [7, 6, 4, 5, 3, 128],  # 7a + 6b + 4c + 5d + 3e = 128
    [3, 5, 7, 6, 4, 116],  # 3a + 5b + 7c + 6d + 4e = 116
    [2, 5, 3, 9, 4, 112],  # 2a + 5b + 3c + 9d + 4e = 112
    [1, 3, 2, 8, 5, 95]    # 1a + 3b + 2c + 8d + 5e = 95
]

# Step 1: Eliminate the first variable (a)
for i in range(1, 5):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(6):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Eliminate the second variable (b)
for i in range(2, 5):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(6):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Eliminate the third variable (c)
for i in range(3, 5):
    factor = Fraction(equations[i][2], equations[2][2])
    for j in range(6):
        equations[i][j] -= factor * equations[2][j]

# Step 4: Eliminate the fourth variable (d)
factor = Fraction(equations[4][3], equations[3][3])
for j in range(6):
    equations[4][j] -= factor * equations[3][j]

# Step 5: Back substitution to solve for e, d, c, b, a
e = Fraction(equations[4][5], equations[4][4])
d = Fraction(equations[3][5] - equations[3][4] * e, equations[3][3])
c = Fraction(equations[2][5] - equations[2][4] * d - equations[2][3] * e, equations[2][2])
b = Fraction(equations[1][5] - equations[1][4] * d - equations[1][3] * e - equations[1][2] * c, equations[1][1])
a = Fraction(equations[0][5] - equations[0][4] * d - equations[0][3] * e - equations[0][2] * c - equations[0][1] * b, equations[0][0])

# Output the results
a, b, c, d, e


"""


### Explanation:
1. **Step 1**: Eliminate the first variable \( a \) from all equations except the first by subtracting a multiple of the first equation from the others.
2. **Step 2**: Eliminate the second variable \( b \) from all equations except the first two.
3. **Step 3**: Eliminate the third variable \( c \) from all equations except the first three.
4. **Step 4**: Eliminate the fourth variable \( d \) from the last equation.
5. **Step 5**: Use back substitution to solve for \( e, d, c, b, a \).

### Final Answer:
The prices per dou are:
- 麻 (a): \( a \) qian
- 麥 (b): \( b \) qian
- 菽 (c): \( c \) qian
- 答 (d): \( d \) qian
- 黍 (e): \( e \) qian
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: -22/5
Variable 'b' has wrong value. Expected: 4, Actual: 229/10
Variable 'c' has wrong value. Expected: 3, Actual: -59/10"""
