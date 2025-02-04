"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a frustum-shaped granary. Let's break it down step by step and translate the procedure into Python code.

### Problem Description:
- The granary is a frustum of a pyramid.
- The difference between the upper and lower square sides is 6 chi.
- The height of the granary is 9 zhang.
- The granary holds 187 shi and 2 dou of grain.
- 50 shi and 4 dou of grain have been removed.
- We need to calculate:
  - The dimensions of the granary: upper side, lower side, and height.
  - The remaining grain's depth and the upper side of the remaining grain.

---

### Procedure:
1. **Find the dimensions of the granary (upper side, lower side, and height):**
   - Use the given volume and dimensions to calculate the upper side of the granary.
   - From the upper side, calculate the lower side and height.

2. **Find the depth and upper side of the remaining grain:**
   - Use the volume of the removed grain to calculate the depth of the remaining grain.
   - Use the depth to calculate the upper side of the remaining grain.

---

### Python Code:


"""


from fractions import Fraction
from math import pow

# Given values
方差 = 6  # Difference between upper and lower sides (chi)
高 = 9 * 10  # Height in chi (9 zhang = 90 chi)
容粟 = 187 * 10 + 2  # Total volume in dou (1 shi = 10 dou)
出粟 = 50 * 10 + 4  # Removed volume in dou
斛法 = 10  # Conversion factor: 1 dou = 10 cubic chi

# Step 1: Calculate the dimensions of the granary
# 以斛法乘容粟，為積尺
積尺 = 斛法 * 容粟

# 方差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# 以乘截高，以減積，余為實
實 = 積尺 - 隅陽冪 * 高

# 方差乘截高，加隅陽冪，為方法
方法 = 方差 * 高 + 隅陽冪

# 置方差，加截高，為廉法
廉法 = 方差 + 高

# 開立方除之，即上方
上方 = pow(Fraction(實, 方法), Fraction(1, 3))

# 加差，即下方
下方 = 上方 + 方差

# Step 2: Calculate the depth and upper side of the remaining grain
# 以斛法乘出粟，三之
出積 = 斛法 * 出粟 * 3

# 以乘高冪，令方差冪而一，為實
實2 = 出積 * 高**2 / 方差**2

# 高乘上方，方差而一，為小高
小高 = 高 * 上方 / 方差

# 令自乘，三之，為方法
方法2 = 3 * 小高**2

# 三因小高，為廉法
廉法2 = 3 * 小高

# 開立方除之，得取出高
取出高 = pow(Fraction(實2, 方法2), Fraction(1, 3))

# 以減本高，余即殘粟高
殘粟高 = 高 - 取出高

# 置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方
余粟上方 = 出粟 * 方差 / 高 + 上方

# Final answers
a = 上方  # Upper side of the granary
b = 下方  # Lower side of the granary
c = Fraction(高, 10)  # Height in zhang
d = 殘粟高  # Depth of remaining grain
e = 余粟上方  # Upper side of remaining grain

# Output results
print(f"上方: {a} 尺")
print(f"下方: {b} 尺")
print(f"高: {c} 丈")
print(f"余粟深: {d} 尺")
print(f"余粟上方: {e} 尺")


"""


---

### Explanation of the Code:
1. **Step 1: Calculate Granary Dimensions**
   - The procedure involves calculating the upper side (`上方`) by solving a cubic equation derived from the volume formula of a frustum.
   - The lower side (`下方`) is obtained by adding the difference (`方差`) to the upper side.
   - The height is given directly in the problem.

2. **Step 2: Calculate Remaining Grain Depth and Upper Side**
   - The depth of the remaining grain is calculated using the volume of the removed grain and the geometry of the frustum.
   - The upper side of the remaining grain is adjusted based on the depth and the geometry.

---

### Final Output:
The program calculates:
- `a`: Upper side of the granary in chi.
- `b`: Lower side of the granary in chi.
- `c`: Height of the granary in zhang.
- `d`: Depth of the remaining grain in chi.
- `e`: Upper side of the remaining grain in chi.
"""


"""
Code error: both arguments should be Rational instances"""
