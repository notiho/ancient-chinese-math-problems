"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary with a frustum shape. The problem asks for the remaining dimensions (upper circumference, lower circumference, height, and the remaining grain's distance from the top) after some grain has been removed. Let's break it down step by step and encode the solution in Python.

### Problem Breakdown:
1. **Given Data:**
   - Upper circumference (to be determined).
   - Lower circumference (to be determined).
   - Height (to be determined).
   - Circumference difference: `周差 = 12 丈 (1 丈 = 10 尺)`.
   - Height exceeds the upper circumference by `18 尺`.
   - Total grain volume: `容粟 = 700 斛 5 斗 6 升`.
   - Grain removed: `出粟 = 266 石 4 斗`.
   - Conversion factors:
     - `1 斛 = 10 斗`
     - `1 石 = 10 斗`
     - `1 丈 = 10 尺`
   - Circumference ratio: `π = 3`.

2. **Steps to Solve:**
   - Calculate the upper circumference, lower circumference, and height of the granary using the given formulas.
   - Calculate the remaining grain's distance from the top (`去口`) and the circumference at that level (`粟周`).

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(2, 1) + Fraction(5, 10)  # 2 尺 5 寸 = 2.5 尺
周差 = 12 * 10  # 12 丈 = 120 尺
高差 = 18  # 高多上周 1 丈 8 尺 = 18 尺
容粟 = 700 * 10 + 5 + Fraction(6, 10)  # 700 斛 5 斗 6 升 = 7000 + 5 + 0.6 = 7005.6 斗
出粟 = 266 * 10 + 4  # 266 石 4 斗 = 2660 + 4 = 2664 斗

# Step 1: Calculate the total height (高) and upper circumference (上周)
# Formula: 斛法 * 容粟 * 36 / 3 = 方亭之積
方亭積 = (斛法 * 容粟 * 36) / 3

# Formula: (周差^2) / 3 = 隅陽冪
隅陽冪 = (周差 ** 2) / 3

# Formula: 隅陽冪 * 高差 = 隅陽冪高
隅陽冪高 = 隅陽冪 * 高差

# Formula: 方亭積 - 隅陽冪高 = 實
實 = 方亭積 - 隅陽冪高

# Formula: 周差 * 高差 + 隅陽冪 = 方法
方法 = 周差 * 高差 + 隅陽冪

# Formula: 周差 + 高差 = 廉法
廉法 = 周差 + 高差

# Solve for 上周 (upper circumference)
上周 = pow(實 / 方法, Fraction(1, 3))

# Add 周差 to get 下周 (lower circumference)
下周 = 上周 + 周差

# Solve for 高 (height)
高 = 上周 + 高差

# Step 2: Calculate the remaining grain's distance from the top (去口) and 粟周
# Formula: 斛法 * 出粟 * 36 = 實
實_去口 = 斛法 * 出粟 * 36

# Formula: 實_去口 * 隅陽冪 / 周差 = 小高
小高 = (實_去口 * 隅陽冪) / 周差

# Formula: 小高^2 * 3 = 方法_去口
方法_去口 = (小高 ** 2) * 3

# Formula: 3 * 小高 = 廉法_去口
廉法_去口 = 3 * 小高

# Solve for 去口 (remaining grain's distance from the top)
去口 = pow(實_去口 / 方法_去口, Fraction(1, 3))

# Calculate 粟周 (circumference at the remaining grain level)
粟周 = (去口 * 周差) / 高 + 上周

# Final results
a = 上周 / 10  # Convert to 丈
b = 下周 / 10  # Convert to 丈
c = 高 / 10  # Convert to 丈
d = 去口 / 10  # Convert to 丈
e = 粟周 / 10  # Convert to 丈

print(f"上周 a = {a} 丈")
print(f"下周 b = {b} 丈")
print(f"高 c = {c} 丈")
print(f"去口 d = {d} 丈")
print(f"粟周 e = {e} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1: Calculating Dimensions**
   - The formulas provided in the problem are used to calculate the upper circumference (`上周`), lower circumference (`下周`), and height (`高`) of the granary.
   - These calculations involve the use of the given circumference difference (`周差`) and height difference (`高差`).

2. **Step 2: Calculating Remaining Grain's Distance and Circumference**
   - After removing some grain, the remaining grain's distance from the top (`去口`) and the circumference at that level (`粟周`) are calculated using the provided formulas.

3. **Units Conversion:**
   - All results are converted from `尺` to `丈` for the final output.

---

### Final Output:
The program will output the following values:
- `上周 a`: Upper circumference in 丈.
- `下周 b`: Lower circumference in 丈.
- `高 c`: Height in 丈.
- `去口 d`: Remaining grain's distance from the top in 丈.
- `粟周 e`: Circumference at the remaining grain level in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 0.2610155479778814
Variable 'b' has wrong value. Expected: 3, Actual: 12.26101554797788
Variable 'c' has wrong value. Expected: 18/5, Actual: 2.0610155479778816
Variable 'd' has wrong value. Expected: 9/5, Actual: 9.542467237887302e-05
Variable 'e' has wrong value. Expected: 12/5, Actual: 0.26157114595465064"""
