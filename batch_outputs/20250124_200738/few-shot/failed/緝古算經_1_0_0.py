"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a complex ancient Chinese calendrical calculation problem. Let's carefully translate the procedure into Python code step by step:

### Problem Breakdown:
- The problem involves calculating the position of the moon at midnight on the first day of the 11th lunar month.
- The calculation uses several constants and involves modular arithmetic and rounding rules.

### Procedure:
1. Subtract the "朔月行定分" (fixed monthly motion of the moon) from the "章歲" (cycle year divisor).
2. Multiply the remainder by the "朔日定小余" (fixed small remainder for the new moon).
3. Divide the product by the "日法" (day divisor) to get the "先行分" (initial motion fraction).
4. Handle rounding: if the remainder is greater than or equal to half the divisor, round up; otherwise, discard it.
5. If the "先行分" exceeds the "日行分" (daily motion divisor), convert it into degrees and fractions.
6. Subtract the result from the sun's position at midnight. If insufficient, adjust by adding or subtracting one degree as needed.
7. The final result is the moon's position in degrees and fractions.

### Constants:
- 章歲 (Cycle year divisor): 700
- 朔月行定分 (Fixed monthly motion of the moon): 9000
- 朔日定小余 (Fixed small remainder for the new moon): 10000
- 日法 (Day divisor): 20000
- 朔日夜半日所在度分 (Sun's position at midnight): 鬥 10度 7分之 480分 (斗 10 degrees, 7/480 of a degree)

### Code Implementation:

"""

#----- content starts here -----

from fractions import Fraction

# Constants
章歲 = 700
朔月行定分 = 9000
朔日定小余 = 10000
日法 = 20000
朔日夜半日所在度 = 10  # 10 degrees
朔日夜半日所在分 = Fraction(7, 480)  # 7/480 of a degree

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder by 朔日定小余
乘積 = 余 * 朔日定小余

# Step 3: Divide the product by 日法 to get 先行分
先行分 = Fraction(乘積, 日法)

# Step 4: Handle rounding
# If the remainder is greater than or equal to half the divisor, round up; otherwise, discard it.
if 先行分.denominator > 1:
    if 先行分 - int(先行分) >= Fraction(1, 2):
        先行分 = int(先行分) + 1
    else:
        先行分 = int(先行分)

# Step 5: Convert 先行分 into degrees and fractions if it exceeds 日行分
日行分 = 1  # Daily motion divisor (1 degree)
if 先行分 >= 日行分:
    度分 = 先行分 // 日行分  # Whole degrees
    分 = 先行分 % 日行分  # Remaining fractions
else:
    度分 = 0
    分 = 先行分

# Step 6: Subtract from the sun's position at midnight
月所在度 = 朔日夜半日所在度 - 度分
月所在分 = 朔日夜半日所在分 - 分

# Handle insufficient fractions
if 月所在分 < 0:
    月所在度 -= 1
    月所在分 += 1  # Add 1 degree worth of fractions

# Final result
a = 月所在度 + 月所在分
#----- content ends here -----


"""


### Explanation of the Answer:
- `a` represents the moon's position in degrees and fractions at midnight on the first day of the 11th lunar month.
- The calculation follows the ancient procedure exactly, including modular arithmetic and rounding rules.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 1996807/480"""
