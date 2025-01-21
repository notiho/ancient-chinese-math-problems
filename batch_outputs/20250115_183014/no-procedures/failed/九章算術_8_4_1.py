"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
This problem involves determining the amount of grain (實) in one bundle (秉) of "upper millet" (上禾) and "lower millet" (下禾) based on the given relationships.

### Problem Breakdown:
1. **Given Relationships:**
   - 6 bundles of upper millet lose 1 dou 8 sheng (18 sheng) and are equivalent to 10 bundles of lower millet.
   - 15 bundles of lower millet lose 5 sheng and are equivalent to 5 bundles of upper millet.

2. **Goal:**
   - Find the grain (實) in one bundle of upper millet and one bundle of lower millet.

---

### Solution in Python:


"""


from fractions import Fraction

# Known values
上禾_損實 = 18  # 1斗8升 = 18升
下禾_損實 = 5   # 5升

# Relationships
# 6 bundles of upper millet = 10 bundles of lower millet
# 15 bundles of lower millet = 5 bundles of upper millet

# Let:
# a = 实 in one bundle of upper millet (in 升)
# b = 实 in one bundle of lower millet (in 升)

# Equation 1: 6 * a - 10 * b = 18
# Equation 2: 15 * b - 5 * a = 5

# Solve the system of equations
# From Equation 1: a = (10 * b + 18) / 6
# Substitute into Equation 2:
# 15 * b - 5 * ((10 * b + 18) / 6) = 5
# Simplify:
# 15 * b - (50 * b + 90) / 6 = 5
# Multiply through by 6 to eliminate the fraction:
# 90 * b - 50 * b - 90 = 30
# 40 * b = 120
# b = 3

# Substitute b = 3 into Equation 1:
# 6 * a - 10 * 3 = 18
# 6 * a = 48
# a = 8

# Results
a = Fraction(8)  # 实 in one bundle of upper millet
b = Fraction(3)  # 实 in one bundle of lower millet

# Output
print(f"上禾 1秉 實 {a}升")
print(f"下禾 1秉 實 {b}升")


"""


---

### Explanation of the Results:
- **上禾 (Upper Millet):** Each bundle contains `8升` of grain.
- **下禾 (Lower Millet):** Each bundle contains `3升` of grain.

This solution uses basic algebra to solve the system of equations derived from the problem's relationships.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'b' has wrong value. Expected: 8, Actual: 3
Missing variable in output: 'c'
Missing variable in output: 'd'"""
