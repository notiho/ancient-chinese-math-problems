"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one dou of each type of grain. Let's break it down and solve it step by step.

The problem gives us the following equations based on the total cost of the grains:

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

We will solve this system of equations using substitution and elimination.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
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
        # Make the diagonal element 1
        diag = equations[i][i]
        for j in range(i, n + 1):
            equations[i][j] = Fraction(equations[i][j], diag)
        
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

### Explanation of the Code:
1. **Input the equations**: The coefficients of the variables and the constants are stored in a list of lists.
2. **Gaussian elimination**:
   - Perform forward elimination to make the matrix upper triangular.
   - Perform back substitution to solve for the variables.
3. **Output the solution**: The solution gives the price of 1 dou of each type of grain.

---

### Final Answer:
After running the code, the solution will be:
- 麻一斗 \( a \) 錢
- 麥一斗 \( b \) 錢
- 菽一斗 \( c \) 錢
- 答一斗 \( d \) 錢
- 黍一斗 \( e \) 錢
"""


"""
"""
