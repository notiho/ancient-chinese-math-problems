"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves determining the dimensions of a square warehouse and a circular pit based on the given conditions. Let's proceed with the translation.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 多自乘
多 = 3  # The difference in height between the square warehouse and the circular pit
多自乘 = 多 * 多

# 以並多少乘之
並多少 = 2  # The difference in depth between the square warehouse and the circular pit
並多少乘之 = 並多少 * 多

# 以乘一十四，如二十五而一
乘一十四 = Fraction(14, 25)
部分1 = 並多少乘之 * 乘一十四

# 所得以減率，余為實
實 = 率 - 部分1

# 並多少，以乘多，倍之
部分2 = 並多少 * 多 * 2

# 乘一十四，如二十五而一
部分3 = 部分2 * 乘一十四

# 多自乘加之，為方法
方法 = 多自乘 + 部分3

# 又並多少，以乘一十四，如二十五而一，加多加之，為廉法
部分4 = 並多少 * 乘一十四
廉法 = 部分4 + 多

# 從。開立方除之，即窖深
窖深 = pow(float(實 / 方法), 1/3)

# 各加差，即方、徑、高
深 = 窖深
方 = 窖深 + 並多少
徑 = 方
高 = 窖深 + 多

# 答案
a = 方  # 方、徑各 a丈
b = 高  # 高 b丈
c = 深  # 深 c丈

print(f"方徑各 {a:.2f} 丈，高 {b:.2f} 丈，深 {c:.2f} 丈。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Values**: The total amount of grain (`粟`) is given as 3072 石. The differences in height and depth are specified as 3 丈 and 2 丈, respectively.
2. **Rate Calculation**: The rate (`率`) is calculated using the formula provided in the procedure.
3. **Intermediate Steps**: The procedure involves several intermediate calculations, such as `多自乘`, `並多少乘之`, and their respective transformations using the fraction `14/25`.
4. **Final Calculations**: Using the derived formulas for `方法` and `廉法`, the depth of the circular pit (`窖深`) is calculated by solving a cubic equation. The dimensions of the square warehouse and circular pit are then determined by adding the respective differences.
5. **Output**: The results are printed as the dimensions of the square warehouse (`方` and `徑`), its height (`高`), and the depth of the circular pit (`深`).

Let me know if you'd like further clarification or adjustments!
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 8.490115515250611
Variable 'b' has wrong value. Expected: 19/10, Actual: 9.490115515250611
Variable 'c' has wrong value. Expected: 7/5, Actual: 6.490115515250611"""
