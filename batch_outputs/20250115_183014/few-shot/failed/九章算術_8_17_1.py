"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one dou (斗) of each type of grain (麻, 麥, 菽, 答, 黍). The solution uses the ancient Chinese method of solving simultaneous equations, which is similar to Gaussian elimination. Here's the Python implementation:


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

# Results (total price in 錢)
results = [140, 128, 116, 112, 95]

# Convert everything to fractions for precise calculations
coefficients = [[Fraction(x) for x in row] for row in coefficients]
results = [Fraction(x) for x in results]

# Perform Gaussian elimination
n = len(coefficients)

# Forward elimination
for i in range(n):
    # Normalize the pivot row
    pivot = coefficients[i][i]
    for j in range(i, n):
        coefficients[i][j] /= pivot
    results[i] /= pivot

    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, n):
        factor = coefficients[k][i]
        for j in range(i, n):
            coefficients[k][j] -= factor * coefficients[i][j]
        results[k] -= factor * results[i]

# Back substitution
solution = [Fraction(0)] * n
for i in range(n - 1, -1, -1):
    solution[i] = results[i]
    for j in range(i + 1, n):
        solution[i] -= coefficients[i][j] * solution[j]

# Extract the solution
a, b = divmod(solution[0].numerator, solution[0].denominator)
c, d = divmod(solution[1].numerator, solution[1].denominator)
e, f = divmod(solution[2].numerator, solution[2].denominator)
g, h = divmod(solution[3].numerator, solution[3].denominator)
i, j = divmod(solution[4].numerator, solution[4].denominator)

# Output the results
print(f"麻 {a}斗 {b}錢")
print(f"麥 {c}斗 {d}錢")
print(f"菽 {e}斗 {f}錢")
print(f"答 {g}斗 {h}錢")
print(f"黍 {i}斗 {j}錢")


"""


### Explanation of the Code:
1. **Input Representation**: The coefficients of the grains and their respective prices are represented as a matrix and a result vector.
2. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations without floating-point errors.
3. **Gaussian Elimination**:
   - **Forward Elimination**: The matrix is transformed into an upper triangular form.
   - **Back Substitution**: The solution is obtained by solving the equations from the last row upwards.
4. **Output**: The solution is converted into the format of dou (斗) and qian (錢).

### Example Output:
If the calculations are correct, the output will be in the form:
```
麻 a斗 b錢
麥 c斗 d錢
菽 e斗 f錢
答 g斗 h錢
黍 i斗 j錢
```

This method adheres to the ancient Chinese procedure for solving simultaneous equations.
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
