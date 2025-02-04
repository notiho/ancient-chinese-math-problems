"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving a circular granary (圓囤) with a tapering shape. It requires calculating the upper circumference, lower circumference, height, remaining grain level, and the circumference of the grain surface after some grain has been removed. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given Data:**
   - The granary has a tapering shape with a top circumference smaller than the bottom.
   - The "斛法" (volume unit) is 2 chi 5 cun (2.5 chi).
   - The ratio of circumference to diameter is 3 (π = 3).
   - The difference between the top and bottom circumferences is 12 chi (1丈2尺).
   - The height exceeds the top circumference by 18 chi (1丈8尺).
   - The total capacity of the granary is 756斛6斗.
   - 266石4斗 of grain has been removed.

2. **Questions:**
   - Calculate the upper circumference, lower circumference, height, remaining grain level, and the circumference of the grain surface.

3. **Procedure:**
   - Use the formulas provided in the problem to calculate the required values step by step.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(5, 2)  # 2 chi 5 cun = 2.5 chi
周差 = 12  # Difference between top and bottom circumferences (1丈2尺 = 12 chi)
高差 = 18  # Height exceeds top circumference (1丈8尺 = 18 chi)
容粟 = 756 + Fraction(6, 10)  # Total capacity in 斛 (756斛6斗 = 756.6斛)
運出 = 266 + Fraction(4, 10)  # Grain removed in 石 (266石4斗 = 266.4石)
石_to_斛 = 10  # 1石 = 10斛
運出斛 = 運出 * 石_to_斛  # Convert removed grain to 斛

# Step 1: Calculate the upper circumference (上周), lower circumference (下周), and height (高)
# Formula: Use the given procedure to calculate these values.

# Calculate 方亭之積 (volume of the truncated cone)
亭積 = (斛法 * 容粟 * 36) / 3

# Calculate 隅陽冪 (square of 周差 divided by 3)
隅陽冪 = (周差 ** 2) / 3

# Calculate 方法 (method divisor)
方法 = 隅陽冪 + (周差 * 高差)

# Calculate 廉法 (linear divisor)
廉法 = 周差 + 高差

# Solve for 上周 (top circumference)
上周 = pow((亭積 / 方法), 1/3)

# Calculate 下周 (bottom circumference)
下周 = 上周 + 周差

# Calculate 高 (height)
高 = 上周 + 高差

# Step 2: Calculate the remaining grain level (去口) and 粟周 (grain surface circumference)
# Formula: Use the given procedure to calculate these values.

# Calculate 去口 (remaining grain level)
去口實 = (斛法 * 運出斛 * 36) / ((周差 ** 2) / 3)
小高 = (高 * 上周) / 周差
方法_去口 = 3 * (小高 ** 2)
廉法_去口 = 3 * 小高
去口 = pow((去口實 / 方法_去口), 1/3)

# Calculate 粟周 (grain surface circumference)
粟周 = (去口 * 周差 / 高) + 上周

# Final Results
a = 上周 / 10  # Convert chi to zhang
b = 下周 / 10  # Convert chi to zhang
c = 高 / 10  # Convert chi to zhang
d = 去口 / 10  # Convert chi to zhang
e = 粟周 / 10  # Convert chi to zhang

# Output the results
print(f"上周: {a}丈")
print(f"下周: {b}丈")
print(f"高: {c}丈")
print(f"去口: {d}丈")
print(f"粟周: {e}丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Conversion:** All measurements are converted into consistent units (chi) for calculations. The `斛法` is converted to `Fraction` for precise arithmetic.
2. **Step-by-Step Calculation:** The formulas provided in the problem are implemented step by step to calculate the required values.
3. **Output Conversion:** The final results are converted back to zhang (1丈 = 10尺) for the answer.

### Final Answer:
The program will output the following:
- `上周 (a丈)`: Top circumference in zhang.
- `下周 (b丈)`: Bottom circumference in zhang.
- `高 (c丈)`: Height in zhang.
- `去口 (d丈)`: Remaining grain level in zhang.
- `粟周 (e丈)`: Grain surface circumference in zhang.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 0.44136160975856786
Variable 'b' has wrong value. Expected: 3, Actual: 1.6413616097585677
Variable 'c' has wrong value. Expected: 18/5, Actual: 2.2413616097585676
Variable 'd' has wrong value. Expected: 9/5, Actual: 0.2904387689791935
Variable 'e' has wrong value. Expected: 12/5, Actual: 0.5968592863751377"""
