"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
To solve this problem, we need to use the method of solving simultaneous linear equations, as described in the ancient Chinese "方程術" (method of solving systems of equations). Each commodity's price per dou (unit) is unknown, and we are given five equations to solve for these unknowns.

The equations are derived from the problem statement:

1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

Here is the Python implementation of the solution using the described procedure:


"""


from fractions import Fraction

# Coefficients of the equations
coefficients = [
    [9, 7, 3, 2, 5],
    [7, 6, 4, 5, 3],
    [3, 5, 7, 6, 4],
    [2, 5, 3, 9, 4],
    [1, 3, 2, 8, 5]
]

# Constants (right-hand side of the equations)
constants = [140, 128, 116, 112, 95]

# Step 1: Normalize the first equation
for i in range(5):
    coefficients[0][i] = Fraction(coefficients[0][i], coefficients[0][0])
constants[0] = Fraction(constants[0], coefficients[0][0])

# Step 2: Eliminate the first variable from the other equations
for i in range(1, 5):
    factor = coefficients[i][0]
    for j in range(5):
        coefficients[i][j] -= factor * coefficients[0][j]
    constants[i] -= factor * constants[0]

# Step 3: Normalize the second equation
for i in range(1, 5):
    coefficients[1][i] = Fraction(coefficients[1][i], coefficients[1][1])
constants[1] = Fraction(constants[1], coefficients[1][1])

# Step 4: Eliminate the second variable from the other equations
for i in range(2, 5):
    factor = coefficients[i][1]
    for j in range(1, 5):
        coefficients[i][j] -= factor * coefficients[1][j]
    constants[i] -= factor * constants[1]

# Step 5: Normalize the third equation
for i in range(2, 5):
    coefficients[2][i] = Fraction(coefficients[2][i], coefficients[2][2])
constants[2] = Fraction(constants[2], coefficients[2][2])

# Step 6: Eliminate the third variable from the other equations
for i in range(3, 5):
    factor = coefficients[i][2]
    for j in range(2, 5):
        coefficients[i][j] -= factor * coefficients[2][j]
    constants[i] -= factor * constants[2]

# Step 7: Normalize the fourth equation
for i in range(3, 5):
    coefficients[3][i] = Fraction(coefficients[3][i], coefficients[3][3])
constants[3] = Fraction(constants[3], coefficients[3][3])

# Step 8: Eliminate the fourth variable from the last equation
factor = coefficients[4][3]
for j in range(3, 5):
    coefficients[4][j] -= factor * coefficients[3][j]
constants[4] -= factor * constants[3]

# Step 9: Solve for the fifth variable
constants[4] = Fraction(constants[4], coefficients[4][4])

# Step 10: Back-substitute to find the other variables
constants[3] -= coefficients[3][4] * constants[4]
constants[2] -= coefficients[2][3] * constants[3] + coefficients[2][4] * constants[4]
constants[1] -= coefficients[1][2] * constants[2] + coefficients[1][3] * constants[3] + coefficients[1][4] * constants[4]
constants[0] -= coefficients[0][1] * constants[1] + coefficients[0][2] * constants[2] + coefficients[0][3] * constants[3] + coefficients[0][4] * constants[4]

# Assign the results to variables
a, b, c, d, e = constants

# Output the results
a, b, c, d, e


"""


### Explanation of the Code:
1. **Normalization**: Each equation is normalized by dividing all terms by the coefficient of the leading variable.
2. **Elimination**: The leading variable is eliminated from subsequent equations by subtracting a multiple of the normalized equation.
3. **Back-substitution**: After reducing the system to a triangular form, the variables are solved starting from the last equation and substituting back into the previous ones.

### Final Answer:
The values of \(a\), \(b\), \(c\), \(d\), and \(e\) represent the price per dou of 麻 (a), 麥 (b), 菽 (c), 答 (d), and 黍 (e), respectively.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: -59407589605/816072227
Variable 'b' has wrong value. Expected: 4, Actual: 9061269737/816072227
Variable 'c' has wrong value. Expected: 3, Actual: 498507991/816072227
Variable 'd' has wrong value. Expected: 5, Actual: 3389454/816072227
Variable 'e' has wrong value. Expected: 6, Actual: 21745302069/816072227"""
