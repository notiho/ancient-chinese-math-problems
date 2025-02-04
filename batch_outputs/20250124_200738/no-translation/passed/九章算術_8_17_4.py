"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
This problem is a system of linear equations, and the solution involves solving for the price per unit (斗) of 麻 (a), 麥 (b), 菽 (c), 答 (d), and 黍 (e). Below is the Python implementation based on the described procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍, and total price
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Step 1: Forward elimination
for i in range(len(equations)):
    # Normalize the current row
    factor = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], factor)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, len(equations)):
        factor = equations[k][i]
        for j in range(len(equations[k])):
            equations[k][j] -= factor * equations[i][j]

# Step 2: Back substitution
results = [0] * len(equations)
for i in range(len(equations) - 1, -1, -1):
    results[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        results[i] -= equations[i][j] * results[j]

# Assign results to variables
a, b, c, d, e = results

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: Each equation corresponds to the given data about 麻, 麥, 菽, 答, 黍, and their total price.
2. **Forward elimination**: The system of equations is reduced to an upper triangular form by normalizing each row and eliminating the variable from subsequent rows.
3. **Back substitution**: Starting from the last equation, solve for each variable by substituting the known values into the equations.
4. **Results**: The values of `a`, `b`, `c`, `d`, and `e` represent the price per 斗 of 麻, 麥, 菽, 答, and 黍, respectively.

### Final Answer:
- 麻一斗 = `a` 錢
- 麥一斗 = `b` 錢
- 菽一斗 = `c` 錢
- 答一斗 = `d` 錢
- 黍一斗 = `e` 錢
"""


"""
"""
