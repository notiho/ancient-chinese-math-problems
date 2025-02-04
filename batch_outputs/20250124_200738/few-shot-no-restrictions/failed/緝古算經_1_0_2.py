"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a complex ancient Chinese astronomical problem involving the calculation of the moon's position at midnight on the first day of the eleventh month. The problem uses traditional Chinese astronomical terms and methods, including concepts like "章歲" (Zhang Sui, a cycle of years), "朔月行定分" (fixed motion of the moon in a synodic month), "朔日定小余" (small remainder for the synodic day), and "日法" (day divisor).

Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
章歲 = 700  # Zhang Sui (cycle of years)
朔月行定分 = 9000  # Fixed motion of the moon in a synodic month
朔日定小余 = 10000  # Small remainder for the synodic day
日法 = 20000  # Day divisor
朔日夜半日所在度分 = Fraction(480, 1)  # Sun's position at midnight on the first day of the month (斗 10度 7分, converted to 分)

# Step 1: Subtract 章歲 from 朔月行定分
余 = 朔月行定分 - 章歲

# Step 2: Multiply the remainder by 朔日定小余
先行分 = 余 * 朔日定小余

# Step 3: Divide by 日法 and take the integer part
先行分 = Fraction(先行分, 日法)

# Step 4: Round the remainder (半法已上收成一, 已下者棄之)
if 先行分.denominator > 1:
    if 先行分 - int(先行分) >= Fraction(1, 2):
        先行分 = int(先行分) + 1
    else:
        先行分 = int(先行分)

# Step 5: If 先行分 exceeds 日法, convert to 度分
if 先行分 >= 日法:
    度分 = Fraction(先行分, 日法)
else:
    度分 = 先行分

# Step 6: Subtract 朔日夜半日所在度分 from 度分
if 度分 >= 朔日夜半日所在度分:
    月所在度分 = 度分 - 朔日夜半日所在度分
else:
    # If 度分 is insufficient, add 往宿度 (360 degrees in 分)
    往宿度 = 360 * 日法
    月所在度分 = 往宿度 + 度分 - 朔日夜半日所在度分

# Step 7: If 分不足减, adjust by retreating one degree
if 月所在度分 < 0:
    月所在度分 += 日法
    月所在度分 -= 1

# Convert 月所在度分 to degrees and 分
月所在度 = 月所在度分 // 日法
月所在分 = 月所在度分 % 日法

# Final answer
a = 月所在度
print(f"答曰：在鬥 {a}度 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The problem provides the constants for the calculations, such as `章歲`, `朔月行定分`, `朔日定小余`, and `日法`.
2. **Step-by-Step Calculation**: The procedure follows the ancient algorithm:
   - Subtract `章歲` from `朔月行定分`.
   - Multiply the remainder by `朔日定小余`.
   - Divide by `日法` and round the result.
   - Adjust for cases where the result exceeds `日法` or is insufficient to subtract.
3. **Output**: The final position of the moon in degrees (`a`) is calculated and printed.

This implementation adheres to the ancient procedure described in the problem. If you have specific values for the constants or additional clarifications, feel free to provide them, and I can refine the code further!
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 0"""
