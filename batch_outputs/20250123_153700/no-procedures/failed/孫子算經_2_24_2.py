"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
This is a classic ancient Chinese math problem involving three people (甲, 乙, 丙) and their respective amounts of money. Each person makes a statement about how much money they would have if the others gave them half of their money. The goal is to determine how much money each person originally had.

---

### Problem Breakdown:
1. **甲's statement**: If 乙 and 丙 each give half of their money to 甲, then 甲's total becomes 90.
   \[
   甲 + \frac{乙}{2} + \frac{丙}{2} = 90
   \]

2. **乙's statement**: If 甲 and 丙 each give half of their money to 乙, then 乙's total becomes 70.
   \[
   乙 + \frac{甲}{2} + \frac{丙}{2} = 70
   \]

3. **丙's statement**: If 甲 and 乙 each give half of their money to 丙, then 丙's total becomes 56.
   \[
   丙 + \frac{甲}{2} + \frac{乙}{2} = 56
   \]

We need to solve this system of equations to find the original amounts of money for 甲, 乙, and 丙.

---

### Python Code Solution:


"""


from fractions import Fraction

# Define the equations based on the problem
# 甲 + 乙/2 + 丙/2 = 90
# 乙 + 甲/2 + 丙/2 = 70
# 丙 + 甲/2 + 乙/2 = 56

# Let 甲 = x, 乙 = y, 丙 = z
# Rewrite the equations:
# x + y/2 + z/2 = 90
# y + x/2 + z/2 = 70
# z + x/2 + y/2 = 56

# Solve for x, y, z
# Multiply through by 2 to eliminate fractions:
# 2x + y + z = 180
# 2y + x + z = 140
# 2z + x + y = 112

# Subtract equations to simplify:
# (1) 2x + y + z = 180
# (2) 2y + x + z = 140
# (3) 2z + x + y = 112

# Subtract (2) from (1):
# (2x + y + z) - (2y + x + z) = 180 - 140
# x - y = 40  --> x = y + 40

# Subtract (3) from (2):
# (2y + x + z) - (2z + x + y) = 140 - 112
# y - z = 28  --> y = z + 28

# Substitute x = y + 40 and y = z + 28 into (1):
# 2x + y + z = 180
# 2(y + 40) + (z + 28) + z = 180
# 2z + 80 + z + 28 + z = 180
# 4z + 108 = 180
# 4z = 72
# z = 18

# Solve for y and x:
z = 18
y = z + 28  # y = 18 + 28 = 46
x = y + 40  # x = 46 + 40 = 86

# Final results:
a = x  # 甲's money
b = y  # 乙's money
c = z  # 丙's money

print(f"甲 originally had {a} units of money.")
print(f"乙 originally had {b} units of money.")
print(f"丙 originally had {c} units of money.")


"""


---

### Answer:
- 甲 (a) = 86
- 乙 (b) = 46
- 丙 (c) = 18
"""


"""
Variable 'a' has wrong value. Expected: 72, Actual: 86
Variable 'b' has wrong value. Expected: 32, Actual: 46
Variable 'c' has wrong value. Expected: 4, Actual: 18"""
