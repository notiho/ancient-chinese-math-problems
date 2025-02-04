"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a(=453/100)丈 ，窖徑 b(=231/50)丈 ，高與深各 c(=31/20)丈 。
"""

#----- content starts here -----
"""
Suppose there are 23120 hu, 7 dou, and 3 sheng of millet. It is desired to construct one square granary and one circular pit, each filled to capacity such that the millet is exactly used up. Let the height (of the granary) and depth (of the pit) be equal. Let the side of the square granary be 9 cun less than the diameter of the circular pit, and 2 zhang 9 chi 8 cun greater than the height. Assume the ratio of the circumference to the diameter is 22:7.

Question: What are the side length of the square granary, the diameter of the circular pit, and the height/depth?

The procedure says:
1. Multiply 14 by the hu divisor (斛法), then multiply by the millet quantity, and divide by 25 to obtain the dividend (實).
2. Double the excess and add the deficit, then multiply by the deficit, multiply by 11, and divide by 25. Add the square of the excess to this to obtain the square divisor (方法).
3. Double the deficit, multiply by 11, and divide by 25. Then double the excess and add it to this to obtain the edge divisor (廉法).
4. Extract the cube root of the dividend divided by the square divisor to obtain the height/depth.
5. Add the differences to the height/depth to obtain the side length and diameter.
6. Verify by calculating the volume of the square granary and circular pit.

Answer: The side length of the square granary is *a*(=453/100) zhang, the diameter of the circular pit is *b*(=231/50) zhang, and the height/depth is *c*(=31/20) zhang.
"""

from fractions import Fraction
from math import isclose

# 粟數：23120斛7斗3升
粟數 = Fraction(23120) + Fraction(7, 10) + Fraction(3, 100)

# 斛法：1斛 = 100升
斛法 = 100

# 方少於圓徑9寸 (少數)
少數 = Fraction(9, 10)

# 方多於高2丈9尺8寸 (多數)
多數 = 2 * 10 + 9 + Fraction(8, 10)

# 圓周率：22/7
圓率 = Fraction(22, 7)

# Step 1: Calculate 實
實 = Fraction(14 * 斛法 * 粟數, 25)

# Step 2: Calculate 方法
方法 = Fraction(11 * (多數 + 少數) * 少數, 25) + 多數**2

# Step 3: Calculate 廉法
廉法 = Fraction(11 * 2 * 少數, 25) + 2 * 多數

# Step 4: Extract the cube root of 實/方法 to find 高/深
高深 = (實 / 方法) ** Fraction(1, 3)

# Step 5: Add differences to 高/深 to find 方 and 徑
倉方 = 高深 + 多數
窖徑 = 高深 + 少數

# Step 6: Verify by calculating the volumes
倉實 = 倉方**2 * 高深
窖實 = 窖徑**2 * 高深 * Fraction(11, 14)
總實 = (倉實 + 窖實) / 斛法

# Ensure the calculated volume matches the given 粟數
assert isclose(float(總實), float(粟數)), "Verification failed!"

# Final answers
a = 倉方  # 453/100
b = 窖徑  # 231/50
c = 高深  # 31/20#----- content ends here -----

"""
Code error: Verification failed!"""
