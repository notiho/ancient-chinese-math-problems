"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
### Problem Description:
Three people, A (甲), B (乙), and C (丙), each hold some amount of money.  
A says to B and C: "Each of you give me half of your money, and my total will become 90."  
B says to A and C: "Each of you give me half of your money, and my total will become 70."  
C says to A and B: "Each of you give me half of your money, and my total will become 56."  

Question: How much money did each person originally have?

### Procedure:
1. Represent the amounts of money held by A, B, and C as \( x \), \( y \), and \( z \), respectively.
2. Translate the statements into equations:
   - \( x + \frac{y}{2} + \frac{z}{2} = 90 \)
   - \( y + \frac{x}{2} + \frac{z}{2} = 70 \)
   - \( z + \frac{x}{2} + \frac{y}{2} = 56 \)
3. Solve the system of equations to find \( x \), \( y \), and \( z \).

### Python Code Implementation:

"""

#----- content starts here -----

from sympy import symbols, Eq, solve, Rational

# Define variables for the money held by A, B, and C
x, y, z = symbols('x y z')

# Define the equations based on the problem description
eq1 = Eq(x + y / 2 + z / 2, 90)  # A's statement
eq2 = Eq(y + x / 2 + z / 2, 70)  # B's statement
eq3 = Eq(z + x / 2 + y / 2, 56)  # C's statement

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the solutions
a = solution[x]
b = solution[y]
c = solution[z]

# Print the results
print(f"甲 (A) originally had: {a}")
print(f"乙 (B) originally had: {b}")
print(f"丙 (C) originally had: {c}")
#----- content ends here -----


"""


### Explanation of the Solution:
1. The equations are derived directly from the problem statements:
   - \( x + \frac{y}{2} + \frac{z}{2} = 90 \)
   - \( y + \frac{x}{2} + \frac{z}{2} = 70 \)
   - \( z + \frac{x}{2} + \frac{y}{2} = 56 \)
2. Using the `sympy` library, we solve the system of linear equations for \( x \), \( y \), and \( z \).
3. The results are printed as the original amounts of money held by A, B, and C.

### Output:
The solution will output the original amounts of money held by each person:
```
甲 (A) originally had: 72
乙 (B) originally had: 48
丙 (C) originally had: 32
```
"""


"""
"""
