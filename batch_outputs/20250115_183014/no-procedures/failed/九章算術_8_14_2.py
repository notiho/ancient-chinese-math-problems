"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This is a classic problem involving proportional weights and relationships. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
- There are three types of grain: **甲禾**, **乙禾**, and **丙禾**.
- The total number of bundles (秉) for each type is:
  - 甲禾: 2 bundles
  - 乙禾: 3 bundles
  - 丙禾: 4 bundles
- The weight relationships are:
  - 2 bundles of 甲 weigh the same as 1 bundle of 乙.
  - 3 bundles of 乙 weigh the same as 1 bundle of 丙.
  - 4 bundles of 丙 weigh the same as 1 bundle of 甲.

The goal is to find the weight of **1 bundle** of each type of grain (甲, 乙, 丙) in terms of **石** (a unit of weight).

---

### Solution in Python:


"""


from fractions import Fraction

# Relationships:
# 2 bundles of 甲 = 1 bundle of 乙
# 3 bundles of 乙 = 1 bundle of 丙
# 4 bundles of 丙 = 1 bundle of 甲

# Let the weight of 1 bundle of 甲, 乙, 丙 be x, y, z respectively.
# From the relationships, we can derive:
# 2x = y  --> y = 2x
# 3y = z  --> z = 3y = 3(2x) = 6x
# 4z = x  --> x = 4z = 4(6x) = 24x --> x = 1/24 (normalize x)

# Normalize x to 1/24 of a 石
x = Fraction(1, 24)  # Weight of 1 bundle of 甲禾
y = 2 * x            # Weight of 1 bundle of 乙禾
z = 6 * x            # Weight of 1 bundle of 丙禾

# Total weight for each type of grain:
甲禾_total_weight = 2 * x  # 2 bundles of 甲禾
乙禾_total_weight = 3 * y  # 3 bundles of 乙禾
丙禾_total_weight = 4 * z  # 4 bundles of 丙禾

# Output results:
a = 2  # Number of bundles of 甲禾
b = 甲禾_total_weight
c = 3  # Number of bundles of 乙禾
d = 乙禾_total_weight
e = 4  # Number of bundles of 丙禾
f = 丙禾_total_weight

print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


---

### Explanation of the Output:
1. **甲禾**: Each bundle weighs `1/24` 石, so 2 bundles weigh `2/24 = 1/12` 石.
2. **乙禾**: Each bundle weighs `2/24 = 1/12` 石, so 3 bundles weigh `3/12 = 1/4` 石.
3. **丙禾**: Each bundle weighs `6/24 = 1/4` 石, so 4 bundles weigh `4/4 = 1` 石.

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
