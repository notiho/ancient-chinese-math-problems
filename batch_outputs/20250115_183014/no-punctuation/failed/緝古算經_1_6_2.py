"""
假令亭倉上小下大上下方差六尺高多上方九尺容粟一百八十七石二斗今已運出五十石四斗問倉上下方高及余粟深上方各多少
求倉方高術曰以斛法乘容粟為積尺又方差自乘三而一為隅陽冪以乘截高以減積余為實又方差乘截高加隅陽冪為方法又置方差加截高為廉法從開立方除之即上方加差即合所問求余粟高及上方術曰以斛法乘出粟三之以乘高冪令方差冪而一為實高乘上方方差而一為小高令自乘三之為方法三因小高為廉法從開立方除之得取出高以減本高余即殘粟高置出粟高又以方差乘之以本高除之所得加上方即余粟上方
答曰上方 a尺 下方 b尺 高 c丈 余粟深上方俱 d尺 
"""

"""
This is a complex ancient Chinese mathematical problem involving a frustum-shaped granary. Let's break it down step by step and translate the procedure into Python code.

### Problem Description:
A granary has a frustum shape, with the top square smaller than the bottom square. The difference between the side lengths of the top and bottom squares is 6 chi, and the height is 9 chi more than the side length of the top square. The granary can hold 187 shi and 2 dou of grain. After removing 50 shi and 4 dou of grain, we are tasked to calculate:
1. The side lengths of the top and bottom squares.
2. The height of the granary.
3. The remaining depth of the grain.
4. The side length of the top square for the remaining grain.

### Procedure:
The procedure involves several steps, including calculating the dimensions of the granary and the remaining grain volume. Let's implement this step by step.

---


"""


from fractions import Fraction
import math

# Initial data
容粟 = 187 + Fraction(2, 10)  # Total grain volume in shi (1 dou = 1/10 shi)
出粟 = 50 + Fraction(4, 10)   # Grain removed in shi
方差 = 6                      # Difference between top and bottom square side lengths in chi
高差 = 9                      # Height is 9 chi more than the top square side length
斛法 = 10                     # Conversion factor: 1 shi = 10 cubic chi

# 求倉方高術
# Step 1: Convert grain volume to cubic chi
積尺 = 容粟 * 斛法

# Step 2: 方差自乘三而一為隅陽冪
隅陽冪 = Fraction(方差**2, 3)

# Step 3: 隅陽冪乘截高 (截高 = 高差)
截高 = 高差
隅陽冪乘截高 = 隅陽冪 * 截高

# Step 4: Subtract 隅陽冪乘截高 from 積尺 to get 實
實 = 積尺 - 隅陽冪乘截高

# Step 5: 方差乘截高加隅陽冪為方法
方法 = 方差 * 截高 + 隅陽冪

# Step 6: 方差加截高為廉法
廉法 = 方差 + 截高

# Step 7: Solve for the top square side length (上方) using the cubic root
上方 = (實 / 方法) ** Fraction(1, 3)

# Step 8: Add 方差 to 上方 to get the bottom square side length (下方)
下方 = 上方 + 方差

# Step 9: Add 高差 to 上方 to get the height (高)
高 = 上方 + 高差

# 求余粟高及上方術
# Step 1: Convert 出粟 to cubic chi
出粟積尺 = 出粟 * 斛法

# Step 2: 出粟積尺三之
出粟積尺三之 = 出粟積尺 * 3

# Step 3: Multiply by 高冪 (上方方差冪而一)
高冪 = 上方**2 + 上方 * 下方 + 下方**2
實 = 出粟積尺三之 / 高冪

# Step 4: Calculate the remaining grain height (余粟高)
余粟高 = 實

# Step 5: Calculate the remaining top square side length (余粟上方)
余粟上方 = 上方 + (方差 * 余粟高 / 高)

# Final results
a = 上方
b = 下方
c = 高
d = 余粟上方

print(f"上方: {a} 尺, 下方: {b} 尺, 高: {c} 丈, 余粟深上方俱: {d} 尺")


"""


### Explanation of Variables:
- `上方`: The side length of the top square in chi.
- `下方`: The side length of the bottom square in chi.
- `高`: The height of the granary in zhang (1 zhang = 10 chi).
- `余粟高`: The remaining depth of the grain in chi.
- `余粟上方`: The side length of the top square for the remaining grain in chi.

### Notes:
1. The procedure involves solving a cubic equation, which is implemented using fractional arithmetic for precision.
2. The results are expressed in chi and zhang as per the problem's requirements.
3. The code adheres to the structure of the ancient procedure ("術").
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 2.989864787615432
Variable 'b' has wrong value. Expected: 9, Actual: 8.989864787615431
Variable 'c' has wrong value. Expected: 6/5, Actual: 11.989864787615431
Variable 'd' has wrong value. Expected: 6, Actual: 9.47707874886689"""
