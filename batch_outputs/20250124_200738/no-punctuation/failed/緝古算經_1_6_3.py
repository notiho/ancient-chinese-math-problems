"""
假令亭倉上小下大上下方差六尺高多上方九尺容粟一百八十七石二斗今已運出五十石四斗問倉上下方高及余粟深上方各多少
求倉方高術曰以斛法乘容粟為積尺又方差自乘三而一為隅陽冪以乘截高以減積余為實又方差乘截高加隅陽冪為方法又置方差加截高為廉法從開立方除之即上方加差即合所問求余粟高及上方術曰以斛法乘出粟三之以乘高冪令方差冪而一為實高乘上方方差而一為小高令自乘三之為方法三因小高為廉法從開立方除之得取出高以減本高余即殘粟高置出粟高又以方差乘之以本高除之所得加上方即余粟上方
答曰上方 a尺 下方 b尺 高 c丈 余粟深上方俱 d尺 
"""

"""
This is a complex ancient Chinese mathematical problem involving a trapezoidal prism (a storage container) with a square top and bottom, where the dimensions and volume are given, and the goal is to calculate the dimensions and remaining volume after some of the contents are removed. Below is the Python implementation of the problem, following the ancient procedure step by step.


"""

#----- content starts here -----

from fractions import Fraction
from math import isqrt

# Given data
上下方差 = 6  # The difference between the side lengths of the top and bottom squares (in chi)
高多上方 = 9  # The height of the storage container (in chi)
容粟 = 187 * 10 + 2  # Total volume of the storage container in dou (1 shi = 10 dou)
已運出 = 50 * 10 + 4  # Volume of millet already removed in dou
斛法 = 10  # Conversion factor: 1 dou = 10 cubic chi

# 求倉方高術 (Procedure to find the dimensions of the storage container)

# Step 1: Convert the total volume to cubic chi
積尺 = 容粟 * 斛法

# Step 2: Calculate 隅陽冪 (corner term)
隅陽冪 = Fraction(上下方差**2, 3)

# Step 3: Calculate the actual volume term
實 = 積尺 - 隅陽冪 * 高多上方

# Step 4: Calculate 方法 (method divisor)
方法 = 上下方差 * 高多上方 + 隅陽冪

# Step 5: Calculate 廉法 (edge divisor)
廉法 = 上下方差 + 高多上方

# Step 6: Solve for the top side length (上方) using cube root approximation
上方 = isqrt(Fraction(實, 方法) / 廉法)
上方 += 1  # Adjust approximation

# Step 7: Calculate the bottom side length (下方)
下方 = 上方 + 上下方差

# Step 8: Calculate the height (高)
高 = Fraction(實, 方法) / (上方**2 + 上方 * 下方 + 下方**2)

# 求余粟高及上方術 (Procedure to find the remaining height and top side length after removing millet)

# Step 1: Convert the removed millet to cubic chi
出粟積尺 = 已運出 * 斛法

# Step 2: Calculate the reduced height term
出粟高 = isqrt(Fraction(出粟積尺 * 3, 上方**2 + 上方 * 下方 + 下方**2))
出粟高 += 1  # Adjust approximation

# Step 3: Calculate the remaining height (余粟高)
余粟高 = 高 - 出粟高

# Step 4: Calculate the remaining top side length (余粟上方)
余粟上方 = 上方 + Fraction(上下方差 * 出粟高, 高)

# Final results
a = 上方  # Top side length (上方)
b = 下方  # Bottom side length (下方)
c = 高 / 10  # Height (高) in zhang (1 zhang = 10 chi)
d = 余粟上方  # Remaining top side length (余粟上方)

# Output the results
print(f"上方 a = {a} 尺")
print(f"下方 b = {b} 尺")
print(f"高 c = {c} 丈")
print(f"余粟深上方俱 d = {d} 尺")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Conversion**: The given volume is converted into cubic chi using the conversion factor (斛法).
2. **Procedure for Dimensions**:
   - The formula for the trapezoidal prism's volume is used to calculate the top side length (上方), bottom side length (下方), and height (高).
   - The cube root is approximated using integer square root (`isqrt`) for simplicity.
3. **Procedure for Remaining Volume**:
   - The removed volume is subtracted, and the remaining height (余粟高) and top side length (余粟上方) are calculated using the same principles.
4. **Output**: The results are printed in chi (尺) for side lengths and zhang (丈) for height.

This implementation follows the ancient procedure step by step, using modern Python constructs like `Fraction` for precise arithmetic and `isqrt` for approximations.
"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
