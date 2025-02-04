"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary with a tapering shape. The problem requires calculating the dimensions of the granary (upper circumference, lower circumference, and height) and the remaining grain volume after some has been removed. Below is the Python implementation of the solution based on the procedure described in the problem.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
率徑 = Fraction(1, 3)  # 圓率 = 1/3
上下周差 = Fraction(12)  # 上下周差 = 1丈2尺 = 12尺
高多上周 = Fraction(18)  # 高多上周 = 1丈8尺 = 18尺
容粟 = Fraction(7005, 10)  # 容粟 = 700斛5斗6斗 = 700.56斛
已運出 = Fraction(2664, 10)  # 已運出 = 266石4斗 = 266.4斛

# 求圓囤上下周及高
# Step 1: 以斛法乘容粟，又三十六乘之，三而一，為方亭之積
方亭積 = (斛法 * 容粟 * 36) / 3

# Step 2: 又以周差自乘，三而一，為隅陽冪
隅陽冪 = (上下周差 ** 2) / 3

# Step 3: 以乘截高，以減亭積，余為實
截高 = 高多上周
實 = 方亭積 - (隅陽冪 * 截高)

# Step 4: 又周差乘截高，加隅陽冪，為方法
方法 = (上下周差 * 截高) + 隅陽冪

# Step 5: 又以周差加截高，為廉法，從
廉法 = 上下周差 + 截高

# Step 6: 開立方除之，得上周
上周 = pow(float(實 / 方法), 1/3) * 廉法

# Step 7: 加差，而合所問
下周 = 上周 + 上下周差
高 = 截高

# 求粟去口
# Step 1: 以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實
高冪 = 高 ** 2
實去口 = (斛法 * 已運出 * 36) * (高冪 / 上下周差 ** 2)

# Step 2: 高乘上周，周差而一，為小高
小高 = (高 * 上周) / 上下周差

# Step 3: 令自乘，三之，為方法
方法去口 = 小高 ** 2 * 3

# Step 4: 三因小高，為廉法，從
廉法去口 = 3 * 小高

# Step 5: 開立方除之，即去口
去口 = pow(float(實去口 / 方法去口), 1/3) * 廉法去口

# Step 6: 置去口，以周差乘之，以本高除之，所得加上周，即粟周
粟周 = ((去口 * 上下周差) / 高) + 上周

# Final answers
a = Fraction(上周).limit_denominator(100)  # 上周
b = Fraction(下周).limit_denominator(100)  # 下周
c = Fraction(高).limit_denominator(100)  # 高
d = Fraction(去口).limit_denominator(100)  # 去口
e = Fraction(粟周).limit_denominator(100)  # 粟周

print(f"上周 a = {a} 丈")
print(f"下周 b = {b} 丈")
print(f"高 c = {c} 丈")
print(f"去口 d = {d} 丈")
print(f"粟周 e = {e} 丈")
#----- content ends here -----


"""


### Explanation of Variables:
- `斛法`: The unit conversion factor for volume (2尺5寸 = 2.5尺).
- `率徑`: The circular ratio (π approximated as 3, so 1/3 for the inverse).
- `上下周差`: The difference between the upper and lower circumferences.
- `高多上周`: The height exceeds the upper circumference by this amount.
- `容粟`: The total volume of grain in the granary.
- `已運出`: The amount of grain already removed.

### Outputs:
- `a`: Upper circumference of the granary.
- `b`: Lower circumference of the granary.
- `c`: Height of the granary.
- `d`: Remaining grain height from the top (去口).
- `e`: Circumference of the remaining grain.

This code follows the ancient procedure step by step and uses Python's `Fraction` class to ensure precision in calculations.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 3945/31
Variable 'b' has wrong value. Expected: 3, Actual: 4317/31
Variable 'c' has wrong value. Expected: 18/5, Actual: 18
Variable 'd' has wrong value. Expected: 9/5, Actual: 42539/94
Variable 'e' has wrong value. Expected: 12/5, Actual: 27453/64"""
