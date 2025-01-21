"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
This is a system of linear equations problem. We are tasked with solving for the price of one dou (斗) of each type of grain: 麻 (hemp), 麥 (wheat), 菽 (beans), 答 (rice), and 黍 (millet). Let the price of one dou of each grain be represented as follows:

- 麻: `a` 錢
- 麥: `c` 錢
- 菽: `e` 錢
- 答: `g` 錢
- 黍: `i` 錢

The problem gives us five equations based on the total price of combinations of grains. Let's solve this step by step in Python.

---

### Python Code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 9a + 7c + 3e + 2g + 5i = 140
# 7a + 6c + 4e + 5g + 3i = 128
# 3a + 5c + 7e + 6g + 4i = 116
# 2a + 5c + 3e + 9g + 4i = 112
# 1a + 3c + 2e + 8g + 5i = 95

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

# Solve the system of linear equations using substitution or elimination
# We will use Gaussian elimination to solve this step by step.

def gaussian_elimination(coefficients, constants):
    n = len(constants)
    # Convert coefficients and constants to fractions for exact arithmetic
    A = [[Fraction(coefficients[i][j]) for j in range(n)] for i in range(n)]
    B = [Fraction(constants[i]) for i in range(n)]
    
    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = A[i][i]
        for j in range(i, n):
            A[i][j] /= diag
        B[i] /= diag
        
        # Eliminate the current column in rows below
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]
    
    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    
    return x

# Solve for the prices
prices = gaussian_elimination(coefficients, constants)

# Extract the results
a, c, e, g, i = prices

# Print the results
print(f"麻: {a} 錢")
print(f"麥: {c} 錢")
print(f"菽: {e} 錢")
print(f"答: {g} 錢")
print(f"黍: {i} 錢")


"""


---

### Explanation of the Code:
1. **Input the equations**: The coefficients of the grains and their total prices are input as lists.
2. **Gaussian Elimination**:
   - Forward elimination is used to convert the system into an upper triangular matrix.
   - Back substitution is used to solve for the variables.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.
4. **Output**: The prices of one dou of each grain are printed as fractions.

---

### Expected Output:
The output will provide the price of one dou of each grain in terms of 錢:

```
麻: a 錢
麥: c 錢
菽: e 錢
答: g 錢
黍: i 錢
```

Where `a`, `c`, `e`, `g`, and `i` are the exact fractional values of the prices.
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
