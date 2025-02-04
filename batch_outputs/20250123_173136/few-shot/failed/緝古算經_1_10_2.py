"""
假令有粟一萬六千三百四十八石八斗，欲作方倉四、圓窖三，令高、深等，方面少於圓徑一丈，多於高五尺，斛法二尺五寸，率徑七，周二十二。問：方、高、徑多少？
術曰：以一十四乘斛法，以乘粟數，如八十九而一，為實。倍多加少，以乘少數，三十三乘之，八十九而一，多自乘加之，為方法。又倍少數，以三十三乘之，八十九而一，倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。
答曰：方 a丈 ，高深 b丈 ，圓徑 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for a square granary and a circular pit based on given relationships. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
- There is a total of 16,348 shi and 8 dou of grain.
- A square granary and a circular pit are to be constructed, with equal height/depth.
- The side length of the square granary is 1 zhang less than the diameter of the circular pit.
- The side length of the square granary is 5 chi more than the height/depth.
- The volume of the square granary and the circular pit are in the ratio 4:3.
- The "斛法" (unit conversion) is 2 chi 5 cun (2.5 chi).
- The ratio of the circumference to the diameter is given as 22:7.

The procedure involves:
1. Calculating the total volume of the square granary and the circular pit.
2. Using the relationships between the dimensions to solve for the side length, height, and diameter.

### Python Code:


"""


from fractions import Fraction
from math import pow

# 粟一萬六千三百四十八石八斗
粟石 = 16348
粟斗 = 8
# 1 石 = 10 斗
粟總斗 = 10 * 粟石 + 粟斗

# 斛法二尺五寸
斛法 = Fraction(5, 2)  # 2 尺 5 寸 = 2.5 尺

# 率徑七，周二十二
圓率 = Fraction(22, 7)

# 以一十四乘斛法
十四斛法 = 14 * 斛法

# 以乘粟數，如八十九而一，為實
實 = Fraction(十四斛法 * 粟總斗, 89)

# 倍多加少，以乘少數，三十三乘之，八十九而一，多自乘加之，為方法
少數 = 1  # Difference between square side and height (5 尺 = 1/2 丈)
多數 = 2  # Difference between circular diameter and square side (1 丈)

倍多加少 = 2 * 多數 + 少數
少數乘積 = 倍多加少 * 少數
三十三少數 = 33 * 少數乘積
方法 = Fraction(三十三少數, 89) + pow(多數, 2)

# 又倍少數，以三十三乘之，八十九而一，倍多加之，為廉法，從
倍少數 = 2 * 少數
三十三倍少數 = 33 * 倍少數
廉法 = Fraction(三十三倍少數, 89) + 2 * 多數

# 開立方除之，即高、深
高深 = pow(實 / 方法, Fraction(1, 3))

# 各加差，即方徑
方 = 高深 + 少數
圓徑 = 高深 + 多數

# 答案
a = 方
b = 高深
c = 圓徑

# Print results
print(f"方 {a} 丈")
print(f"高深 {b} 丈")
print(f"圓徑 {c} 丈")


"""


### Explanation of the Code:
1. **Volume Calculation**:
   - The total volume of grain is converted into dou and then multiplied by the "斛法" (unit conversion factor).
   - The volume is scaled by a factor of 14 and divided by 89 as per the procedure.

2. **Dimension Relationships**:
   - The relationships between the square side, circular diameter, and height are encoded using the given differences (1 zhang and 5 chi).

3. **Formulas for Methods**:
   - The procedure involves calculating two key formulas: `方法` (square granary method) and `廉法` (circular pit method).

4. **Solving for Dimensions**:
   - The height/depth is calculated by taking the cube root of the ratio of the total volume to the square granary method.
   - The side length of the square granary and the diameter of the circular pit are then calculated by adding the respective differences.

5. **Output**:
   - The results are printed as the side length of the square granary (`a`), the height/depth (`b`), and the diameter of the circular pit (`c`).

### Note:
This code adheres to the ancient procedure and uses only basic arithmetic and the `Fraction` class for precise calculations.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 23.22825655419319
Variable 'b' has wrong value. Expected: 13/10, Actual: 22.22825655419319
Variable 'c' has wrong value. Expected: 14/5, Actual: 24.22825655419319"""
