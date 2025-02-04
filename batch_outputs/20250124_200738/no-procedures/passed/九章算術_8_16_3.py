"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This is a system of linear equations problem. Let's solve it step by step in Python using the `Fraction` class to ensure precise calculations.

### Problem:
We are given the following equations based on the problem:

1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

Where:
- \( a \) is the price of a sheep (羊價),
- \( b \) is the price of a dog (犬價),
- \( c \) is the price of a chicken (雞價),
- \( d \) is the price of a rabbit (兔價).

We need to solve for \( a \), \( b \), \( c \), and \( d \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Define the equations as lists of coefficients and constants
eq1 = [5, 4, 3, 2, 1496]
eq2 = [4, 2, 6, 3, 1175]
eq3 = [3, 1, 7, 5, 958]
eq4 = [2, 3, 5, 1, 861]

# Function to eliminate a variable using two equations
def eliminate(eq1, eq2, var_index):
    factor1 = eq2[var_index]
    factor2 = eq1[var_index]
    new_eq = [
        factor1 * eq1[i] - factor2 * eq2[i]
        for i in range(len(eq1))
    ]
    return new_eq

# Step 1: Eliminate 'a' from eq2, eq3, and eq4 using eq1
eq2 = eliminate(eq1, eq2, 0)
eq3 = eliminate(eq1, eq3, 0)
eq4 = eliminate(eq1, eq4, 0)

# Step 2: Eliminate 'b' from eq3 and eq4 using the new eq2
eq3 = eliminate(eq2, eq3, 1)
eq4 = eliminate(eq2, eq4, 1)

# Step 3: Eliminate 'c' from eq4 using the new eq3
eq4 = eliminate(eq3, eq4, 2)

# Step 4: Back-substitute to solve for d, c, b, and a
d = Fraction(eq4[4], eq4[3])
c = Fraction(eq3[4] - eq3[3] * d, eq3[2])
b = Fraction(eq2[4] - eq2[3] * d - eq2[2] * c, eq2[1])
a = Fraction(eq1[4] - eq1[3] * d - eq1[2] * c - eq1[1] * b, eq1[0])

# Output the results
a, b, c, d
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Elimination Process**:
   - We use the elimination method to reduce the system of equations step by step.
   - First, we eliminate \( a \) from the second, third, and fourth equations using the first equation.
   - Next, we eliminate \( b \) from the third and fourth equations using the modified second equation.
   - Finally, we eliminate \( c \) from the fourth equation using the modified third equation.

2. **Back-Substitution**:
   - Once we have a single equation with only \( d \), we solve for \( d \).
   - Then, we substitute \( d \) back into the previous equations to solve for \( c \), \( b \), and \( a \) step by step.

3. **Fraction Class**:
   - The `Fraction` class ensures that all calculations are precise and avoids floating-point errors.

---

### Final Answer:
After running the code, the values of \( a \), \( b \), \( c \), and \( d \) will be:

- \( a \): Price of a sheep (羊價)
- \( b \): Price of a dog (犬價)
- \( c \): Price of a chicken (雞價)
- \( d \): Price of a rabbit (兔價)
"""


"""
"""
