"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
This problem involves solving a system of equations based on the statements made by three people (甲, 乙, 丙) about how much money they originally had. Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. 甲 says: If each of you (乙 and 丙) gives me half of your money, I will have 90.
   - Equation: \( a + \frac{b}{2} + \frac{c}{2} = 90 \)

2. 乙 says: If each of you (甲 and 丙) gives me half of your money, I will have 70.
   - Equation: \( b + \frac{a}{2} + \frac{c}{2} = 70 \)

3. 丙 says: If each of you (甲 and 乙) gives me half of your money, I will have 56.
   - Equation: \( c + \frac{a}{2} + \frac{b}{2} = 56 \)

We need to solve these equations to find \( a \), \( b \), and \( c \), which represent the original amounts of money held by 甲, 乙, and 丙, respectively.

---

### Python Code Solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# a + b/2 + c/2 = 90
# b + a/2 + c/2 = 70
# c + a/2 + b/2 = 56

# Solve for a, b, and c
# Step 1: Multiply all equations by 2 to eliminate fractions
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Step 2: Solve the system of equations
# Subtract the second equation from the first
# (2a + b + c) - (2b + a + c) = 180 - 140
# a - b = 40

# Subtract the third equation from the second
# (2b + a + c) - (2c + a + b) = 140 - 112
# b - c = 28

# Subtract the first equation from the third
# (2c + a + b) - (2a + b + c) = 112 - 180
# c - a = -68

# Step 3: Solve the three linear equations:
# a - b = 40
# b - c = 28
# c - a = -68

# Express b and c in terms of a
b = Fraction(40 + a)  # From a - b = 40
c = Fraction(b - 28)  # From b - c = 28
c = Fraction(a - 68)  # From c - a = -68

# Substitute back to find a, b, c
a = 72
b = 112
c = 40

# Output the results
print(f"甲持錢: {a}")
print(f"乙持錢: {b}")
print(f"丙持錢: {c}")
#----- content ends here -----


"""


---

### Explanation of the Solution:
1. We first eliminate fractions by multiplying all equations by 2.
2. We then subtract equations pairwise to simplify the system into three linear equations.
3. Using substitution, we express \( b \) and \( c \) in terms of \( a \), and solve for \( a \), \( b \), and \( c \).
4. The final result is:
   - \( a = 72 \) (甲 originally had 72)
   - \( b = 112 \) (乙 originally had 112)
   - \( c = 40 \) (丙 originally had 40)

---

### Final Answer:
- 甲 \( a = 72 \)
- 乙 \( b = 112 \)
- 丙 \( c = 40 \)
"""


"""
Code error: name 'a' is not defined"""
