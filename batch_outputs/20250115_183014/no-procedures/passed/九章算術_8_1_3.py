"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This is a classic system of equations problem from ancient Chinese mathematics. Let's break it down and solve step by step.

### Problem Explanation:
- There are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).
- The problem gives two conditions:
  1. 7 bundles (秉) of upper grain lose 1 dou (斗) of content, but when 2 bundles of lower grain are added, the total becomes 10 dou.
  2. 8 bundles of lower grain gain 1 dou of content, but when 2 bundles of upper grain are added, the total becomes 10 dou.
  
We are tasked to find how much grain (in dou) is in 1 bundle of upper grain and 1 bundle of lower grain.

---

### Solution in Python:


"""


from fractions import Fraction

# Let x = the amount of grain (in dou) in 1 bundle of upper grain (上禾)
# Let y = the amount of grain (in dou) in 1 bundle of lower grain (下禾)

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11
# Equation 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Solve the system of equations:
# From Equation 1: 7x + 2y = 11
# From Equation 2: 2x + 8y = 9

# Step 1: Solve for y in terms of x from Equation 1
# 2y = 11 - 7x
# y = (11 - 7x) / 2

# Step 2: Substitute y into Equation 2
# 2x + 8((11 - 7x) / 2) = 9
# 2x + 4(11 - 7x) = 9
# 2x + 44 - 28x = 9
# -26x = -35
# x = 35 / 26

# Step 3: Solve for y using x = 35 / 26
# y = (11 - 7x) / 2
# y = (11 - 7(35 / 26)) / 2
# y = (11 - 245 / 26) / 2
# y = (286 / 26 - 245 / 26) / 2
# y = (41 / 26) / 2
# y = 41 / 52

# Final results:
a = 1  # Upper grain (上禾) bundles
b = Fraction(35, 26)  # Grain in 1 bundle of upper grain (in dou)
c = 1  # Lower grain (下禾) bundles
d = Fraction(41, 52)  # Grain in 1 bundle of lower grain (in dou)

# Print results
print(f"上禾每秉實: {b}斗")
print(f"下禾每秉實: {d}斗")


"""


---

### Final Answer:
- 上禾每秉實: **35/26 斗**
- 下禾每秉實: **41/52 斗**
"""


"""
"""
