"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
答曰：甲 a ，乙 b ，丙 c 。
"""

"""
This is a classic problem involving three people (甲, 乙, 丙) and their respective amounts of money. Each person asks the others to give them half of their money, and after receiving the contributions, their total money reaches a specific amount. We need to determine how much money each person originally had.

---

### Problem Breakdown:
1. 甲 says: "If each of you (乙 and 丙) gives me half of your money, my total becomes 90."
   - \( 甲 + \frac{乙}{2} + \frac{丙}{2} = 90 \)

2. 乙 says: "If each of you (甲 and 丙) gives me half of your money, my total becomes 70."
   - \( 乙 + \frac{甲}{2} + \frac{丙}{2} = 70 \)

3. 丙 says: "If each of you (甲 and 乙) gives me half of your money, my total becomes 56."
   - \( 丙 + \frac{甲}{2} + \frac{乙}{2} = 56 \)

We need to solve these three equations to find the original amounts of money held by 甲, 乙, and 丙.

---

### Python Code Solution:


"""


from fractions import Fraction

# Define the equations as variables
# Let a = 甲, b = 乙, c = 丙
# From the problem:
# a + b/2 + c/2 = 90
# b + a/2 + c/2 = 70
# c + a/2 + b/2 = 56

# Solve the equations step by step
# Multiply through by 2 to eliminate fractions:
# 2a + b + c = 180
# 2b + a + c = 140
# 2c + a + b = 112

# Subtract equations to isolate variables
# (1) 2a + b + c = 180
# (2) 2b + a + c = 140
# Subtract (2) from (1):
# (2a + b + c) - (2b + a + c) = 180 - 140
# a - b = 40  --> a = b + 40

# (2) 2b + a + c = 140
# (3) 2c + a + b = 112
# Subtract (3) from (2):
# (2b + a + c) - (2c + a + b) = 140 - 112
# b - c = 28  --> b = c + 28

# Substitute b = c + 28 and a = b + 40 into (1):
# 2a + b + c = 180
# 2(b + 40) + b + c = 180
# 2(c + 28 + 40) + (c + 28) + c = 180
# 2c + 136 + c + 28 + c = 180
# 4c + 164 = 180
# 4c = 16
# c = 4

# Solve for b and a:
c = 4
b = c + 28  # b = 4 + 28 = 32
a = b + 40  # a = 32 + 40 = 72

# Final results:
a, b, c = Fraction(a), Fraction(b), Fraction(c)
print(f"甲持錢: {a}, 乙持錢: {b}, 丙持錢: {c}")


"""


---

### Final Answer:
- 甲持錢: \( a = 72 \)
- 乙持錢: \( b = 32 \)
- 丙持錢: \( c = 4 \)
"""


"""
"""
