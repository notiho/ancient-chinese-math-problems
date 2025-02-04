"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a(=453/100)丈 ，窖徑 b(=231/50)丈 ，高與深各 c(=31/20)丈 。
"""

"""
Suppose there are 23120 hu, 7 dou, and 3 sheng of millet. It is desired to construct one square granary and one circular pit, each filled to capacity such that the millet is exactly used up. 
Let the height (or depth) of both be equal, and let the side of the square granary be 9 cun less than the diameter of the circular pit, and 2 zhang 9 chi 8 cun greater than the height. 
The ratio of the diameter to the circumference is 7:22.

Question: What are the side length of the square granary, the diameter of the circular pit, and the height (or depth)?

The procedure for finding the side, diameter, height, and depth says:
Multiply 14 by the hu divisor, then multiply by the millet quantity, and divide by 25 to obtain the dividend. 
Double the excess and add the deficit, then multiply by the deficit, and multiply by 11, dividing by 25, and add the square of the excess to obtain the square divisor. 
Double the deficit, multiply by 11, divide by 25, and double the excess and add it to obtain the linear divisor. Extract the cube root and divide to obtain the height (or depth). Add the differences to obtain the side and diameter. 

Verification procedure:
The square granary's side is squared, then multiplied by the height to obtain the volume. 
The circular pit's diameter is squared, then multiplied by the depth, then multiplied by 11, and divided by 14 to obtain the volume. 
Divide both by the hu divisor to verify the millet quantity.

Answer: The side of the square granary is *a*(=453/100) zhang, the diameter of the circular pit is *b*(=231/50) zhang, and the height (or depth) is *c*(=31/20) zhang.
"""

from fractions import Fraction
from math import isclose

# 粟數：二萬三千一百二十斛七斗三升
粟數 = Fraction(23120 * 10 + 7 + Fraction(3, 10))  # Convert to dou (1 hu = 10 dou)

# 斛法
斛法 = 100  # 1 hu = 100 cubic chi

# 方少於圓徑九寸，多於高二丈九尺八寸
少數 = Fraction(9, 10)  # 9 cun = 9/10 chi
多數 = Fraction(2 * 10 + 9 + Fraction(8, 10))  # 2 zhang 9 chi 8 cun = 29.8 chi

# 比率：徑七，周二十二
圓率 = Fraction(22, 7)

# 術曰：十四乘斛法，以乘粟數，二十五而一，為實
實 = Fraction(14 * 斛法 * 粟數, 25)

# 又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法
方法 = Fraction(2 * 多數 + 少數, 1) * 少數
方法 = Fraction(11 * 方法, 25) + 多數**2

# 又倍少數，十一乘之，二十五而一，又倍多加之，為廉法
廉法 = Fraction(2 * 少數, 1)
廉法 = Fraction(11 * 廉法, 25) + 2 * 多數

# 從。開立方除之，即高、深
高深 = (實 / 方法).sqrt() / 廉法

# 各加差，即方徑
方 = 高深 + 多數
徑 = 高深 + 少數

# 驗算
倉方體積 = 方**2 * 高深
窖體積 = (徑**2 * 高深 * 11) / 14

倉方粟數 = 倉方體積 / 斛法
窖粟數 = 窖體積 / 斛法

assert isclose(float(倉方粟數 + 窖粟數), float(粟數)), "Verification failed!"

# 答案
a = 方  # 453/100 zhang
b = 徑  # 231/50 zhang
c = 高深  # 31/20 zhang
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
