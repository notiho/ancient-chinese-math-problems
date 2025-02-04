"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. Let's solve it step by step using Python to represent the procedure.

### Problem Breakdown:
1. Let `甲` (A) and `乙` (B) represent the amounts of money held by person A and person B, respectively.
2. The problem states:
   - If A takes half of B's money, A will have 48.
   - If B takes more than half of A's money, B will also have 48.
3. Using these conditions, we can form two equations:
   - \( A + \frac{1}{2}B = 48 \)
   - \( B + \frac{3}{2}A = 48 \)

We solve this system of equations using the ancient Chinese method described in the problem.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# 2A + B = 96  (Multiply the first equation by 2 to eliminate the fraction)
# 2A + 3B = 144 (Multiply the second equation by 2 to eliminate the fraction)

# Step 1: Set up the coefficients and constants
coefficients_1 = [2, 1]  # Coefficients of A and B in the first equation
coefficients_2 = [2, 3]  # Coefficients of A and B in the second equation
constant_1 = 96          # Constant term in the first equation
constant_2 = 144         # Constant term in the second equation

# Step 2: Eliminate one variable (B) by subtracting the equations
# Multiply the first equation by 3 and the second equation by 1 to align B's coefficients
multiplier_1 = 3
multiplier_2 = 1

# New equations after multiplication:
# 6A + 3B = 288  (First equation multiplied by 3)
# 2A + 3B = 144  (Second equation remains as is)

# Subtract the second equation from the first to eliminate B:
# (6A + 3B) - (2A + 3B) = 288 - 144
# 4A = 144
A = Fraction(144, 4)  # Solve for A
A = int(A)  # Convert to integer since money is discrete

# Step 3: Substitute A back into one of the original equations to solve for B
# Using the first equation: 2A + B = 96
B = Fraction(96 - 2 * A, 1)  # Solve for B
B = int(B)  # Convert to integer since money is discrete

# Final Answer
a = A
b = B

print(f"甲持錢 {a} ，乙持錢 {b} 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The equations are derived from the problem statement:
   - \( 2A + B = 96 \)
   - \( 2A + 3B = 144 \)
2. The coefficients and constants are set up as lists for clarity.
3. The elimination method is used to solve the system of equations:
   - Multiply the equations to align the coefficients of \( B \).
   - Subtract one equation from the other to eliminate \( B \) and solve for \( A \).
4. Substitute \( A \) back into one of the original equations to solve for \( B \).
5. The solution is printed as the final answer.

---

### Final Answer:
```
甲持錢 36 ，乙持錢 24 。
```
"""


"""
"""
