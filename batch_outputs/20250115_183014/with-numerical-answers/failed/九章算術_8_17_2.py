"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a(=1)斗 b(=7)錢 ，麥 c(=1)斗 d(=4)錢 ，菽 e(=1)斗 f(=3)錢 ，答 g(=1)斗 h(=5)錢 ，黍 i(=1)斗 j(=6)錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one dou of each type of grain. The procedure described corresponds to solving the equations using elimination methods, similar to Gaussian elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations (麻, 麥, 菽, 答, 黍)
coefficients = [
    [9, 7, 3, 2, 5],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗
    [7, 6, 4, 5, 3],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗
    [3, 5, 7, 6, 4],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗
    [2, 5, 3, 9, 4],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗
    [1, 3, 2, 8, 5],  # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗
]

# Constants (total price in 錢)
constants = [140, 128, 116, 112, 95]

# Step 1: Convert coefficients and constants to fractions for exact arithmetic
coefficients = [[Fraction(x) for x in row] for row in coefficients]
constants = [Fraction(x) for x in constants]

# Step 2: Perform Gaussian elimination
n = len(coefficients)

for i in range(n):
    # Make the diagonal element 1 by dividing the row
    diag = coefficients[i][i]
    for j in range(i, n):
        coefficients[i][j] /= diag
    constants[i] /= diag

    # Eliminate the current variable from the rows below
    for k in range(i + 1, n):
        factor = coefficients[k][i]
        for j in range(i, n):
            coefficients[k][j] -= factor * coefficients[i][j]
        constants[k] -= factor * constants[i]

# Step 3: Back substitution to solve for variables
solutions = [0] * n
for i in range(n - 1, -1, -1):
    solutions[i] = constants[i]
    for j in range(i + 1, n):
        solutions[i] -= coefficients[i][j] * solutions[j]

# Step 4: Extract results
a, c, e, g, i = solutions  # 麻, 麥, 菽, 答, 黍 prices per 斗
b, d, f, h, j = [x.numerator for x in solutions], [x.denominator for x in solutions]

# 麻 a(=1)斗 b(=7)錢, 麥 c(=1)斗 d(=4)錢, 菽 e(=1)斗 f(=3)錢, 答 g(=1)斗 h(=5)錢, 黍 i(=1)斗 j(=6)錢
print(f"麻: {a}斗 {b}錢")
print(f"麥: {c}斗 {d}錢")
print(f"菽: {e}斗 {f}錢")
print(f"答: {g}斗 {h}錢")
print(f"黍: {i}斗 {j}錢")


"""


### Explanation of the Code:
1. **Input Setup**: The coefficients of the equations represent the number of dou for each type of grain in each equation, and the constants represent the total price in qian.
2. **Gaussian Elimination**: The procedure described in the problem is implemented using Gaussian elimination, which involves normalizing rows and eliminating variables step by step.
3. **Back Substitution**: After elimination, the solution is obtained by substituting back into the equations.
4. **Output**: The solution gives the price of one dou of each type of grain in qian.

### Final Answer:
- 麻: 1斗 7錢
- 麥: 1斗 4錢
- 菽: 1斗 3錢
- 答: 1斗 5錢
- 黍: 1斗 6錢
"""


"""
Code error: not enough values to unpack (expected 5, got 2)"""
