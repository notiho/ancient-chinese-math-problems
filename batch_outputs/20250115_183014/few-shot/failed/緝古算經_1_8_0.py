"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary with a tapered shape. The solution involves multiple steps, including calculating the upper and lower circumferences, the height, the remaining grain volume, and the grain's surface circumference. Below is the Python code that follows the procedure described in the problem:


"""


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
# Step 1: Calculate 方亭之積
方亭積 = Fraction(斛法 * 容粟 * 36, 3)

# Step 2: Calculate 隅陽冪
隅陽冪 = Fraction(上下周差**2, 3)

# Step 3: Calculate 實
實 = 方亭積 - 隅陽冪 * 高多上周

# Step 4: Calculate 方法
方法 = 隅陽冪 + 上下周差 * 高多上周

# Step 5: Calculate 廉法
廉法 = 上下周差 + 高多上周

# Step 6: 求上周
上周 = pow(Fraction(實, 方法), Fraction(1, 3))

# Step 7: 求下周
下周 = 上周 + 上下周差

# Step 8: 求高
高 = 上周 + 高多上周

# 求粟去口
# Step 1: Calculate 實 for 去口
去口實 = Fraction(斛法 * 已運出 * 36, 1) * Fraction(高**2, 上下周差**2)

# Step 2: Calculate 方法 for 去口
去口方法 = Fraction(高 * 上周, 上下周差)

# Step 3: Calculate 廉法 for 去口
去口廉法 = Fraction(3 * 去口方法, 1)

# Step 4: 求去口
去口 = pow(Fraction(去口實, 去口方法), Fraction(1, 3))

# Step 5: 求粟周
粟周 = Fraction(去口 * 上下周差, 高) + 上周

# Final results
a = 上周 / 10  # Convert to 丈
b = 下周 / 10  # Convert to 丈
c = 高 / 10    # Convert to 丈
d = 去口 / 10  # Convert to 丈
e = 粟周 / 10  # Convert to 丈

print(f"上周 a丈 = {a}")
print(f"下周 b丈 = {b}")
print(f"高 c丈 = {c}")
print(f"去口 d丈 = {d}")
print(f"粟周 e丈 = {e}")


"""


### Explanation of the Code:
1. **斛法**: The unit conversion factor for the volume of grain.
2. **率徑**: The circular ratio (π approximated as 3 in ancient Chinese math).
3. **上下周差**: The difference between the upper and lower circumferences.
4. **高多上周**: The height difference relative to the upper circumference.
5. **容粟**: The total volume of grain in the granary.
6. **已運出**: The volume of grain already removed.

The calculations follow the procedure described in the problem, step by step, using fractions to ensure precision. The results are converted to 丈 (1丈 = 10尺) for the final answer.
"""


"""
Code error: both arguments should be Rational instances"""
