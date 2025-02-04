"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a frustum-shaped granary (a truncated pyramid). The problem requires calculating the dimensions of the granary (top side, bottom side, and height) and the remaining depth and top side of the granary after some grain has been removed. Below is the Python implementation of the procedure described in the problem.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
方差 = 6  # Difference between top and bottom sides in chi
高多上方 = 9  # Height exceeds the top side by 9 chi
容粟 = 187 + Fraction(2, 10)  # Total volume of grain in shi (1 shi = 10 dou)
已運出 = 50 + Fraction(4, 10)  # Grain already removed in shi
斛法 = 100  # Conversion factor: 1 shi = 100 cubic chi

# 求倉上下方、高
# Step 1: 以斛法乘容粟，為積尺
積尺 = 斛法 * 容粟

# Step 2: 方差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# Step 3: 以乘截高，以減積，余為實
實 = 積尺 - 隅陽冪 * 高多上方

# Step 4: 方差乘截高，加隅陽冪，為方法
方法 = 方差 * 高多上方 + 隅陽冪

# Step 5: 置方差，加截高，為廉法，從
廉法 = 方差 + 高多上方

# Step 6: 開立方除之，即上方
上方 = pow(Fraction(實, 方法), Fraction(1, 3))

# Step 7: 加差，即合所問
下方 = 上方 + 方差
高 = 上方 + 高多上方

# 求余粟高及上方
# Step 1: 以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實
出粟積尺 = 斛法 * 已運出
實 = Fraction(3 * 出粟積尺, 方差**2)

# Step 2: 高乘上方，方差而一，為小高
小高 = Fraction(高 * 上方, 方差)

# Step 3: 令自乘，三之，為方法
方法 = 3 * 小高**2

# Step 4: 三因小高，為廉法，從
廉法 = 3 * 小高

# Step 5: 開立方除之，得取出高
取出高 = pow(Fraction(實, 方法), Fraction(1, 3))

# Step 6: 以減本高，余即殘粟高
殘粟高 = 高 - 取出高

# Step 7: 置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方
余粟上方 = Fraction(取出高 * 方差, 高) + 上方

# Final answers
a = 上方  # 上方
b = 下方  # 下方
c = Fraction(高, 10)  # 高 in 丈 (1 丈 = 10 chi)
d = 余粟上方  # 余粟深上方
#----- content ends here -----


"""


### Explanation of Variables:
- `上方` (`a`): The top side of the granary in chi.
- `下方` (`b`): The bottom side of the granary in chi.
- `高` (`c`): The height of the granary in zhang (1 zhang = 10 chi).
- `余粟上方` (`d`): The remaining depth and top side of the granary after removing some grain, in chi.

### Notes:
1. The solution uses `Fraction` to ensure precise calculations, as ancient Chinese mathematics often involved fractional values.
2. The cubic root (`pow(x, 1/3)`) is used to solve for dimensions, as the problem involves cubic relationships.
3. The units are consistent with the problem statement: `chi` for lengths and `shi` for volumes.
"""


"""
Code error: both arguments should be Rational instances"""
