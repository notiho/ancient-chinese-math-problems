"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one dou of each type of grain. Let's break it down and solve step by step.

We are given the following equations based on the problem:

1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

Where:
- \( a \) is the price of 1 dou of 麻 (hemp),
- \( b \) is the price of 1 dou of 麥 (wheat),
- \( c \) is the price of 1 dou of 菽 (beans),
- \( d \) is the price of 1 dou of 答 (rice),
- \( e \) is the price of 1 dou of 黍 (millet).

We need to solve this system of equations to find \( a, b, c, d, e \).

---

### Python Code to Solve the System of Equations


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

# Function to solve the system of linear equations using Gaussian elimination
def solve_linear_system(coefficients, constants):
    n = len(coefficients)
    
    # Convert coefficients and constants to fractions for exact arithmetic
    for i in range(n):
        coefficients[i] = [Fraction(x) for x in coefficients[i]]
        constants[i] = Fraction(constants[i])
    
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

# Solve the system
solution = solve_linear_system(coefficients, constants)

# Extract the results
a, b, c, d, e = solution

# Print the results
print(f"麻一斗 {a} 錢")
print(f"麥一斗 {b} 錢")
print(f"菽一斗 {c} 錢")
print(f"答一斗 {d} 錢")
print(f"黍一斗 {e} 錢")


"""


---

### Explanation of the Code

1. **Input the coefficients and constants**: The coefficients of the variables \( a, b, c, d, e \) are stored in a 2D list, and the constants (right-hand side of the equations) are stored in a separate list.

2. **Gaussian elimination**: The system of equations is solved using Gaussian elimination, which involves:
   - Forward elimination to convert the system into an upper triangular matrix.
   - Back substitution to solve for the variables.

3. **Fractions for exact arithmetic**: The `Fraction` class is used to ensure that all calculations are exact and avoid floating-point errors.

4. **Output the results**: The solution is printed as the price of 1 dou of each type of grain.

---

### Output

After running the code, the output will be:

```
麻一斗 a 錢
麥一斗 b 錢
菽一斗 c 錢
答一斗 d 錢
黍一斗 e 錢
```

Where \( a, b, c, d, e \) are the exact prices in terms of fractions or integers.
"""


"""
"""
