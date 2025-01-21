"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This is a classic problem involving proportional relationships between weights. Let's solve it step by step.

### Problem Breakdown:
- There are three types of grain: **甲**, **乙**, and **丙**.
- The total number of bundles (秉) is:
  - 甲: 2 bundles
  - 乙: 3 bundles
  - 丙: 4 bundles
- Weight relationships:
  - 甲's 2 bundles weigh the same as 1 bundle of 乙.
  - 乙's 3 bundles weigh the same as 1 bundle of 丙.
  - 丙's 4 bundles weigh the same as 1 bundle of 甲.

We need to calculate the weight of **1 bundle** of each type of grain (甲, 乙, 丙) in terms of **石**.

---

### Solution in Python:


"""


from fractions import Fraction

# Define the relationships:
# 2 bundles of 甲 = 1 bundle of 乙
# 3 bundles of 乙 = 1 bundle of 丙
# 4 bundles of 丙 = 1 bundle of 甲

# Let the weight of 1 bundle of 甲 be x 石
# Then:
甲_weight = Fraction(1, 1)  # Let 甲's 1 bundle weight be the base unit (x = 1 石)

# From the relationships:
乙_weight = 2 * 甲_weight  # 2 bundles of 甲 = 1 bundle of 乙, so 1 bundle of 乙 = 2x
丙_weight = 3 * 乙_weight  # 3 bundles of 乙 = 1 bundle of 丙, so 1 bundle of 丙 = 6x

# Now calculate the total weight for each type of grain:
甲_total_weight = 2 * 甲_weight  # 2 bundles of 甲
乙_total_weight = 3 * 乙_weight  # 3 bundles of 乙
丙_total_weight = 4 * 丙_weight  # 4 bundles of 丙

# Output results:
a, b = 2, 甲_total_weight
c, d = 3, 乙_total_weight
e, f = 4, 丙_total_weight

# Print results
print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


---

### Explanation of Results:
1. **甲禾**: Each bundle weighs `1` 石, so 2 bundles weigh `2` 石.
2. **乙禾**: Each bundle weighs `2` 石, so 3 bundles weigh `6` 石.
3. **丙禾**: Each bundle weighs `6` 石, so 4 bundles weigh `24` 石.

Thus:
- 甲禾 2秉 重 2石
- 乙禾 3秉 重 6石
- 丙禾 4秉 重 24石
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 2
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 6
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 24"""
