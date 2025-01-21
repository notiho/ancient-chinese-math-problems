"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This is a classic system of equations problem from ancient Chinese mathematics. Let's break it down and solve it step by step.

### Problem Breakdown:
1. There are two types of grain: **upper grain (上禾)** and **lower grain (下禾)**.
2. Seven bundles (秉) of upper grain lose 1 dou (斗) of grain, but when 2 bundles of lower grain are added, the total becomes 10 dou.
3. Eight bundles of lower grain gain 1 dou of grain, but when 2 bundles of upper grain are added, the total becomes 10 dou.
4. The question asks for the amount of grain (斗) per bundle (秉) for both the upper grain and the lower grain.

We need to solve for:
- `a`: the number of bundles of upper grain (上禾)
- `b`: the amount of grain per bundle of upper grain (斗)
- `c`: the number of bundles of lower grain (下禾)
- `d`: the amount of grain per bundle of lower grain (斗)

---

### Solution in Python:


"""


from fractions import Fraction

# Let x = the amount of grain per bundle of upper grain (斗)
# Let y = the amount of grain per bundle of lower grain (斗)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Solve for x and y
# Rearrange Equation 1: 7x + 2y = 11
# Rearrange Equation 2: 2x + 8y = 9

# Solve the system of equations using substitution or elimination
# Multiply Equation 1 by 4 to align coefficients of y:
# 28x + 8y = 44
# 2x + 8y = 9

# Subtract the second equation from the first:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)

# Substitute x back into Equation 1: 7x + 2y = 11
# 7(35/26) + 2y = 11
# 245/26 + 2y = 11
# 2y = 11 - 245/26
# 2y = (286/26) - (245/26)
# 2y = 41/26
y = Fraction(41, 52)

# Results
a = 7  # Number of bundles of upper grain
b = x  # Grain per bundle of upper grain
c = 8  # Number of bundles of lower grain
d = y  # Grain per bundle of lower grain

# Print results
print(f"上禾 {a}秉 實 {b}斗")
print(f"下禾 {c}秉 實 {d}斗")


"""


---

### Final Answer:
- 上禾 7秉 實 \( \frac{35}{26} \)斗
- 下禾 8秉 實 \( \frac{41}{52} \)斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
