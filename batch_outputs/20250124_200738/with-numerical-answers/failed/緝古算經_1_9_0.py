"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a(=453/100)丈 ，窖徑 b(=231/50)丈 ，高與深各 c(=31/20)丈 。
"""

#----- content starts here -----
"""
Suppose there are 23120 hu, 7 dou, and 3 sheng of millet. It is desired to construct one square granary and one circular pit, each filled completely with millet. 
Let the height and depth be equal, and let the side of the square granary be 9 cun less than the diameter of the circular pit, and 2 zhang 9 chi 8 cun more than the height.
The ratio of the circumference to the diameter is 22:7.

Question: What are the side length of the square granary, the diameter of the circular pit, and the height/depth?

The procedure for finding the side, diameter, height, and depth says:
Multiply 14 by the hu-divisor, then multiply by the millet quantity, and divide by 25 to obtain the dividend.
Double the excess and add the deficit, then multiply by the deficit, multiply by 11, and divide by 25. Add the square of the excess to this to obtain the divisor for the square granary.
Double the deficit, multiply by 11, and divide by 25. Then double the excess and add it to this to obtain the divisor for the circular pit.
Extract the cube root of the dividend divided by the divisor to obtain the height/depth. Add the differences to obtain the side and diameter.

Verification: The procedure says: The side of the granary is squared, then multiplied by the height to obtain the volume. The diameter of the pit is squared, then multiplied by the depth, then multiplied by 11, and divided by 14 to obtain the volume. Divide both by the hu-divisor to verify the millet quantity.

Answer: The side of the granary is *a*(=453/100) zhang, the diameter of the pit is *b*(=231/50) zhang, and the height/depth is *c*(=31/20) zhang.
"""

from fractions import Fraction
import math

# 粟數：23120斛7斗3升
粟數 = Fraction(23120) + Fraction(7, 10) + Fraction(3, 100)

# 斛法：1斛 = 100升
斛法 = 100

# 方倉少於圓徑9寸 (差1)
少數 = Fraction(9, 10)

# 方倉多於高2丈9尺8寸 (差2)
多數 = Fraction(2 * 10 + 9, 10) + Fraction(8, 10)

# 圓周率：22/7
圓率 = Fraction(22, 7)

# 求實
實 = Fraction(14 * 斛法 * 粟數, 25)

# 求方法 (方倉)
方法 = Fraction(11 * (2 * 多數 + 少數) * 少數, 25) + 多數**2

# 求廉法 (圓窖)
廉法 = Fraction(11 * 2 * 少數, 25) + 2 * 多數

# 求高、深
高深 = Fraction(math.isqrt(實 / 方法), 1)

# 求方倉邊長
倉方 = 高深 + 多數

# 求圓窖直徑
窖徑 = 高深 + 少數

# 驗算
倉實 = 倉方**2 * 高深
窖實 = 窖徑**2 * 高深 * Fraction(11, 14)
驗算粟數 = Fraction(倉實 +#----- content ends here -----

"""
Code error: '(' was never closed (<string>, line 59)"""
