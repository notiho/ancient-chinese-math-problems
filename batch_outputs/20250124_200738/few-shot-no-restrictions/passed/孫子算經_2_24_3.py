"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
This problem involves three people, A (甲), B (乙), and C (丙), who each hold an unknown amount of money. They make statements about how their money changes when others contribute half of their money to them. The goal is to determine how much money each person originally had.

---

### Problem Breakdown:
1. **甲 (A)** says: "If each of you (乙 and 丙) gives me half of your money, I will have 90."
2. **乙 (B)** says: "If each of you (甲 and 丙) gives me half of your money, I will have 70."
3. **丙 (C)** says: "If each of you (甲 and 乙) gives me half of your money, I will have 56."

We need to find the original amounts of money held by 甲 (A), 乙 (B), and 丙 (C).

---

### Solution Procedure:
1. Let the original amounts of money held by 甲, 乙, and 丙 be \( x \), \( y \), and \( z \), respectively.
2. Translate the statements into equations:
   - From 甲: \( x + \frac{y}{2} + \frac{z}{2} = 90 \)
   - From 乙: \( y + \frac{x}{2} + \frac{z}{2} = 70 \)
   - From 丙: \( z + \frac{x}{2} + \frac{y}{2} = 56 \)
3. Solve this system of equations to find \( x \), \( y \), and \( z \).

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the amounts of money held by 甲 (A), 乙 (B), and 丙 (C)
x, y, z = symbols('x y z')

# Define the equations based on the problem statements
eq1 = Eq(x + y / 2 + z / 2, 90)  # From 甲's statement
eq2 = Eq(y + x / 2 + z / 2, 70)  # From 乙's statement
eq3 = Eq(z + x / 2 + y / 2, 56)  # From 丙's statement

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the results
a = solution[x]  # 甲's original amount
b = solution[y]  # 乙's original amount
c = solution[z]  # 丙's original amount

# Print the results
print(f"甲 originally had: {a}")
print(f"乙 originally had: {b}")
print(f"丙 originally had: {c}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `x`, `y`, and `z` to represent the original amounts of money held by 甲, 乙, and 丙, respectively.
2. **Set Up Equations**: The equations are derived from the problem statements, where each person's total after receiving half of the others' money is given.
3. **Solve the System**: Using `sympy.solve`, we solve the three equations simultaneously to find the values of \( x \), \( y \), and \( z \).
4. **Output the Results**: The solution gives the original amounts of money held by each person.

---

### Answer:
After running the code, the solution will provide the values of \( a \), \( b \), and \( c \), which are the original amounts of money held by 甲, 乙, and 丙, respectively.
"""


"""
"""
