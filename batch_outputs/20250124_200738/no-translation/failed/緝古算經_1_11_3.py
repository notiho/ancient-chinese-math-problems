"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving cubic equations and geometric relationships. Below is the Python implementation of the procedure ("術") described:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 多自乘
多 = 2  # 多 is the difference between the square and the circle (2 feet)
多自乘 = 多 * 多

# 以並多少乘之
並多少 = 3  # 並多少 is the difference between the height of the square and the circle (3 feet)
並多少乘之 = 並多少 * 多

# 以乘一十四，如二十五而一
乘十四 = Fraction(14, 25)

# 所得以減率，余為實
實 = 率 - (多自乘 + 並多少乘之) * 乘十四

# 並多少，以乘多，倍之
並多倍之 = 2 * 並多少 * 多

# 乘一十四，如二十五而一，多自乘加之，為方法
方法 = 並多倍之 * 乘十四 + 多自乘

# 又並多少，以乘一十四，如二十五而一，加多加之，為廉法
廉法 = 並多少 * 乘十四 + 多

# 從。開立方除之，即窖深
窖深 = pow(float(實 / 方法), 1/3)

# 各加差，即方、徑、高
方 = 窖深 + 多
徑 = 窖深 + 多
高 = 窖深 + 並多少

# 答案
a = 方  # 方徑各 a丈
b = 高  # 高 b丈
c = 窖深  # 深 c丈

print(f"方徑各 {a:.2f} 丈，高 {b:.2f} 丈，深 {c:.2f} 丈。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Values**: The input values are the total amount of 粟 (3072 石), the difference between the square and circle depths (2 feet), and the difference between the square and circle heights (3 feet).
2. **Rate Calculation**: The rate (`率`) is calculated based on the given formula.
3. **Intermediate Steps**: The procedure involves several intermediate calculations, such as `多自乘`, `並多少乘之`, and `乘十四`.
4. **Key Formulas**: The `實`, `方法`, and `廉法` are calculated as per the procedure.
5. **Cubic Root**: The cubic root of `實 / 方法` gives the depth of the circular pit (`窖深`).
6. **Final Dimensions**: The dimensions of the square and circular pits are calculated by adding the respective differences.

### Output:
The program will output the dimensions of the square and circular pits:
- 方徑 (square side and circular diameter): `a` 丈
- 高 (height): `b` 丈
- 深 (depth): `c` 丈
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 9.372184607126329
Variable 'b' has wrong value. Expected: 19/10, Actual: 10.372184607126329
Variable 'c' has wrong value. Expected: 7/5, Actual: 7.372184607126328"""
