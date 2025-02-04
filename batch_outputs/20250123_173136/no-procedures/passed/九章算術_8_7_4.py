"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step.

### Problem Breakdown:
1. Let the price of a cow (牛) be `a`, the price of a sheep (羊) be `b`, and the price of a pig (豕) be `c`.
2. From the problem, we have the following equations:
   - Selling 2 cows and 5 sheep can buy 13 pigs, with 1000 money left:
     \[
     2a + 5b = 13c + 1000
     \]
   - Selling 3 cows and 3 pigs can buy 9 sheep, with no money left:
     \[
     3a + 3c = 9b
     \]
   - Selling 6 sheep and 8 pigs can buy 5 cows, but 600 money is still needed:
     \[
     6b + 8c + 600 = 5a
     \]

### Solve the system of equations:
We will solve these equations step by step.


"""


from fractions import Fraction

# Define the equations
# 1. 2a + 5b = 13c + 1000
# 2. 3a + 3c = 9b
# 3. 6b + 8c + 600 = 5a

# Step 1: Express `a` in terms of `b` and `c` from equation (2)
# 3a = 9b - 3c
# a = (9b - 3c) / 3
a = lambda b, c: Fraction(9 * b - 3 * c, 3)

# Step 2: Substitute `a` into equation (1)
# 2a + 5b = 13c + 1000
# 2((9b - 3c) / 3) + 5b = 13c + 1000
# (18b - 6c) / 3 + 5b = 13c + 1000
# 6b - 2c + 5b = 13c + 1000
# 11b - 2c = 13c + 1000
# 11b = 15c + 1000
# b = (15c + 1000) / 11
b = lambda c: Fraction(15 * c + 1000, 11)

# Step 3: Substitute `a` and `b` into equation (3)
# 6b + 8c + 600 = 5a
# 6((15c + 1000) / 11) + 8c + 600 = 5((9b - 3c) / 3)
# 6(15c + 1000) / 11 + 8c + 600 = 5(9((15c + 1000) / 11) - 3c) / 3
# Simplify step by step:

# Left-hand side:
# 6(15c + 1000) / 11 + 8c + 600
# = (90c + 6000) / 11 + 8c + 600
# = (90c + 6000 + 88c + 6600) / 11
# = (178c + 12600) / 11

# Right-hand side:
# 5(9((15c + 1000) / 11) - 3c) / 3
# = 5((135c + 9000) / 11 - 3c) / 3
# = 5((135c + 9000 - 33c) / 11) / 3
# = 5((102c + 9000) / 11) / 3
# = (510c + 45000) / 33

# Final equation:
# (178c + 12600) / 11 = (510c + 45000) / 33
# Cross-multiply:
# 33(178c + 12600) = 11(510c + 45000)
# 5874c + 415800 = 5610c + 495000
# 5874c - 5610c = 495000 - 415800
# 264c = 79200
# c = 79200 / 264
# c = 300

# Step 4: Solve for `b` and `a` using `c = 300`
c = 300
b = b(c)  # b = (15 * 300 + 1000) / 11
b = Fraction(15 * 300 + 1000, 11)

a = a(b, c)  # a = (9 * b - 3 * c) / 3
a = Fraction(9 * b - 3 * c, 3)

# Final results
print(f"牛價 a = {a} (in money units)")
print(f"羊價 b = {b} (in money units)")
print(f"豕價 c = {c} (in money units)")


"""


### Final Answer:
- 牛價 \(a = 1100\) (in money units)
- 羊價 \(b = 500\) (in money units)
- 豕價 \(c = 300\) (in money units)
"""


"""
"""
