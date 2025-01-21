"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This is a classic problem involving proportional relationships between weights. Let's break it down step by step and solve it.

---

### Problem:
- There are three types of grain: **甲禾**, **乙禾**, and **丙禾**.
- The number of bundles (秉) for each type is:
  - 甲禾: 2 bundles
  - 乙禾: 3 bundles
  - 丙禾: 4 bundles
- The weight relationships are:
  - 2 bundles of 甲 weigh the same as 1 bundle of 乙.
  - 3 bundles of 乙 weigh the same as 1 bundle of 丙.
  - 4 bundles of 丙 weigh the same as 1 bundle of 甲.
- Question: What is the weight of **1 bundle** of each type of grain (甲, 乙, 丙) in terms of 石 (a unit of weight)?

---

### Solution:

We will use the relationships to calculate the weight of 1 bundle of each type of grain.

1. Let the weight of **1 bundle of 丙禾** be `x` 石.
   - Then, the weight of **1 bundle of 乙禾** is `3x` (since 3 bundles of 乙 weigh the same as 1 bundle of 丙).
   - The weight of **1 bundle of 甲禾** is `6x` (since 2 bundles of 甲 weigh the same as 1 bundle of 乙, and 1 bundle of 乙 is `3x`).

2. Now, we know the weight of 1 bundle of each type:
   - 甲禾: `6x` 石
   - 乙禾: `3x` 石
   - 丙禾: `x` 石

3. To find the total weight of all bundles:
   - Total weight of 甲禾 (2 bundles): `2 * 6x = 12x` 石
   - Total weight of 乙禾 (3 bundles): `3 * 3x = 9x` 石
   - Total weight of 丙禾 (4 bundles): `4 * x = 4x` 石

4. The total weight of all bundles is given to exceed 1 石. To normalize, we can express the weights in terms of their ratios.

---

### Final Answer:
- **甲禾**: 1 bundle weighs `6x` 石, and 2 bundles weigh `12x` 石.
- **乙禾**: 1 bundle weighs `3x` 石, and 3 bundles weigh `9x` 石.
- **丙禾**: 1 bundle weighs `x` 石, and 4 bundles weigh `4x` 石.

Let’s write this in Python to calculate the normalized weights.

---


"""


from fractions import Fraction

# Let the weight of 1 bundle of 丙禾 be x
x = Fraction(1)  # Assume x = 1 for simplicity

# Weights of 1 bundle of each type
weight_丙 = x
weight_乙 = 3 * x
weight_甲 = 6 * x

# Total weights for all bundles
total_weight_甲 = 2 * weight_甲
total_weight_乙 = 3 * weight_乙
total_weight_丙 = 4 * weight_丙

# Output results
a = 2  # Number of bundles of 甲禾
b = total_weight_甲  # Total weight of 甲禾

c = 3  # Number of bundles of 乙禾
d = total_weight_乙  # Total weight of 乙禾

e = 4  # Number of bundles of 丙禾
f = total_weight_丙  # Total weight of 丙禾

print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


---

### Output:
```
甲禾 2秉 重 12石
乙禾 3秉 重 9石
丙禾 4秉 重 4石
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 12
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 9
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 4"""
