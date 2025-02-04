"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step.

### Problem Breakdown:
We are tasked with finding the price of a cow (`牛`), a sheep (`羊`), and a pig (`豕`). Let:
- `a` = price of a cow
- `b` = price of a sheep
- `c` = price of a pig

The problem gives us three equations based on the transactions:

1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left:
   \[
   2a + 5b = 13c + 1000
   \]

2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left:
   \[
   3a + 3c = 9b
   \]

3. Selling 6 sheep and 8 pigs to buy 5 cows, but falling short by 600:
   \[
   6b + 8c + 600 = 5a
   \]

We now solve this system of equations.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# 1. 2a + 5b = 13c + 1000
# 2. 3a + 3c = 9b
# 3. 6b + 8c + 600 = 5a

# Solve the system of equations step by step:

# From equation (2): 3a + 3c = 9b
# Divide through by 3:
# a + c = 3b
# => a = 3b - c

# Substitute a = 3b - c into equations (1) and (3):

# Equation (1): 2a + 5b = 13c + 1000
# => 2(3b - c) + 5b = 13c + 1000
# => 6b - 2c + 5b = 13c + 1000
# => 11b - 15c = 1000  ---- (4)

# Equation (3): 6b + 8c + 600 = 5a
# => 6b + 8c + 600 = 5(3b - c)
# => 6b + 8c + 600 = 15b - 5c
# => 6b + 8c + 600 - 15b + 5c = 0
# => -9b + 13c + 600 = 0
# => 9b = 13c + 600
# => 3b = (13c + 600) / 3  ---- (5)

# Solve equations (4) and (5):

# From (4): 11b = 15c + 1000
# => b = (15c + 1000) / 11  ---- (6)

# Substitute (6) into (5):
# 3((15c + 1000) / 11) = (13c + 600) / 3
# => (45c + 3000) / 11 = (13c + 600) / 3
# Cross-multiply:
# 3(45c + 3000) = 11(13c + 600)
# => 135c + 9000 = 143c + 6600
# => 9000 - 6600 = 143c - 135c
# => 2400 = 8c
# => c = 300

# Substitute c = 300 into (6):
# b = (15(300) + 1000) / 11
# => b = (4500 + 1000) / 11
# => b = 5500 / 11
# => b = 500

# Substitute b = 500 and c = 300 into a = 3b - c:
# a = 3(500) - 300
# => a = 1500 - 300
# => a = 1200

# Final results:
a = 1200  # Price of a cow
b = 500   # Price of a sheep
c = 300   # Price of a pig

print(f"牛價 a = {a}，羊價 b = {b}，豕價 c = {c}")
#----- content ends here -----


"""


---

### Explanation of Results:
- The price of a cow (`牛價`) is **1200**.
- The price of a sheep (`羊價`) is **500**.
- The price of a pig (`豕價`) is **300**.
"""


"""
"""
