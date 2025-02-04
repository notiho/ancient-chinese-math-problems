"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a(=7)錢 ，麥一斗 b(=4)錢 ，菽一斗 c(=3)錢 ，答一斗 d(=5)錢 ，黍一斗 e(=6)錢 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The goal is to determine the price per dou (斗) of each type of grain: 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), and 黍 (shu).

### Problem Setup:
We are given the following equations based on the quantities of grains and their total prices:

1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

We solve for \( a \), \( b \), \( c \), \( d \), and \( e \), which represent the price per dou of 麻, 麥, 菽, 答, and 黍, respectively.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
coefficients = [
    [9, 7, 3, 2, 5],
    [7, 6, 4, 5, 3],
    [3, 5, 7, 6, 4],
    [2, 5, 3, 9, 4],
    [1, 3, 2, 8, 5]
]

# Constants (total prices)
constants = [140, 128, 116, 112, 95]

# Step 1: Forward elimination
for i in range(len(coefficients)):
    # Normalize the current row
    divisor = coefficients[i][i]
    for j in range(i, len(coefficients[i])):
        coefficients[i][j] = Fraction(coefficients[i][j], divisor)
    constants[i] = Fraction(constants[i], divisor)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, len(coefficients)):
        multiplier = coefficients[k][i]
        for j in range(i, len(coefficients[k])):
            coefficients[k][j] -= multiplier * coefficients[i][j]
        constants[k] -= multiplier * constants[i]

# Step 2: Back substitution
solutions = [0] * len(constants)
for i in range(len(coefficients) - 1, -1, -1):
    solutions[i] = constants[i]
    for j in range(i + 1, len(coefficients[i])):
        solutions[i] -= coefficients[i][j] * solutions[j]

# Extract solutions
a, b, c, d, e = solutions

# Output results
a, b, c, d, e  # a = 7, b = 4, c = 3, d = 5, e = 6
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Forward Elimination**:
   - Normalize each row by dividing all elements in the row (including the constant) by the pivot element (diagonal element).
   - Subtract multiples of the current row from subsequent rows to eliminate the current variable from those rows.

2. **Back Substitution**:
   - Start from the last row and solve for the variable in that row.
   - Substitute the solved variable into the rows above to solve for the remaining variables.

---

### Final Answer:
- 麻 (ma): \( a = 7 \) 錢
- 麥 (mai): \( b = 4 \) 錢
- 菽 (shu): \( c = 3 \) 錢
- 答 (da): \( d = 5 \) 錢
- 黍 (shu): \( e = 6 \) 錢
"""


"""
"""
