"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary with a frustum-like shape. The solution involves multiple steps, including calculating the upper and lower circumferences, height, remaining grain volume, and the grain's surface circumference after some grain has been removed. Below is the Python implementation of the solution based on the provided procedure.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
率徑 = Fraction(1, 3)    # 圓率 = 1/3
上下周差 = 12           # 上下周差 = 1丈2尺 = 12尺
高多上周 = 18           # 高多上周 = 1丈8尺 = 18尺
容粟 = 756              # 容粟 = 700斛6斗 = 756斗
已運出 = 2664           # 已運出 = 266石4斗 = 2664斗

# 求圓囤上下周及高
# Step 1: 以斛法乘容粟，又三十六乘之，三而一，為方亭之積
方亭積 = (斛法 * 容粟 * 36) / 3

# Step 2: 又以周差自乘，三而一，為隅陽冪
隅陽冪 = (上下周差 ** 2) / 3

# Step 3: 以乘截高，以減亭積，余為實
截高 = 高多上周 + 上下周差
實 = 方亭積 - 隅陽冪 * 截高

# Step 4: 又周差乘截高，加隅陽冪，為方法
方法 = (上下周差 * 截高) + 隅陽冪

# Step 5: 又以周差加截高，為廉法
廉法 = 上下周差 + 截高

# Step 6: 開立方除之，得上周
上周 = pow(實 / 方法, Fraction(1, 3)) / 廉法

# Step 7: 加差，而合所問
下周 = 上周 + 上下周差
高 = 高多上周 + 上周

# 求粟去口
# Step 1: 以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實
高冪 = 高 ** 2
周差冪 = 上下周差 ** 2
實_去口 = (斛法 * 已運出 * 36) * (高冪 / 周差冪)

# Step 2: 高乘上周，周差而一，為小高
小高 = (高 * 上周) / 上下周差

# Step 3: 令自乘，三之，為方法
方法_去口 = (小高 ** 2) * 3

# Step 4: 三因小高，為廉法
廉法_去口 = 3 * 小高

# Step 5: 開立方除之，即去口
去口 = pow(實_去口 / 方法_去口, Fraction(1, 3)) / 廉法_去口

# Step 6: 置去口，以周差乘之，以本高除之，所得加上周，即粟周
粟周 = ((去口 * 上下周差) / 高) + 上周

# Final answers
a = 上周 / 10  # Convert to 丈
b = 下周 / 10  # Convert to 丈
c = 高 / 10    # Convert to 丈
d = 去口 / 10  # Convert to 丈
e = 粟周 / 10  # Convert to 丈

# Output results
print(f"上周: {a}丈")
print(f"下周: {b}丈")
print(f"高: {c}丈")
print(f"去口: {d}丈")
print(f"粟周: {e}丈")
#----- content ends here -----


"""


### Explanation of Variables:
1. **`斛法`**: Conversion factor for volume (2尺5寸 = 2.5尺).
2. **`率徑`**: Ratio of circumference to diameter (1/3).
3. **`上下周差`**: Difference between the upper and lower circumferences (1丈2尺 = 12尺).
4. **`高多上周`**: Height exceeding the upper circumference (1丈8尺 = 18尺).
5. **`容粟`**: Total volume of grain (700斛6斗 = 756斗).
6. **`已運出`**: Grain already removed (266石4斗 = 2664斗).

### Explanation of Steps:
- The procedure involves calculating the frustum's dimensions (upper circumference, lower circumference, and height) and then determining the remaining grain's dimensions after some grain has been removed.
- The calculations use ancient Chinese mathematical methods, including ratios and cubic root extraction.

### Final Output:
The program calculates:
- `a`: Upper circumference in 丈.
- `b`: Lower circumference in 丈.
- `c`: Height in 丈.
- `d`: Remaining grain's height from the top in 丈.
- `e`: Remaining grain's surface circumference in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 0.008890281092874595
Variable 'b' has wrong value. Expected: 3, Actual: 1.2088902810928746
Variable 'c' has wrong value. Expected: 18/5, Actual: 1.8088902810928746
Variable 'd' has wrong value. Expected: 9/5, Actual: 53.786560078873336
Variable 'e' has wrong value. Expected: 12/5, Actual: 35.69036459121666"""
