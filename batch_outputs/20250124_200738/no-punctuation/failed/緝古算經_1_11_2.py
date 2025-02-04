"""
假令有粟三千七十二石欲作方倉一圓窖一令徑與方等方於窖深二尺少於倉高三尺盛各滿中而粟適盡問方徑高深各多少
術曰三十五乘粟二十五而一為率多自乘以並多少乘之以乘一十四如二十五而一所得以減率余為實並多少以乘多倍之乘一十四如二十五而一多自乘加之為方法又並多少以乘一十四如二十五而一加多加之為廉法從開立方除之即窖深各加差即方徑高
答曰方徑各 a丈 高 b丈 深 c丈 
"""

#----- content starts here -----
"""
Suppose there are 3072 shi of millet, and it is desired to construct one square granary and one circular pit.
Let the diameter of the circular pit be equal to the side length of the square granary.
The square granary's height exceeds the circular pit's depth by 3 chi, and the circular pit's depth is 2 chi less than the square granary's height.
Both are filled to capacity, and the millet is exactly used up.
Question: What are the side length (or diameter), height, and depth?

The procedure says:
1. Multiply 35 by the millet, then divide by 25 to obtain the base ratio.
2. Multiply the base ratio by itself and add the product of the millet and 14, then divide by 25 to obtain the "method divisor."
3. Subtract the base ratio from the "method divisor" to obtain the "remainder."
4. Multiply the "remainder" by the base ratio and multiply by 14, then divide by 25 to obtain the "side length divisor."
5. Add the base ratio to the "side length divisor" to obtain the "side length."
6. Multiply the base ratio by 14, then divide by 25 to obtain the "height divisor."
7. Add the base ratio to the "height divisor" to obtain the "height."
8. Subtract 3 chi from the height to obtain the depth.

Answer: The side length (or diameter) is *a* zhang, the height is *b* zhang, and the depth is *c* zhang.
"""

from fractions import Fraction

# 粟三千七十二石
粟 = 3072

# 三十五乘粟
率 = 35 * 粟

# 二十五而一
率 = Fraction(率, 25)

# 多自乘
多自乘 = 率 * 率

# 以並多少乘之
並多少 = 粟 * 14

# 以乘一十四如二十五而一
並多少 = Fraction(並多少, 25)

# 所得以減率余為實
實 = 並多少 - 率

# 並多少以乘多倍之
多倍之 = 實 * 率

# 乘一十四如二十五而一
多倍之 = Fraction(多倍之 * 14, 25)

# 多自乘加之為方法
方法 = 多自乘 + 多倍之

# 又並多少以乘一十四如二十五而一
廉法 = Fraction(率 * 14, 25)

# 加多加之為廉法
廉法 = 廉法 + 率

# 從開立方除之即窖深
方徑 = 方法 ** Fraction(1, 3)

# 各加差即方徑高
高 = 廉法

# 深 = 高 - 3
深 = 高 - 3

a = 方徑
b = 高
c = 深#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 230.72192036608152
Variable 'b' has wrong value. Expected: 19/10, Actual: 838656/125
Variable 'c' has wrong value. Expected: 7/5, Actual: 838281/125"""
