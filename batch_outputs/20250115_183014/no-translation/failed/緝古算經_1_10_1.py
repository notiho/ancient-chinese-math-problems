"""
假令有粟一萬六千三百四十八石八斗，欲作方倉四、圓窖三，令高、深等，方面少於圓徑一丈，多於高五尺，斛法二尺五寸，率徑七，周二十二。問：方、高、徑多少？
術曰：以一十四乘斛法，以乘粟數，如八十九而一，為實。倍多加少，以乘少數，三十三乘之，八十九而一，多自乘加之，為方法。又倍少數，以三十三乘之，八十九而一，倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。
答曰：方 a丈 ，高深 b丈 ，圓徑 c丈 。
"""

"""
To solve this problem, we will follow the procedure ("術") step by step and encode it into Python. Let's break it down:


"""


from fractions import Fraction
from math import pow

# 粟一萬六千三百四十八石八斗，轉換為斗
粟數 = 16348 * 10 + 8  # 1石 = 10斗

# 斛法二尺五寸，轉換為尺
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺

# 率徑七，周二十二
率徑 = 7
率周 = 22

# 方倉四，圓窖三
方倉 = 4
圓窖 = 3

# 方面少於圓徑一丈，多於高五尺
少數 = 1  # 少於圓徑1丈
多數 = Fraction(5, 10)  # 多於高5尺 = 0.5丈

# Step 1: 以一十四乘斛法，以乘粟數，如八十九而一，為實
實 = Fraction(14 * 斛法 * 粟數, 89)

# Step 2: 倍多加少，以乘少數，三十三乘之，八十九而一，多自乘加之，為方法
倍多 = 2 * 多數
倍多加少 = 倍多 + 少數
方法 = Fraction(33 * 倍多加少 * 少數, 89) + pow(倍多, 2)

# Step 3: 又倍少數，以三十三乘之，八十九而一，倍多加之，為廉法
倍少 = 2 * 少數
廉法 = Fraction(33 * 倍少, 89) + 倍多

# Step 4: 從。開立方除之，即高、深
高深 = pow(Fraction(實, 方法), Fraction(1, 3))

# Step 5: 各加差，即方徑
方 = 高深 + 多數
圓徑 = 高深 + 少數

# Results
a = 方
b = 高深
c = 圓徑

# Output the results
a, b, c


"""


### Explanation of Variables:
- `粟數`: Total amount of 粟 in 斗.
- `斛法`: Conversion factor for 斛法 in 尺.
- `率徑` and `率周`: Ratios for circular calculations.
- `少數` and `多數`: Differences between dimensions.
- `實`: Intermediate calculation based on 粟數 and 斛法.
- `方法`: Formula for 方倉.
- `廉法`: Formula for 圓窖.
- `高深`: Height/depth of the倉 or窖.
- `方` and `圓徑`: Final dimensions for the square倉 and circular窖.

This code follows the ancient procedure step by step and calculates the required dimensions.
"""


"""
Code error: both arguments should be Rational instances"""
