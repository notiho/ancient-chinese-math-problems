"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a(=3)尺 ，下方 b(=9)尺 ，高 c(=6/5)丈 ；余粟深上方俱 d(=6)尺 。
"""

"""
This is a complex problem involving a frustum-shaped granary. Let's break it into two parts: first, solving for the dimensions of the granary (top side, bottom side, and height), and second, solving for the remaining depth and top side after some grain has been removed.

### Part 1: Solving for the granary dimensions
The procedure for finding the dimensions of the granary is as follows:

1. Multiply the volume of grain by the "斛法" (conversion factor for volume to cubic chi) to get the total cubic chi (積尺).
2. Square the difference between the top and bottom sides (方差), divide by 3 to get the "隅陽冪" (corner adjustment).
3. Multiply the height by the squared difference, subtract from the total cubic chi to get the "實" (adjusted volume).
4. Add the squared difference multiplied by the height to the corner adjustment to get the "方法" (method divisor).
5. Add the difference between the sides to the height to get the "廉法" (method divisor for the cube root).
6. Solve for the top side (上方) by taking the cube root of the ratio of the adjusted volume to the method divisor.

### Part 2: Solving for the remaining grain depth and top side
The procedure for finding the remaining grain depth and top side is as follows:

1. Multiply the removed grain volume by the "斛法" and by 3, then multiply by the squared height and divide by the squared difference between the sides to get the "實" (adjusted volume for removed grain).
2. Multiply the height by the top side and divide by the difference between the sides to get the "小高" (small height adjustment).
3. Square the small height adjustment, multiply by 3 to get the "方法" (method divisor for the cube root).
4. Multiply the small height adjustment by 3 to get the "廉法" (method divisor for the cube root).
5. Solve for the removed grain height by taking the cube root of the ratio of the adjusted volume to the method divisor.
6. Subtract the removed grain height from the total height to get the remaining grain depth.
7. Multiply the removed grain height by the difference between the sides, divide by the total height, and add to the top side to get the remaining top side.

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given values
容粟 = Fraction(187 * 10 + 2, 10)  # 187石2斗 converted to 石
出粟 = Fraction(50 * 10 + 4, 10)  # 50石4斗 converted to 石
斛法 = 10  # Conversion factor for 石 to cubic chi
方差 = 6  # Difference between top and bottom sides in chi
高多上方 = 9  # Height is 9 chi more than the top side

# 求倉方、高
# Step 1: Calculate total cubic chi (積尺)
積尺 = 容粟 * 斛法

# Step 2: Calculate 隅陽冪 (corner adjustment)
隅陽冪 = (方差 ** 2) / 3

# Step 3: Calculate 實 (adjusted volume)
實 = 積尺 - 隅陽冪 * 高多上方

# Step 4: Calculate 方法 (method divisor)
方法 = 方差 ** 2 * 高多上方 + 隅陽冪

# Step 5: Calculate 廉法 (method divisor for cube root)
廉法 = 方差 + 高多上方

# Step 6: Solve for 上方 (top side)
上方 = pow(float(實 / 方法), 1/3)

# Step 7: Calculate 下方 (bottom side) and 高 (height)
下方 = 上方 + 方差
高 = 上方 + 高多上方

# 求余粟高及上方
# Step 1: Calculate adjusted volume for removed grain (實)
實_出粟 = 出粟 * 斛法 * 3 * 高 ** 2 / 方差 ** 2

# Step 2: Calculate 小高 (small height adjustment)
小高 = 高 * 上方 / 方差

# Step 3: Calculate 方法 (method divisor for cube root)
方法_出粟 = 小高 ** 2 * 3

# Step 4: Calculate 廉法 (method divisor for cube root)
廉法_出粟 = 小高 * 3

# Step 5: Solve for removed grain height
出粟高 = pow(float(實_出粟 / 方法_出粟), 1/3)

# Step 6: Calculate remaining grain depth
余粟深 = 高 - 出粟高

# Step 7: Calculate remaining top side
余粟上方 = 出粟高 * 方差 / 高 + 上方

# Final results
a = Fraction(int(上方), 1)  # Top side in chi
b = Fraction(int(下方), 1)  # Bottom side in chi
c = Fraction(int(高 * 10), 10)  # Height in zhang (1丈 = 10尺)
d = Fraction(int(余粟上方), 1)  # Remaining grain depth and top side in chi

# Output results
print(f"上方 a={a} 尺")
print(f"下方 b={b} 尺")
print(f"高 c={c} 丈")
print(f"余粟深上方俱 d={d} 尺")
#----- content ends here -----


"""


### Explanation of Results
- `a`: Top side of the granary in chi.
- `b`: Bottom side of the granary in chi.
- `c`: Height of the granary in zhang (1丈 = 10尺).
- `d`: Remaining grain depth and top side in chi after removing the specified amount of grain.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 1
Variable 'b' has wrong value. Expected: 9, Actual: 7
Variable 'c' has wrong value. Expected: 6/5, Actual: 107/10
Variable 'd' has wrong value. Expected: 6, Actual: 4"""
