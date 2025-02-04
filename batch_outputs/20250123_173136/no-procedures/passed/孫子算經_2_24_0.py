"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
This is a classic problem involving three people (甲, 乙, 丙) and their respective amounts of money. The problem can be solved using a system of equations.

### Problem Breakdown:
1. **甲's statement**: If 乙 and 丙 each give half of their money to 甲, then 甲's total money becomes 90.
   \[
   a + \frac{b}{2} + \frac{c}{2} = 90
   \]

2. **乙's statement**: If 甲 and 丙 each give half of their money to 乙, then 乙's total money becomes 70.
   \[
   b + \frac{a}{2} + \frac{c}{2} = 70
   \]

3. **丙's statement**: If 甲 and 乙 each give half of their money to 丙, then 丙's total money becomes 56.
   \[
   c + \frac{a}{2} + \frac{b}{2} = 56
   \]

We need to solve for \(a\), \(b\), and \(c\), which represent the original amounts of money held by 甲, 乙, and 丙, respectively.

---

### Python Code Solution:


"""


from fractions import Fraction

# Define the equations based on the problem
# a + b/2 + c/2 = 90
# b + a/2 + c/2 = 70
# c + a/2 + b/2 = 56

# Solve for a, b, c
# Rearrange the equations to isolate a, b, c
# Multiply through by 2 to eliminate fractions
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Using substitution or elimination, solve the system of equations
# Subtract equations to simplify
# (2a + b + c) - (2b + a + c) = 180 - 140
# a - b = 40  --> (1)

# (2b + a + c) - (2c + a + b) = 140 - 112
# b - c = 28  --> (2)

# Substitute (1) and (2) into one of the original equations
# From (1): a = b + 40
# From (2): b = c + 28

# Substitute into the first equation: 2a + b + c = 180
# 2(b + 40) + b + c = 180
# 2b + 80 + b + c = 180
# 3b + c = 100  --> (3)

# Substitute b = c + 28 into (3)
# 3(c + 28) + c = 100
# 3c + 84 + c = 100
# 4c = 16
# c = 4

# Solve for b using b = c + 28
# b = 4 + 28 = 32

# Solve for a using a = b + 40
# a = 32 + 40 = 72

# Final results
a = 72
b = 32
c = 4

# Print the results
print(f"甲持錢: {a}")
print(f"乙持錢: {b}")
print(f"丙持錢: {c}")


"""


---

### Answer:
- 甲 \(a = 72\)
- 乙 \(b = 32\)
- 丙 \(c = 4\)
"""


"""
"""
