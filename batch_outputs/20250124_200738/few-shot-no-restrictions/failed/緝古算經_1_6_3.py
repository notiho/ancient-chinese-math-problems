"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
This is a complex ancient Chinese math problem involving a frustum-shaped granary (a truncated pyramid). The problem asks for the dimensions of the granary (top side, bottom side, height) and the remaining depth and top side area of the granary after some grain has been removed. Below is the Python implementation of the solution.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
斛法 = 10  # 1石 = 10斗
容粟 = 187 * 斛法 + 2  # Total grain volume in dou
出粟 = 50 * 斛法 + 4  # Grain removed in dou
方差 = 6  # Difference between top and bottom sides in chi
截高 = 9  # Height difference between the top and bottom in chi

# 求倉上下方及高
# Step 1: Calculate the total volume in cubic chi
積尺 = 容粟 * 斛法

# Step 2: Calculate 隅陽冪 (corner volume adjustment)
隅陽冪 = Fraction(方差**2, 3)

# Step 3: Calculate the actual volume (實)
實 = 積尺 - 隅陽冪 * 截高

# Step 4: Calculate 方法 (method divisor)
方法 = 方差 * 截高 + 隅陽冪

# Step 5: Calculate 廉法 (linear divisor)
廉法 = 方差 + 截高

# Step 6: Solve for the top side (上方)
上方 = pow(Fraction(實, 方法), 1/3)

# Step 7: Solve for the bottom side (下方)
下方 = 上方 + 方差

# Step 8: Solve for the height (高)
高 = 截高 + 上方

# 求余粟深及上方
# Step 1: Calculate the volume of the removed grain in cubic chi
出粟積 = 出粟 * 斛法

# Step 2: Calculate the actual height of the removed grain
實 = 出粟積 * 3 / (隅陽冪 + 方差 * 截高)
小高 = pow(Fraction(實, 方法), 1/3)

# Step 3: Calculate the remaining height of the grain
余粟高 = 高 - 小高

# Step 4: Calculate the remaining top side of the grain
余粟上方 = 上方 + 方差 * 小高 / 高

# Convert height to zhang (1丈 = 10尺)
高丈 = 高 / 10

# Final results
a = 上方
b = 下方
c = 高丈
d = 余粟高
e = 余粟上方

print(f"上方: {a} 尺")
print(f"下方: {b} 尺")
print(f"高: {c} 丈")
print(f"余粟深: {d} 尺")
print(f"余粟上方: {e} 尺")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initial Calculations**:
   - Convert the total grain volume and removed grain volume into cubic chi using the conversion factor `斛法` (1石 = 10斗).
   - Use the given formulas to calculate the total volume (`積尺`), corner adjustment (`隅陽冪`), and the actual volume (`實`).

2. **Granary Dimensions**:
   - Solve for the top side (`上方`), bottom side (`下方`), and height (`高`) using the formulas provided in the problem.

3. **Remaining Grain Depth and Top Side**:
   - Calculate the height of the removed grain (`小高`) and subtract it from the total height to get the remaining depth (`余粟高`).
   - Use the remaining height to calculate the new top side area (`余粟上方`).

4. **Output**:
   - The results are printed in chi for the top side, bottom side, and remaining top side, and in zhang for the height.

This code follows the ancient Chinese mathematical procedure step by step and provides the required answers.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 6.557672186169711
Variable 'b' has wrong value. Expected: 9, Actual: 12.557672186169711
Variable 'c' has wrong value. Expected: 6/5, Actual: 1.555767218616971
Variable 'd' has wrong value. Expected: 6, Actual: 14.043571905261688"""
