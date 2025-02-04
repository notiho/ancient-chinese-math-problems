"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
This is a system of linear equations problem. We are tasked with solving for the price of one dou (斗) of 麻 (hemp), 麥 (wheat), 菽 (beans), 答 (rice), and 黍 (millet). Let's translate the problem into equations and solve it step by step.

The equations are as follows:

1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

We will solve this system of equations using substitution and elimination.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Each equation is represented as a list of coefficients for a, b, c, d, e, and the constant term
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Function to perform Gaussian elimination
def gaussian_elimination(equations):
    n = len(equations)
    
    # Forward elimination
    for i in range(n):
        # Normalize the current row
        divisor = equations[i][i]
        for j in range(i, n + 1):
            equations[i][j] = Fraction(equations[i][j], divisor)
        
        # Eliminate the current variable from subsequent rows
        for k in range(i + 1, n):
            factor = equations[k][i]
            for j in range(i, n + 1):
                equations[k][j] -= factor * equations[i][j]
    
    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = equations[i][n]
        for j in range(i + 1, n):
            solution[i] -= equations[i][j] * solution[j]
    
    return solution

# Solve the system of equations
solution = gaussian_elimination(equations)

# Extract the results
a, b, c, d, e = solution

# Print the results
print(f"麻一斗 {a} 錢")
print(f"麥一斗 {b} 錢")
print(f"菽一斗 {c} 錢")
print(f"答一斗 {d} 錢")
print(f"黍一斗 {e} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code

1. **Input Representation**: Each equation is represented as a list of coefficients, where the last element is the constant term (e.g., 140 for the first equation).
2. **Gaussian Elimination**:
   - Forward elimination is used to transform the system into an upper triangular matrix.
   - Back substitution is then used to solve for the variables.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic without floating-point errors.

---

### Output

The solution will provide the price of one dou of each type of grain:

- 麻一斗 \( a \) 錢
- 麥一斗 \( b \) 錢
- 菽一斗 \( c \) 錢
- 答一斗 \( d \) 錢
- 黍一斗 \( e \) 錢

You can run the code to get the exact values.
"""


"""
"""
