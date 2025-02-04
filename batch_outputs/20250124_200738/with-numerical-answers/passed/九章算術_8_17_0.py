"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a(=7)錢 ，麥一斗 b(=4)錢 ，菽一斗 c(=3)錢 ，答一斗 d(=5)錢 ，黍一斗 e(=6)錢 。
"""

"""
To solve this problem, we need to use the method of solving simultaneous linear equations, as described in the ancient Chinese "fangcheng" (方程) method. Each type of grain (麻, 麥, 菽, 答, 黍) corresponds to a variable, and the given equations represent the total cost of combinations of these grains. Let's translate the procedure into Python code.


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95],   # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Step 1: Eliminate 麻 (first variable) from all but the first equation
for i in range(1, len(equations)):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(len(equations[0])):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Eliminate 麥 (second variable) from all but the first two equations
for i in range(2, len(equations)):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, len(equations[0])):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Eliminate 菽 (third variable) from all but the first three equations
for i in range(3, len(equations)):
    factor = Fraction(equations[i][2], equations[2][2])
    for j in range(2, len(equations[0])):
        equations[i][j] -= factor * equations[2][j]

# Step 4: Eliminate 答 (fourth variable) from all but the first four equations
factor = Fraction(equations[4][3], equations[3][3])
for j in range(3, len(equations[0])):
    equations[4][j] -= factor * equations[3][j]

# Step 5: Back substitution to solve for each variable
e = Fraction(equations[4][5], equations[4][4])  # 黍
d = Fraction(equations[3][5] - equations[3][4] * e, equations[3][3])  # 答
c = Fraction(equations[2][5] - equations[2][4] * e - equations[2][3] * d, equations[2][2])  # 菽
b = Fraction(equations[1][5] - equations[1][4] * e - equations[1][3] * d - equations[1][2] * c, equations[1][1])  # 麥
a = Fraction(equations[0][5] - equations[0][4] * e - equations[0][3] * d - equations[0][2] * c - equations[0][1] * b, equations[0][0])  # 麻

# Results
a, b, c, d, e  # 麻=7錢, 麥=4錢, 菽=3錢, 答=5錢, 黍=6錢
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: Each equation represents the cost of a combination of grains.
2. **Elimination process**: Using the "fangcheng" method, eliminate variables step by step by subtracting multiples of one equation from another.
3. **Back substitution**: Solve for each variable starting from the last equation.
4. **Result**: The values of `a`, `b`, `c`, `d`, and `e` represent the cost of one dou of 麻, 麥, 菽, 答, and 黍, respectively.

### Final Answer:
- 麻 (a) = 7 錢
- 麥 (b) = 4 錢
- 菽 (c) = 3 錢
- 答 (d) = 5 錢
- 黍 (e) = 6 錢
"""


"""
"""
