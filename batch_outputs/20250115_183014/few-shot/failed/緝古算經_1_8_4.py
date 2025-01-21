"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex problem involving a circular truncated cone (a frustum) with specific dimensions and calculations for its geometry and the remaining volume of grain after some has been removed. Below is the Python implementation of the problem, following the ancient Chinese mathematical procedure step by step.


"""


from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
率徑 = Fraction(1, 3)  # 圓率 = 1/3
上下周差 = Fraction(12)  # 上下周差 = 1丈2尺 = 12尺
高多上周 = Fraction(18)  # 高多上周 = 1丈8尺 = 18尺
容粟 = Fraction(7005, 10)  # 容粟 = 700斛5斗6升 = 700.5斛
已運出 = Fraction(2664, 10)  # 已運出 = 266石4斗 = 266.4斛

# 求圓囤上下周及高
# Step 1: 以斛法乘容粟，又三十六乘之，三而一，為方亭之積
方亭積 = (斛法 * 容粟 * 36) / 3

# Step 2: 又以周差自乘，三而一，為隅陽冪
隅陽冪 = (上下周差 ** 2) / 3

# Step 3: 以乘截高，以減亭積，余為實
截高 = 高多上周 - 上下周差
實 = 方亭積 - (隅陽冪 * 截高)

# Step 4: 又周差乘截高，加隅陽冪，為方法
方法 = (上下周差 * 截高) + 隅陽冪

# Step 5: 又以周差加截高，為廉法，從
廉法 = 上下周差 + 截高

# Step 6: 開立方除之，得上周
上周 = pow(float(實 / 方法), 1/3) * 廉法

# Step 7: 加差，而合所問
上周 = Fraction(round(上周, 6))  # Convert to Fraction for precision
下周 = 上周 + 上下周差
高 = 高多上周 - 上周

# 求粟去口
# Step 1: 以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實
高冪 = 高 ** 2
實去口 = (斛法 * 已運出 * 36) * (高冪 / (上下周差 ** 2))

# Step 2: 高乘上周，周差而一，為小高
小高 = (高 * 上周) / 上下周差

# Step 3: 令自乘，三之，為方法
方法去口 = (小高 ** 2) * 3

# Step 4: 三因小高，為廉法，從
廉法去口 = 3 * 小高

# Step 5: 開立方除之，即去口
去口 = pow(float(實去口 / 方法去口), 1/3) * 廉法去口
去口 = Fraction(round(去口, 6))  # Convert to Fraction for precision

# Step 6: 置去口，以周差乘之，以本高除之，所得加上周，即粟周
粟周 = ((去口 * 上下周差) / 高) + 上周

# Final answers
a = 上周  # 上周
b = 下周  # 下周
c = 高  # 高
d = 去口  # 去口
e = 粟周  # 粟周

# Output the results
print(f"上周 a = {a} 丈")
print(f"下周 b = {b} 丈")
print(f"高 c = {c} 丈")
print(f"去口 d = {d} 丈")
print(f"粟周 e = {e} 丈")


"""


### Explanation of Variables:
- `斛法`: The unit conversion factor for volume (2尺5寸 = 2.5尺).
- `率徑`: The ratio of the circumference to the diameter (π approximated as 3).
- `上下周差`: The difference between the upper and lower circumferences (1丈2尺 = 12尺).
- `高多上周`: The height exceeds the upper circumference by 1丈8尺 = 18尺.
- `容粟`: The total volume of grain in the frustum (700斛5斗6升 = 700.5斛).
- `已運出`: The volume of grain already removed (266石4斗 = 266.4斛).
- `上周`, `下周`, `高`: The upper circumference, lower circumference, and height of the frustum.
- `去口`: The remaining height of the grain from the top.
- `粟周`: The circumference of the grain surface.

This code follows the ancient procedure step by step and calculates the required values.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 7054031162021845/70368744177664
Variable 'b' has wrong value. Expected: 3, Actual: 7898456092153813/70368744177664
Variable 'c' has wrong value. Expected: 18/5, Actual: -5787393766823893/70368744177664
Variable 'd' has wrong value. Expected: 9/5, Actual: -8398609866676373/4398046511104
Variable 'e' has wrong value. Expected: 12/5, Actual: 154296384776048382206020935415609/407251631433037745789392125952"""
