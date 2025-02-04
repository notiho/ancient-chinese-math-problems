"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary with a conical frustum shape. The problem requires calculating the upper circumference, lower circumference, height, remaining grain level, and the circumference of the remaining grain. Below is the Python implementation of the solution based on the described procedure.

---

### Problem Breakdown:
1. **Given Data:**
   - The granary is a circular frustum.
   - Upper circumference (`上周`) and lower circumference (`下周`) differ by `1丈2尺 = 12尺`.
   - Height exceeds the upper circumference by `1丈8尺 = 18尺`.
   - Volume of the granary is `700斛5斗6升 = 700.56斛`.
   - Grain removed: `266石4斗 = 266.4石 = 2664斗`.
   - Conversion: `1斛 = 10斗`, `1石 = 10斗`.

2. **Procedure:**
   - Calculate the upper circumference, lower circumference, and height of the granary.
   - Calculate the remaining grain level (`去口`) after removing the grain.
   - Calculate the circumference of the remaining grain (`粟周`).

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Conversion factors
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
周差 = 12  # 1丈2尺 = 12尺
高差 = 18  # 1丈8尺 = 18尺
容粟 = 700.56 * 10  # 700斛5斗6升 = 700.56斛 = 7005.6斗
運出 = 266.4 * 10  # 266石4斗 = 266.4石 = 2664斗

# Step 1: Calculate the upper circumference, lower circumference, and height
# 以斛法乘容粟，又三十六乘之，三而一，為方亭之積
方亭積 = Fraction(斛法 * 容粟 * 36, 3)

# 又以周差自乘，三而一，為隅陽冪
隅陽冪 = Fraction(pow(周差, 2), 3)

# 以乘截高，以減亭積，余為實
截高 = 高差
實 = 方亭積 - 隅陽冪 * 截高

# 又周差乘截高，加隅陽冪，為方法
方法 = 周差 * 截高 + 隅陽冪

# 又以周差加截高，為廉法，從
廉法 = 周差 + 截高

# 開立方除之，得上周
上周 = pow(Fraction(實, 方法), 1/3)

# 加差，而合所問
下周 = 上周 + 周差
高 = 上周 + 高差

# Step 2: Calculate the remaining grain level (去口)
# 以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實
出斛 = 運出
實2 = Fraction(斛法 * 出斛 * 36, pow(周差, 2))

# 高乘上周，周差而一，為小高
小高 = Fraction(高 * 上周, 周差)

# 令自乘，三之，為方法
方法2 = Fraction(pow(小高, 2) * 3)

# 三因小高，為廉法，從
廉法2 = 3 * 小高

# 開立方除之，即去口
去口 = pow(Fraction(實2, 方法2), 1/3)

# Step 3: Calculate the circumference of the remaining grain (粟周)
# 置去口，以周差乘之，以本高除之，所得加上周，即粟周
粟周 = Fraction(去口 * 周差, 高) + 上周

# Final Results
a = 上周
b = 下周
c = 高
d = 去口
e = 粟周

print(f"上周: {a} 丈")
print(f"下周: {b} 丈")
print(f"高: {c} 丈")
print(f"去口: {d} 丈")
print(f"粟周: {e} 丈")
#----- content ends here -----


"""


---

### Explanation of Variables:
- `上周 (a)`: Upper circumference of the granary.
- `下周 (b)`: Lower circumference of the granary.
- `高 (c)`: Height of the granary.
- `去口 (d)`: Remaining grain level from the top.
- `粟周 (e)`: Circumference of the remaining grain.

### Notes:
1. The calculations involve fractions (`Fraction`) to maintain precision, as ancient Chinese mathematics often worked with exact ratios.
2. The cube root (`pow(x, 1/3)`) is used to solve for dimensions.
3. Ensure all units are consistent (e.g., converting `斛`, `斗`, and `石` to the same unit).

Let me know if you need further clarification or adjustments!
"""


"""
Code error: both arguments should be Rational instances"""
