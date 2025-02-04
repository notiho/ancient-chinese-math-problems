"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics. Let's solve it step by step using Python to represent the procedure.

### Problem Breakdown:
1. Let `甲` (A) and `乙` (B) represent the amounts of money held by person A and person B, respectively.
2. The problem gives two conditions:
   - If A takes half of B's money, A will have 48.
   - If B takes more than half of A's money, B will also have 48.
3. We need to solve for `甲` and `乙`.

The procedure uses a method similar to solving simultaneous equations. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the equations based on the problem
# Equation 1: A + (1/2)B = 48
# Equation 2: B + (3/2)A = 48

# Step 2: Rewrite the equations in standard form
# Multiply through by 2 to eliminate fractions:
# 2A + B = 96  (Equation 1)
# 3A + 2B = 144 (Equation 2)

# Step 3: Solve the system of equations using elimination
# Multiply Equation 1 by 2 to align coefficients of B:
# 4A + 2B = 192
# 3A + 2B = 144

# Subtract the second equation from the first:
# (4A + 2B) - (3A + 2B) = 192 - 144
# A = 48

# Substitute A = 48 into Equation 1 to solve for B:
# 2(48) + B = 96
# 96 + B = 96
# B = 96 - 96
# B = 24

# Final Answer:
a = 48  # 甲持錢
b = 24  # 乙持錢

print(f"甲持錢 a = {a} ，乙持錢 b = {b} 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. We first translate the problem into two equations:
   - \( 2A + B = 96 \)
   - \( 3A + 2B = 144 \)
2. Using elimination, we align the coefficients of \( B \) and subtract the equations to solve for \( A \).
3. Once \( A \) is found, we substitute it back into one of the original equations to solve for \( B \).
4. The final result is \( A = 48 \) and \( B = 24 \).

### Output:
```
甲持錢 a = 48 ，乙持錢 b = 24 。
```
"""


"""
Variable 'a' has wrong value. Expected: 36, Actual: 48"""
