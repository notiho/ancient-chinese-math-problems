"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step using Python code.

### Problem Breakdown:
Let:
- 牛 (cattle) price = `a`
- 羊 (sheep) price = `b`
- 豕 (pig) price = `c`

From the problem, we have the following equations:
1. \( 2a + 5b = 13c + 1000 \)  (selling 2 cattle and 5 sheep to buy 13 pigs with 1000 leftover)
2. \( 3a + 3c = 9b \)          (selling 3 cattle and 3 pigs to buy 9 sheep, no leftover or shortage)
3. \( 6b + 8c = 5a - 600 \)    (selling 6 sheep and 8 pigs to buy 5 cattle, 600 short)

We solve these equations to find \( a \), \( b \), and \( c \).

### Python Code:

"""


from fractions import Fraction

# Define the equations
# 1. 2a + 5b = 13c + 1000
# 2. 3a + 3c = 9b
# 3. 6b + 8c = 5a - 600

# Solve for a, b, and c
# Rearrange equations into standard form:
# 1. 2a + 5b - 13c = 1000
# 2. 3a - 9b + 3c = 0
# 3. -5a + 6b + 8c = -600

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
eq1 = [2, 5, -13, 1000]
# Equation 2: 3a - 9b + 3c = 0
eq2 = [3, -9, 3, 0]
# Equation 3: -5a + 6b + 8c = -600
eq3 = [-5, 6, 8, -600]

# Use substitution or elimination to solve the system of equations
# We'll use a manual approach to solve step by step

# Step 1: Eliminate one variable (e.g., a) using equations 1 and 2
# Multiply eq1 by 3 and eq2 by 2 to align coefficients of a
eq1_scaled = [3 * x for x in eq1]  # [6, 15, -39, 3000]
eq2_scaled = [2 * x for x in eq2]  # [6, -18, 6, 0]

# Subtract eq2_scaled from eq1_scaled to eliminate a
eq4 = [eq1_scaled[i] - eq2_scaled[i] for i in range(4)]  # [0, 33, -45, 3000]

# Simplify eq4: 33b - 45c = 3000
# Divide through by 3: 11b - 15c = 1000
eq4 = [11, -15, 0, 1000]

# Step 2: Eliminate a using equations 1 and 3
# Multiply eq1 by 5 and eq3 by 2 to align coefficients of a
eq1_scaled = [5 * x for x in eq1]  # [10, 25, -65, 5000]
eq3_scaled = [2 * x for x in eq3]  # [-10, 12, 16, -1200]

# Add eq1_scaled and eq3_scaled to eliminate a
eq5 = [eq1_scaled[i] + eq3_scaled[i] for i in range(4)]  # [0, 37, -49, 3800]

# Simplify eq5: 37b - 49c = 3800
eq5 = [37, -49, 0, 3800]

# Step 3: Solve for b and c using eq4 and eq5
# Align coefficients of b in eq4 and eq5
eq4_scaled = [37 * x for x in eq4]  # [407, -555, 0, 37000]
eq5_scaled = [11 * x for x in eq5]  # [407, -539, 0, 41800]

# Subtract eq4_scaled from eq5_scaled to eliminate b
eq6 = [eq5_scaled[i] - eq4_scaled[i] for i in range(4)]  # [0, 16, 0, 4800]

# Simplify eq6: 16c = 4800
c = Fraction(4800, 16)  # c = 300

# Substitute c back into eq4 to solve for b
# 11b - 15c = 1000
b = Fraction(1000 + 15 * c, 11)  # b = 500

# Substitute b and c back into eq1 to solve for a
# 2a + 5b - 13c = 1000
a = Fraction(1000 + 13 * c - 5 * b, 2)  # a = 800

# Final results
print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


### Final Answer:
- 牛價 \( a = 800 \)
- 羊價 \( b = 500 \)
- 豕價 \( c = 300 \)
"""


"""
"""
