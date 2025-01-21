"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one unit (斗) of each commodity (麻, 麥, 菽, 答, 黍). Below is the Python code that follows the described procedure ("方程術") to solve the problem step by step.


"""


from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95]    # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Step 1: Elimination process to reduce the system to upper triangular form
for i in range(len(equations)):
    # Normalize the pivot row
    pivot = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], pivot)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(equations)):
        factor = equations[k][i]
        for j in range(len(equations[k])):
            equations[k][j] -= factor * equations[i][j]

# Step 2: Back substitution to solve for each variable
results = [0] * len(equations)
for i in range(len(equations) - 1, -1, -1):
    results[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        results[i] -= equations[i][j] * results[j]

# Extract results
a, b = divmod(results[0].numerator, results[0].denominator)  # 麻
c, d = divmod(results[1].numerator, results[1].denominator)  # 麥
e, f = divmod(results[2].numerator, results[2].denominator)  # 菽
g, h = divmod(results[3].numerator, results[3].denominator)  # 答
i, j = divmod(results[4].numerator, results[4].denominator)  # 黍

# Output results
print(f"麻 {a}斗 {b}錢")
print(f"麥 {c}斗 {d}錢")
print(f"菽 {e}斗 {f}錢")
print(f"答 {g}斗 {h}錢")
print(f"黍 {i}斗 {j}錢")


"""


### Explanation of the Code:
1. **Input Representation**: The system of equations is represented as a list of lists, where each inner list corresponds to the coefficients of one equation, including the constant term on the right-hand side.

2. **Gaussian Elimination**:
   - The system is reduced to an upper triangular form by normalizing the pivot row and eliminating the variable from the rows below.
   - Fractions are used to ensure exact arithmetic.

3. **Back Substitution**:
   - Starting from the last equation, each variable is solved by substituting the known values of the variables already determined.

4. **Result Extraction**:
   - The results are converted into the format of "斗" and "錢" by dividing the numerator and denominator of the fraction.

### Output:
The output will display the price of one unit (斗) of each commodity in terms of "斗" and "錢".
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'b' has wrong value. Expected: 7, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 4
Variable 'd' has wrong value. Expected: 4, Actual: 0
Variable 'e' has wrong value. Expected: 1, Actual: 3
Variable 'f' has wrong value. Expected: 3, Actual: 0
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 5, Actual: 0
Variable 'i' has wrong value. Expected: 1, Actual: 6
Variable 'j' has wrong value. Expected: 6, Actual: 0"""
