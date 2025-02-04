"""
假令亭倉上小下大上下方差六尺高多上方九尺容粟一百八十七石二斗今已運出五十石四斗問倉上下方高及余粟深上方各多少
求倉方高術曰以斛法乘容粟為積尺又方差自乘三而一為隅陽冪以乘截高以減積余為實又方差乘截高加隅陽冪為方法又置方差加截高為廉法從開立方除之即上方加差即合所問求余粟高及上方術曰以斛法乘出粟三之以乘高冪令方差冪而一為實高乘上方方差而一為小高令自乘三之為方法三因小高為廉法從開立方除之得取出高以減本高余即殘粟高置出粟高又以方差乘之以本高除之所得加上方即余粟上方
答曰上方 a尺 下方 b尺 高 c丈 余粟深上方俱 d尺 
"""

"""
This is a complex problem involving a frustum-shaped granary. Let's break it down step by step and encode the solution in Python.

### Problem Breakdown:
1. **Given Data**:
   - The granary is frustum-shaped, with the top smaller than the bottom.
   - The difference in side lengths between the top and bottom is 6 chi.
   - The height of the granary is 9 chi.
   - The granary can hold 187 shi and 2 dou of millet.
   - 50 shi and 4 dou of millet have been removed.

2. **Questions**:
   - Find the dimensions of the granary: top side length, bottom side length, and height.
   - Find the remaining depth of millet and the new top side length.

3. **Procedure**:
   - Use the given formulas to calculate the dimensions of the granary and the remaining millet.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
容粟 = 187 + Fraction(2, 10)  # 容粟 in 石 (1 石 = 10 斗)
已出粟 = 50 + Fraction(4, 10)  # 已出粟 in 石
方差 = 6  # 上下方差 in 尺
高 = 9  # 高 in 尺
斛法 = 10  # 1 石 = 10 斗, so 斛法 = 10

# 求倉方高術:
# Step 1: 以斛法乘容粟為積尺
積尺 = 斛法 * 容粟

# Step 2: 方差自乘三而一為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# Step 3: 隅陽冪乘截高以減積余為實
實 = 積尺 - 隅陽冪 * 高

# Step 4: 方差乘截高加隅陽冪為方法
方法 = 方差 * 高 + 隅陽冪

# Step 5: 置方差加截高為廉法
廉法 = 方差 + 高

# Step 6: 開立方除之即上方
上方 = pow(float(實 / 方法 / 廉法), 1/3)

# Step 7: 加差即下方
下方 = 上方 + 方差

# Step 8: 高即合所問
c = Fraction(高, 10)  # 高 in 丈 (1 丈 = 10 尺)

# 求余粟高及上方術:
# Step 1: 以斛法乘出粟三之
出粟積 = Fraction(斛法 * 已出粟, 3)

# Step 2: 乘高冪令方差冪而一為實
高冪 = 高**2
實余 = 出粟積 * 高冪 / 方差

# Step 3: 高乘上方方差而一為小高
小高 = 高 * 上方 * 方差 / 3

# Step 4: 自乘三之為方法
方法余 = 小高**2 * 3

# Step 5: 小高為廉法
廉法余 = 小高

# Step 6: 開立方除之得取出高
取出高 = pow(float(實余 / 方法余 / 廉法余), 1/3)

# Step 7: 減本高余即殘粟高
余粟高 = 高 - 取出高

# Step 8: 置出粟高以方差乘之以本高除之所得加上方即余粟上方
余粟上方 = (取出高 * 方差 / 高) + 上方

# Final results
a = Fraction(上方).limit_denominator()  # 上方 in 尺
b = Fraction(下方).limit_denominator()  # 下方 in 尺
c = Fraction(c).limit_denominator()  # 高 in 丈
d = Fraction(余粟上方).limit_denominator()  # 余粟上方 in 尺

# Output results
print(f"上方 a = {a} 尺")
print(f"下方 b = {b} 尺")
print(f"高 c = {c} 丈")
print(f"余粟深上方俱 d = {d} 尺")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **求倉方高術**:
   - This part calculates the dimensions of the granary (top side, bottom side, and height) using the given formulas.
   - The key steps involve calculating the total volume in chi³, adjusting for the frustum shape, and solving for the top side length.

2. **求余粟高及上方術**:
   - This part calculates the remaining depth of millet and the new top side length after some millet has been removed.
   - The steps involve recalculating the volume for the removed millet and adjusting the dimensions accordingly.

3. **Units**:
   - All calculations are done in chi (尺) for lengths and shi (石) for volumes, with appropriate conversions where necessary.

4. **Output**:
   - The results are presented as fractions for precision, matching the style of ancient Chinese mathematics.

---

### Final Answer:
The program will output:
- `a`: Top side length in chi.
- `b`: Bottom side length in chi.
- `c`: Height in zhang (丈).
- `d`: Remaining depth of millet and new top side length in chi.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 1122491/925895
Variable 'b' has wrong value. Expected: 9, Actual: 6677861/925895
Variable 'c' has wrong value. Expected: 6/5, Actual: 9/10
Variable 'd' has wrong value. Expected: 6, Actual: 1238807/831059"""
