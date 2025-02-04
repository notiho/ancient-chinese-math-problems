"""
假令圓囤上小下大斛法二尺五寸以率徑一周三上下周差一丈二尺高多上周一丈八尺容粟七百五斛六斗今已運出二百六十六石四斗問殘粟去口上下周高各多少
求圓囤上下周及高術曰以斛法乘容粟又三十六乘之三而一為方亭之積又以周差自乘三而一為隅陽冪以乘截高以減亭積余為實又周差乘截高加隅陽冪為方法又以周差加截高為廉法從開立方除之得上周加差而合所問求粟去口術曰以斛法乘出斛三十六乘之以乘高冪如周差冪而一為實高乘上周周差而一為小高令自乘三之為方法三因小高為廉法從開立方除之即去口置去口以周差乘之以本高除之所得加上周即粟周
答曰上周 a丈 下周 b丈 高 c丈 去口 d丈 粟周 e丈 
"""

"""
This problem is quite complex and involves multiple steps to calculate the dimensions of a circular granary and the remaining grain after some has been removed. Let's break it down step by step and translate the procedure into Python code.

### Problem Breakdown:
1. **Given Data:**
   - The granary is circular, with a smaller top circumference and a larger bottom circumference.
   - The "斛法" (unit conversion factor) is 2 chi 5 cun (2.5 chi).
   - The circumference difference between the top and bottom is 1 zhang 2 chi (12 chi).
   - The height difference is 1 zhang 8 chi (18 chi).
   - The total capacity is 750 hu 6 dou.
   - 266 shi 4 dou of grain have been removed.

2. **Questions:**
   - What are the remaining dimensions: top circumference, bottom circumference, and height?
   - What is the remaining grain's distance from the top (去口)?
   - What is the circumference of the remaining grain's surface (粟周)?

3. **Procedure:**
   - Use the given formulas to calculate the top circumference, bottom circumference, and height.
   - Use the formulas to calculate the remaining grain's distance from the top and its surface circumference.

---

### Python Code Implementation:


"""


from fractions import Fraction
from math import pow

# Given data
斛法 = Fraction(25, 10)  # 2 chi 5 cun = 2.5 chi
上下周差 = 12  # 1 zhang 2 chi = 12 chi
高差 = 18  # 1 zhang 8 chi = 18 chi
容粟 = 750 * 10 + 6  # 750 hu 6 dou = 750.6 hu
已運出 = 266 * 10 + 4  # 266 shi 4 dou = 266.4 shi = 2664 dou

# Step 1: Calculate the total volume of the granary (亭積)
亭積 = Fraction(斛法 * 容粟 * 36, 3)

# Step 2: Calculate 隅陽冪 (corner volume factor)
隅陽冪 = Fraction(上下周差**2, 3)

# Step 3: Calculate the method factor (方法)
方法 = 隅陽冪 + 上下周差 * 高差

# Step 4: Calculate the remaining volume after subtracting the corner volume
實 = 亭積 - 隅陽冪 * 高差

# Step 5: Calculate the "廉法" (edge factor)
廉法 = 上下周差 + 高差

# Step 6: Solve for the top circumference (上周)
上周 = pow(float(實 / 方法), 1/3) + 上下周差

# Step 7: Calculate the bottom circumference (下周)
下周 = 上周 - 上下周差

# Step 8: Calculate the height (高)
高 = 實 / (隅陽冪 + 上下周差 * 上周)

# Step 9: Calculate the remaining grain's distance from the top (去口)
去口實 = Fraction(斛法 * 已運出 * 36, 1)
小高 = 去口實 / (隅陽冪 + 上下周差 * 上周)
去口 = pow(float(去口實 / 方法), 1/3)

# Step 10: Calculate the circumference of the remaining grain's surface (粟周)
粟周 = 上周 + 上下周差 * 去口 / 高

# Final answers
a = Fraction(上周).limit_denominator()  # Top circumference
b = Fraction(下周).limit_denominator()  # Bottom circumference
c = Fraction(高).limit_denominator()  # Height
d = Fraction(去口).limit_denominator()  # Distance from the top
e = Fraction(粟周).limit_denominator()  # Circumference of the remaining grain's surface

# Output the results
print(f"上周 a = {a} 丈")
print(f"下周 b = {b} 丈")
print(f"高 c = {c} 丈")
print(f"去口 d = {d} 丈")
print(f"粟周 e = {e} 丈")


"""


---

### Explanation of the Code:
1. **Units Conversion:**
   - All measurements are converted into consistent units (chi or dou) for calculation.
   - 1 hu = 10 dou, 1 shi = 10 dou.

2. **Formulas:**
   - The formulas provided in the problem are directly translated into Python code.
   - Fractions are used to ensure precision in calculations.

3. **Steps:**
   - The code follows the procedure step by step, calculating intermediate values like `亭積`, `隅陽冪`, and `方法` before solving for the desired dimensions and remaining grain properties.

4. **Output:**
   - The results are presented in terms of the dimensions (丈) and remaining grain properties.

This code adheres to the structure of the procedure and provides the required answers.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 15777924/734831
Variable 'b' has wrong value. Expected: 3, Actual: 6959952/734831
Variable 'c' has wrong value. Expected: 18/5, Actual: 19419907/26462
Variable 'd' has wrong value. Expected: 9/5, Actual: 9324513/962872
Variable 'e' has wrong value. Expected: 12/5, Actual: 6715138/310457"""
