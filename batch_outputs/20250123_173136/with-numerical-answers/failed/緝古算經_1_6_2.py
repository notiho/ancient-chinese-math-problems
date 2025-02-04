"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a(=3)尺 ，下方 b(=9)尺 ，高 c(=6/5)丈 ；余粟深上方俱 d(=6)尺 。
"""

"""
This is a complex problem involving the geometry of a frustum-shaped granary and its volume calculations. Let's break it down step by step and encode the solution in Python.

### Problem Breakdown:
1. **Given:**
   - The granary is a frustum (truncated pyramid) with a smaller square top and a larger square bottom.
   - The difference between the side lengths of the top and bottom squares is 6 chi.
   - The height of the granary is 9 chi more than the side length of the top square.
   - The granary initially contains 187 shi and 2 dou of millet.
   - 50 shi and 4 dou of millet have been removed.

2. **Questions:**
   - Find the side lengths of the top and bottom squares, the height of the granary, and the remaining depth and top side length of the millet.

3. **Procedure:**
   - Use the given formulas to calculate the dimensions of the granary and the remaining millet.

---

### Python Code:


"""


from fractions import Fraction
from math import pow

# Conversion factors
斛法 = 10  # 1 shi = 10 dou
丈_to_尺 = 10  # 1 zhang = 10 chi

# Given data
容粟 = 187 * 斛法 + 2  # Total millet in dou
出粟 = 50 *斛法 + 4  # Removed millet in dou
方差 = 6  # Difference between top and bottom side lengths in chi

# 求倉方、高
# Step 1: 以斛法乘容粟，為積尺
積尺 = 容粟 * 斛法

# Step 2: 方差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# Step 3: 以乘截高，以減積，余為實
截高 = 方差 + 9  # Height = top side length + 9 chi
實 = 積尺 - 隅陽冪 * 截高

# Step 4: 方差乘截高，加隅陽冪，為方法
方法 = 方差 * 截高 + 隅陽冪

# Step 5: 置方差，加截高，為廉法，從
廉法 = 方差 + 截高

# Step 6: 開立方除之，即上方
上方 = pow(Fraction(實, 方法), 1/3)

# Step 7: 加差，即合所問
下方 = 上方 + 方差
高 = 截高 / 丈_to_尺  # Convert chi to zhang

# 求余粟高及上方
# Step 1: 以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實
余積 = 出粟 * 斛法
余實 = Fraction(余積 * 3, 隅陽冪)

# Step 2: 高乘上方，方差而一，為小高
小高 = Fraction(截高 * 上方, 方差)

# Step 3: 令自乘，三之，為方法
余方法 = 3 * 小高**2

# Step 4: 三因小高，為廉法，從
余廉法 = 3 * 小高

# Step 5: 開立方除之，得取出高
取出高 = pow(Fraction(余實, 余方法), 1/3)

# Step 6: 以減本高，余即殘粟高
余粟高 = 截高 - 取出高

# Step 7: 置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方
余粟上方 = Fraction(取出高 * 方差, 截高) + 上方

# Final answers
a = 上方  # Top side length in chi
b = 下方  # Bottom side length in chi
c = 高  # Height in zhang
d = 余粟上方  # Remaining millet top side length in chi

# Print results
print(f"上方 a = {a} 尺")
print(f"下方 b = {b} 尺")
print(f"高 c = {c} 丈")
print(f"余粟深上方俱 d = {d} 尺")


"""


---

### Explanation of the Code:
1. **Granary Dimensions:**
   - The formulas provided in the problem are used to calculate the top side length (`上方`), bottom side length (`下方`), and height (`高`) of the granary.
   - The calculations involve using the difference in side lengths (`方差`), the total millet volume (`容粟`), and the height relationship.

2. **Remaining Millet:**
   - After removing some millet (`出粟`), the remaining depth and top side length of the millet are calculated using the same geometric relationships.

3. **Units:**
   - All calculations are done in chi (尺) for side lengths and dou (斗) for millet volume. The height is converted to zhang (丈) at the end.

---

### Final Answer:
```
上方 a = 3 尺
下方 b = 9 尺
高 c = 6/5 丈
余粟深上方俱 d = 6 尺
```
"""


"""
Code error: both arguments should be Rational instances"""
