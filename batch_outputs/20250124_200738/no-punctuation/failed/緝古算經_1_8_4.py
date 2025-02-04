"""
假令圓囤上小下大斛法二尺五寸以率徑一周三上下周差一丈二尺高多上周一丈八尺容粟七百五斛六斗今已運出二百六十六石四斗問殘粟去口上下周高各多少
求圓囤上下周及高術曰以斛法乘容粟又三十六乘之三而一為方亭之積又以周差自乘三而一為隅陽冪以乘截高以減亭積余為實又周差乘截高加隅陽冪為方法又以周差加截高為廉法從開立方除之得上周加差而合所問求粟去口術曰以斛法乘出斛三十六乘之以乘高冪如周差冪而一為實高乘上周周差而一為小高令自乘三之為方法三因小高為廉法從開立方除之即去口置去口以周差乘之以本高除之所得加上周即粟周
答曰上周 a丈 下周 b丈 高 c丈 去口 d丈 粟周 e丈 
"""

"""
This is a complex problem involving a frustum-shaped grain storage container. The problem requires calculating the dimensions of the container (upper circumference, lower circumference, and height) as well as the remaining grain level and circumference after some grain has been removed. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction
from math import isqrt

# Given values
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
容粟 = Fraction(756, 1)  # 756斛6斗 = 756.6斛
出斛 = Fraction(2664, 10)  # 266石4斗 = 266.4斛
上下周差 = Fraction(12, 1)  # 1丈2尺 = 12尺
高 = Fraction(18, 1)  # 1丈8尺 = 18尺

# 求圓囤上下周及高術
# Step 1: Calculate 方亭之積
方亭之積 = Fraction(斛法 * 容粟 * 36, 3)

# Step 2: Calculate 隅陽冪
隅陽冪 = Fraction(上下周差**2, 3)

# Step 3: Calculate 方法
方法 = 隅陽冪 + (上下周差 * 高)

# Step 4: Calculate 亭積余
亭積余 = 方亭之積 - (隅陽冪 * 高)

# Step 5: Calculate 廉法
廉法 = 上下周差 + 高

# Step 6: Solve for 上周
上周加差 = isqrt(亭積余 * 廉法 // 方法)
上周 = 上周加差 - 上下周差

# Step 7: Solve for 下周
下周 = 上周 + 上下周差

# Step 8: Solve for 高
高 = 高

# 求粟去口術
# Step 1: Calculate 出粟的方亭之積
出粟方亭之積 = Fraction(斛法 * 出斛 * 36, 1)

# Step 2: Calculate 小高
小高 = Fraction(出粟方亭之積, 隅陽冪)

# Step 3: Calculate 方法 for 出粟
方法出粟 = Fraction(小高**2 * 3, 1)

# Step 4: Solve for 去口
去口 = isqrt(出粟方亭之積 * 廉法 // 方法出粟)

# Step 5: Calculate 粟周
粟周 = Fraction(上下周差 * 去口, 高) + 上周

# Final results
a = 上周 / 10  # Convert to 丈
b = 下周 / 10  # Convert to 丈
c = 高 / 10  # Convert to 丈
d = 去口 / 10  # Convert to 丈
e = 粟周 / 10  # Convert to 丈

print(f"上周: {a}丈, 下周: {b}丈, 高: {c}丈, 去口: {d}丈, 粟周: {e}丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. **斛法**: The unit conversion factor for the container.
2. **容粟**: The total volume of the grain stored initially.
3. **上下周差**: The difference between the upper and lower circumferences.
4. **高**: The height of the container.
5. **方亭之積**: The volume of the frustum-shaped container.
6. **隅陽冪**: A derived value based on the circumference difference.
7. **方法**: A divisor used to calculate the upper circumference.
8. **廉法**: A divisor used to calculate the remaining grain level.
9. **去口**: The remaining height of the grain after some has been removed.
10. **粟周**: The circumference of the grain level after removal.

The results are expressed in 丈 (a traditional Chinese unit of length).
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 37/10
Variable 'b' has wrong value. Expected: 3, Actual: 49/10
Variable 'c' has wrong value. Expected: 18/5, Actual: 9/5
Variable 'd' has wrong value. Expected: 9/5, Actual: 0.0
Variable 'e' has wrong value. Expected: 12/5, Actual: 37/10"""
