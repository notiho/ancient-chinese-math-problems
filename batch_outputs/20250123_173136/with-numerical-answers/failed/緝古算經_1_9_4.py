"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a(=453/100)丈 ，窖徑 b(=231/50)丈 ，高與深各 c(=31/20)丈 。
"""

"""
Suppose there are 23120 hu, 7 dou, and 3 sheng of millet. It is desired to construct one square granary and one round silo, each filled to capacity, such that the millet is exactly used up. Let the height of the granary and the depth of the silo be equal. Let the side of the square granary be 9 cun less than the diameter of the round silo, and 2 zhang 9 chi 8 cun more than the height. Assume the ratio of the circumference to the diameter is 22:7.

Question: What are the side length of the square granary, the diameter of the round silo, and the height/depth?

The procedure for finding the side, diameter, height, and depth says:
1. Multiply 14 by the hu divisor, then multiply by the total millet amount. Divide by 25 to get the dividend.
2. Double the "more" value, add the "less" value, multiply by the "less" value, then multiply by 11. Divide by 25, then add the square of the "more" value to get the divisor for the square granary.
3. Double the "less" value, multiply by 11, divide by 25, then double the "more" value and add it to get the divisor for the round silo.
4. Extract the cube root of the dividend divided by the divisor to get the height/depth. Add the "more" and "less" values to get the side and diameter.
5. Verify by calculating the volume of the square granary and the round silo, ensuring they sum to the total millet amount.

Answer: The side of the square granary is *a*(=453/100) zhang, the diameter of the round silo is *b*(=231/50) zhang, and the height/depth is *c*(=31/20) zhang.
"""

from fractions import Fraction
from math import isclose

# 粟數 (convert to hu)
粟數 = Fraction(23120) + Fraction(7, 10) + Fraction(3, 100)

# 方倉少於圓徑九寸 (convert to zhang)
少數 = Fraction(9, 100)

# 方倉多於高二丈九尺八寸 (convert to zhang)
多數 = Fraction(2) + Fraction(9, 10) + Fraction(8, 100)

# 率徑七，周二十二
圓率 = Fraction(22, 7)

# Step 1: Calculate the dividend
十四 = 14
斛法 = 100  # 1 hu = 100 sheng
實 = (十四 * 斛法 * 粟數) / 25

# Step 2: Calculate the divisor for the square granary
倍多 = 2 * 多數
倍多加少 = 倍多 + 少數
方法 = ((倍多加少 * 少數 * 11) / 25) + (多數 ** 2)

# Step 3: Calculate the divisor for the round silo
倍少 = 2 * 少數
廉法 = ((倍少 * 11) / 25) + 倍多

# Step 4: Calculate the height/depth
高深 = (實 / (方法 + 廉法)) ** Fraction(1, 3)

# Calculate the side of the square granary and the diameter of the round silo
倉方 = 高深 + 多數
窖徑 = 高深 + 少數

# Step 5: Verify the result
# Square granary volume
倉方積 = 倉方 ** 2 * 高深

# Round silo volume
窖徑積 = (窖徑 ** 2 * 高深 * 11) / 14

# Total volume
總積 = (倉方積 + 窖徑積) / 斛法

# Verify that the total volume matches the millet amount
assert isclose(float(總積), float(粟數)), "Verification failed!"

# Final answers
a = 倉方  # 453/100 zhang
b = 窖徑  # 231/50 zhang
c = 高深  # 31/20 zhang
"""
Code error: Verification failed!"""
