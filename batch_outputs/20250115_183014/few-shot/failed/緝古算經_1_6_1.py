"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a frustum-shaped grain storage (亭倉). The problem asks for the dimensions of the storage (top side, bottom side, height) and the remaining grain depth and top side after some grain has been removed. Below is the solution encoded in Python, following the procedure ("術") step by step.


"""


from fractions import Fraction
from math import pow

# Given values
方差 = 6  # Difference between the top and bottom sides (in chi)
高多上方 = 9  # Height is 9 chi more than the top side
容粟 = 187 + Fraction(2, 10)  # Total grain volume in 石 (187石2斗)
已運出粟 = 50 + Fraction(4, 10)  # Grain already removed in 石 (50石4斗)
斛法 = 10  # Conversion factor: 1石 = 10 cubic chi

# Step 1: 求倉上下方、高
# 以斛法乘容粟，為積尺
積尺 = 容粟 * 斛法

# 方差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# 以乘截高，以減積，余為實
截高 = 高多上方
實 = 積尺 - 隅陽冪 * 截高

# 方差乘截高，加隅陽冪，為方法
方法 = 方差 * 截高 + 隅陽冪

# 置方差，加截高，為廉法，從
廉法 = 方差 + 截高

# 開立方除之，即上方
上方 = pow(Fraction(實, 方法), Fraction(1, 3))

# 加差，即合所問
下方 = 上方 + 方差
高 = 上方 + 高多上方

# Step 2: 求余粟高及上方
# 以斛法乘出粟，三之
出粟積 = 已運出粟 * 斛法 * 3

# 以乘高冪，令方差冪而一，為實
高冪 = 高**2
方差冪 = 方差**2
實 = Fraction(出粟積, 方差冪)

# 高乘上方，方差而一，為小高
小高 = Fraction(高 * 上方, 方差)

# 令自乘，三之，為方法
方法 = 3 * 小高**2

# 三因小高，為廉法，從
廉法 = 3 * 小高

# 開立方除之，得取出高
取出高 = pow(Fraction(實, 方法), Fraction(1, 3))

# 以減本高，余即殘粟高
殘粟高 = 高 - 取出高

# 置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方
余粟上方 = Fraction(取出高 * 方差, 高) + 上方

# Final answers
a = 上方  # 上方 in chi
b = 下方  # 下方 in chi
c = Fraction(高, 10)  # 高 in zhang (1 zhang = 10 chi)
d = 余粟上方  # Remaining grain depth and top side in chi

print(f"上方 a = {a} 尺")
print(f"下方 b = {b} 尺")
print(f"高 c = {c} 丈")
print(f"余粟深上方俱 d = {d} 尺")


"""


### Explanation of the Code:
1. **求倉上下方、高**:
   - The procedure calculates the top side (`上方`), bottom side (`下方`), and height (`高`) of the frustum-shaped storage based on the total grain volume (`容粟`), the difference between the top and bottom sides (`方差`), and the height difference (`高多上方`).

2. **求余粟高及上方**:
   - After some grain is removed (`已運出粟`), the remaining grain depth (`余粟深`) and the new top side (`余粟上方`) are calculated.

3. **Units**:
   - `chi` (尺) is used for lengths, and `zhang` (丈) is used for height (1丈 = 10尺).
   - `shi` (石) and `dou` (斗) are used for volume (1石 = 10斗).

### Final Outputs:
- `a`: Top side of the storage in chi.
- `b`: Bottom side of the storage in chi.
- `c`: Height of the storage in zhang.
- `d`: Remaining grain depth and top side in chi.
"""


"""
Code error: both arguments should be Rational instances"""
