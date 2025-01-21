"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one dou of each type of grain. Let's break it down and solve step by step.

We are solving for the prices of 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), and 黍 (shu), represented as variables `a`, `c`, `e`, `g`, and `i` respectively. Each equation corresponds to the total cost of a combination of grains.

The equations are as follows:

1. \( 9a + 7c + 3e + 2g + 5i = 140 \)
2. \( 7a + 6c + 4e + 5g + 3i = 128 \)
3. \( 3a + 5c + 7e + 6g + 4i = 116 \)
4. \( 2a + 5c + 3e + 9g + 4i = 112 \)
5. \( 1a + 3c + 2e + 8g + 5i = 95 \)

We will solve this system of equations using Python.

---


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

# Constants (total cost in each equation)
constants = [140, 128, 116, 112, 95]

# Solve using substitution/elimination (Gaussian elimination)
def gaussian_elimination(coefficients, constants):
    n = len(constants)
    # Convert coefficients and constants to fractions for exact arithmetic
    coefficients = [[Fraction(x) for x in row] for row in coefficients]
    constants = [Fraction(x) for x in constants]

    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = coefficients[i][i]
        for j in range(i, n):
            coefficients[i][j] /= diag
        constants[i] /= diag

        # Eliminate the current variable from subsequent rows
        for k in range(i + 1, n):
            factor = coefficients[k][i]
            for j in range(i, n):
                coefficients[k][j] -= factor * coefficients[i][j]
            constants[k] -= factor * constants[i]

    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = constants[i]
        for j in range(i + 1, n):
            solution[i] -= coefficients[i][j] * solution[j]

    return solution

# Solve the system of equations
solution = gaussian_elimination(coefficients, constants)

# Extract the solution
a, c, e, g, i = solution

# Print the results
print(f"麻: {a} 錢/斗")
print(f"麥: {c} 錢/斗")
print(f"菽: {e} 錢/斗")
print(f"答: {g} 錢/斗")
print(f"黍: {i} 錢/斗")


"""


---

### Explanation of the Code:
1. **Fractions**: We use the `Fraction` class to ensure exact arithmetic without floating-point errors.
2. **Gaussian Elimination**: This method systematically eliminates variables to solve the system of linear equations.
3. **Forward Elimination**: We make the diagonal elements of the coefficient matrix equal to 1 and eliminate variables from subsequent rows.
4. **Back Substitution**: Once the matrix is in row-echelon form, we solve for the variables starting from the last row.

### Output:
The solution will provide the price of one dou of each type of grain in terms of qian (錢). For example:
```
麻: a 錢/斗
麥: c 錢/斗
菽: e 錢/斗
答: g 錢/斗
黍: i 錢/斗
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 4
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 3
Missing variable in output: 'f'
Variable 'g' has wrong value. Expected: 1, Actual: 5
Missing variable in output: 'h'
Variable 'i' has wrong value. Expected: 1, Actual: 6
Missing variable in output: 'j'"""
