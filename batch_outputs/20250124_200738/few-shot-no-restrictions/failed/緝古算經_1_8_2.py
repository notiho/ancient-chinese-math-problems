"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary with a frustum-like shape. The problem requires calculating the dimensions of the granary (upper circumference, lower circumference, and height) and the remaining grain's dimensions after some grain has been removed. Below is the Python implementation of the solution, step by step.

### Problem Breakdown:
1. **Given Data:**
   - The granary has an upper circumference smaller than the lower circumference.
   - The circumference difference is 12 chi (1丈2尺).
   - The height exceeds the upper circumference by 18 chi (1丈8尺).
   - The granary can hold 756 dou of grain.
   - 266 shi and 4 dou of grain have been removed.
   - The task is to calculate:
     - Upper circumference (`a`),
     - Lower circumference (`b`),
     - Height (`c`),
     - Remaining grain's distance to the opening (`d`),
     - Remaining grain's circumference (`e`).

2. **Procedure:**
   - Use the formulas provided in the problem to calculate the required values step by step.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
周差 = 12  # 1丈2尺 = 12尺
高差 = 18  # 1丈8尺 = 18尺
容粟 = 756  # 756斛6斗
已運出 = 266 * 10 + 4  # 266石4斗 (1石 = 10斗)

# Step 1: Calculate the total volume of the granary in cubic chi
# 容粟 * 斛法 * 36 / 3
方亭積 = Fraction(容粟 * 斛法 * 36, 3)

# Step 2: Calculate 隅陽冪 (corner volume)
# 周差^2 / 3
隅陽冪 = Fraction(周差**2, 3)

# Step 3: Calculate the height of the granary
# 高 = 方亭積 - 隅陽冪 / (周差 * 高差 + 隅陽冪)
方法 = 周差 * 高差 + 隅陽冪
高 = Fraction(方亭積 - 隅陽冪, 方法)

# Step 4: Calculate the upper circumference
# 上周 = 開立方(方亭積 / 方法)
上周 = pow(float(Fraction(方亭積, 方法)), 1/3)

# Step 5: Calculate the lower circumference
# 下周 = 上周 + 周差
下周 = 上周 + 周差

# Step 6: Calculate the remaining grain volume
# 剩餘粟 = 容粟 - 已運出
剩餘粟 = 容粟 - 已運出

# Step 7: Calculate the distance to the opening (去口)
# 去口 = 剩餘粟 * 斛法 * 36 / (高 * 隅陽冪)
去口實 = 剩餘粟 * 斛法 * 36
去口方法 = 高 * 隅陽冪
去口 = Fraction(去口實, 去口方法)

# Step 8: Calculate the circumference of the remaining grain
# 粟周 = 上周 + (周差 * 去口 / 高)
粟周 = 上周 + Fraction(周差 * 去口, 高)

# Final results
a = 上周
b = 下周
c = 高
d = 去口
e = 粟周

print(f"上周 (a): {a} 丈")
print(f"下周 (b): {b} 丈")
print(f"高 (c): {c} 丈")
print(f"去口 (d): {d} 丈")
print(f"粟周 (e): {e} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1:** Calculate the total volume of the granary (`方亭積`) using the formula provided: `容粟 * 斛法 * 36 / 3`.
2. **Step 2:** Calculate the corner volume (`隅陽冪`) using `周差^2 / 3`.
3. **Step 3:** Calculate the height (`高`) using the formula: `(方亭積 - 隅陽冪) / (周差 * 高差 + 隅陽冪)`.
4. **Step 4:** Calculate the upper circumference (`上周`) by taking the cube root of `方亭積 / 方法`.
5. **Step 5:** Calculate the lower circumference (`下周`) by adding the circumference difference (`周差`) to the upper circumference.
6. **Step 6:** Calculate the remaining grain volume (`剩餘粟`) by subtracting the removed grain from the total grain.
7. **Step 7:** Calculate the distance to the opening (`去口`) using the formula: `剩餘粟 * 斛法 * 36 / (高 * 隅陽冪)`.
8. **Step 8:** Calculate the circumference of the remaining grain (`粟周`) using the formula: `上周 + (周差 * 去口 / 高)`.

---

### Output:
The program will output the following values:
- `a`: Upper circumference in 丈.
- `b`: Lower circumference in 丈.
- `c`: Height in 丈.
- `d`: Distance to the opening in 丈.
- `e`: Circumference of the remaining grain in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 4.412449091688448
Variable 'b' has wrong value. Expected: 3, Actual: 16.412449091688448
Variable 'c' has wrong value. Expected: 18/5, Actual: 943/11
Variable 'd' has wrong value. Expected: 9/5, Actual: -78705/1886
Variable 'e' has wrong value. Expected: 12/5, Actual: -1.4290306288397732"""
