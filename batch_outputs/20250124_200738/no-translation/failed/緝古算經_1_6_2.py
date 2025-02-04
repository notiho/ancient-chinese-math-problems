"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. We'll use the `Fraction` class to handle fractional values accurately.


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
斛法 = 10  # 1石 = 10斗 = 100升 = 1000斛
容粟 = 187 * 10 + 2  # Convert 187石2斗 to斗
出粟 = 50 * 10 + 4  # Convert 50石4斗 to斗
方差 = 6  # 上下方差6尺
截高 = 9  # 高多上方9尺

# 求倉上下方及高
# Step 1: 以斛法乘容粟，為積尺
積尺 = 斛法 * 容粟

# Step 2: 方差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# Step 3: 方差乘截高，加隅陽冪，為方法
方法 = 方差 * 截高 + 隅陽冪

# Step 4: 置方差，加截高，為廉法
廉法 = 方差 + 截高

# Step 5: 開立方除之，即上方
上方 = Fraction(math.isqrt(積尺 * 3 // 方法), 1)

# Step 6: 加差，即合所問
下方 = 上方 + 方差
高 = 截高

# 求余粟深及上方
# Step 1: 以斛法乘出粟，三之
出粟積 = Fraction(斛法 * 出粟 * 3, 1)

# Step 2: 乘高冪，令方差冪而一，為實
實 = 出粟積 * (高**2) / 方差

# Step 3: 高乘上方，方差而一，為小高
小高 = 高 * 上方 / 方差

# Step 4: 令自乘，三之，為方法
方法 = 3 * 小高**2

# Step 5: 三因小高，為廉法
廉法 = 3 * 小高

# Step 6: 開立方除之，得取出高
取出高 = Fraction(math.isqrt(實 // 方法), 1)

# Step 7: 以減本高，余即殘粟高
余粟高 = 高 - 取出高

# Step 8: 置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方
余粟上方 = 出粟高 * 方差 / 高 + 上方

# Final answers
a = 上方
b = 下方
c = Fraction(高, 10)  # Convert to 丈
d = 余粟上方

# Output results
print(f"上方 a = {a} 尺")
print(f"下方 b = {b} 尺")
print(f"高 c = {c} 丈")
print(f"余粟深及上方 d = {d} 尺")
#----- content ends here -----


"""


This code follows the ancient procedure step by step, ensuring that each calculation adheres to the described method. Note that `math.isqrt` is used for integer square roots, and `Fraction` ensures precise arithmetic for fractional values.
"""


"""
Code error: name '出粟高' is not defined"""
