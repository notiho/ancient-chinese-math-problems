"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This problem involves solving the weights of three types of grain bundles (甲, 乙, 丙) based on their relative weights and quantities. Let's break it down step by step.

---

### Problem Explanation:
- 甲禾 has 2 bundles (秉), 乙禾 has 3 bundles, 丙禾 has 4 bundles.
- The weight relationships are:
  - 甲's 2 bundles weigh the same as 乙's 1 bundle.
  - 乙's 3 bundles weigh the same as 丙's 1 bundle.
  - 丙's 4 bundles weigh the same as 甲's 1 bundle.

We need to calculate the weight of **one bundle** of each type (甲, 乙, 丙) and the total weight of their respective bundles.

---

### Solution in Python:


"""


from fractions import Fraction

# Let the weight of one bundle of 甲, 乙, 丙 be x, y, z respectively.
# From the problem, we know:
# 1. 2x = y  (甲's 2 bundles weigh the same as 乙's 1 bundle)
# 2. 3y = z  (乙's 3 bundles weigh the same as 丙's 1 bundle)
# 3. 4z = x  (丙's 4 bundles weigh the same as 甲's 1 bundle)

# Solve for x, y, z in terms of a common unit:
# From 1: y = 2x
# From 2: z = 3y = 3(2x) = 6x
# From 3: x = 4z = 4(6x) = 24x
# This implies x = 1/24 (in terms of a common unit).

# Assign weights:
x = Fraction(1, 24)  # Weight of one bundle of 甲
y = 2 * x            # Weight of one bundle of 乙
z = 6 * x            # Weight of one bundle of 丙

# Calculate total weights for each type:
甲_total_weight = 2 * x  # 2 bundles of 甲
乙_total_weight = 3 * y  # 3 bundles of 乙
丙_total_weight = 4 * z  # 4 bundles of 丙

# Output results:
a = 2  # Number of bundles of 甲
b = 甲_total_weight  # Total weight of 甲禾

c = 3  # Number of bundles of 乙
d = 乙_total_weight  # Total weight of 乙禾

e = 4  # Number of bundles of 丙
f = 丙_total_weight  # Total weight of 丙禾

# Print results:
print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


---

### Explanation of Results:
1. The weight of one bundle of 甲 (x) is `1/24` shi.
2. The weight of one bundle of 乙 (y) is `2/24 = 1/12` shi.
3. The weight of one bundle of 丙 (z) is `6/24 = 1/4` shi.

The total weights are:
- 甲禾: 2 bundles × `1/24` = `2/24 = 1/12` shi.
- 乙禾: 3 bundles × `1/12` = `3/12 = 1/4` shi.
- 丙禾: 4 bundles × `1/4` = `4/4 = 1` shi.

---

### Final Answer:
```
甲禾 2秉 重 1/12石
乙禾 3秉 重 1/4石
丙禾 4秉 重 1石
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 1/12
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 1/4
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 1"""
