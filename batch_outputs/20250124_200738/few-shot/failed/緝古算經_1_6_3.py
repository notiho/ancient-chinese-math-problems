"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a frustum-shaped granary. Let's break it down step by step and translate the procedure into Python code.

### Problem Description:
- A frustum-shaped granary has a smaller square top and a larger square bottom.
- The difference between the side lengths of the top and bottom squares is 6 chi.
- The height of the granary is 9 zhang.
- The granary can hold 187 shi and 2 dou of grain.
- 50 shi and 4 dou of grain have already been removed.
- We need to calculate:
  - The side lengths of the top and bottom squares.
  - The height of the granary.
  - The remaining depth of the grain and the side length of the top square corresponding to the remaining grain.

---

### Procedure:
The procedure involves several steps, including calculating the dimensions of the granary and the remaining grain depth and top square side length. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
方差 = 6  # Difference between the side lengths of the top and bottom squares (chi)
高 = 9 * 10  # Height of the granary in chi (9 zhang = 90 chi)
容粟 = 187 * 10 + 2  # Total volume of the granary in dou (1 shi = 10 dou)
出粟 = 50 * 10 + 4  # Grain already removed in dou
斛法 = 10  # Conversion factor: 1 dou = 10 cubic chi

# Step 1: 求倉上方 (Top square side length)
# 以斛法乘容粟，為積尺
積尺 = 容粟 * 斛法

# 方差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# 以乘截高，以減積，余為實
實 = 積尺 - 隅陽冪 * 高

# 方差乘截高，加隅陽冪，為方法
方法 = 方差 * 高 + 隅陽冪

# 置方差，加截高，為廉法
廉法 = 方差 + 高

# 開立方除之，即上方
上方 = (實 / 方法) ** Fraction(1, 3)

# 下方 = 上方 + 方差
下方 = 上方 + 方差

# Step 2: 求余粟高及上方 (Remaining grain depth and top square side length)
# 以斛法乘出粟，三之
出粟積 = 出粟 * 斛法 * 3

# 以乘高冪，令方差冪而一，為實
實余 = 出粟積 * 高 / 方差

# 高乘上方，方差而一，為小高
小高 = 高 * 上方 / 方差

# 令自乘，三之，為方法
方法余 = 小高**2 * 3

# 三因小高，為廉法
廉法余 = 3 * 小高

# 開立方除之，得取出高
取出高 = (實余 / 方法余) ** Fraction(1, 3)

# 以減本高，余即殘粟高
殘粟高 = 高 - 取出高

# 置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方
余粟上方 = (取出高 * 方差 / 高) + 上方

# Convert results to appropriate units
a = 上方  # Top square side length in chi
b = 下方  # Bottom square side length in chi
c = Fraction(高, 10)  # Height in zhang
d = 殘粟高  # Remaining grain depth in chi
e = 余粟上方  # Remaining grain top square side length in chi

# Final answers
print(f"上方 a = {float(a):.2f} 尺")
print(f"下方 b = {float(b):.2f} 尺")
print(f"高 c = {float(c):.2f} 丈")
print(f"余粟深 d = {float(d):.2f} 尺")
print(f"余粟上方 e = {float(e):.2f} 尺")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1: Calculating the top and bottom square side lengths (`上方` and `下方`)**:
   - Use the given formula to calculate the top square side length (`上方`).
   - Add the difference (`方差`) to get the bottom square side length (`下方`).

2. **Step 2: Calculating the remaining grain depth and top square side length**:
   - Use the volume of the removed grain to calculate the remaining grain depth (`余粟深`).
   - Use the remaining grain depth to calculate the corresponding top square side length (`余粟上方`).

3. **Units**:
   - All calculations are performed in chi (尺) and zhang (丈) as appropriate.

4. **Output**:
   - The results are printed in the required units with two decimal places for clarity.

---

### Final Output:
The program will output:
- The side length of the top square (`a`).
- The side length of the bottom square (`b`).
- The height of the granary (`c`).
- The remaining grain depth and top square side length (`d` and `e`).
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 3.1733635889665
Variable 'b' has wrong value. Expected: 9, Actual: 9.1733635889665
Variable 'c' has wrong value. Expected: 6/5, Actual: 9
Variable 'd' has wrong value. Expected: 6, Actual: 86.78066229399595"""
