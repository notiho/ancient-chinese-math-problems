"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This problem involves calculating the position of the moon at midnight on the first day of the eleventh month, based on ancient Chinese astronomical methods. The procedure involves several steps using modular arithmetic and fractional calculations. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Given constants
章歲 = 700  # The "Zhang Sui" (cycle of years), also called the "movement divisor"
朔月行定分 = 9000  # Fixed movement of the moon per synodic month
朔日定小余 = 10000  # Fixed remainder for the synodic day
日法 = 20000  # Divisor for the sun's movement
朔日夜半日所在度分 = Fraction(480, 1)  # The position of the sun at midnight on the first day of the month (斗 10度 7分 = 480分)

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder (余) by 朔日定小余
先行分 = 余 * 朔日定小余

# Step 3: Divide by 日法 and take the integer part (modular arithmetic)
先行分 = Fraction(先行分, 日法)

# Step 4: Round the remainder
if 先行分.denominator > 2 and 先行分.numerator * 2 >= 先行分.denominator:
    先行分 = 先行分.numerator // 先行分.denominator + 1
else:
    先行分 = 先行分.numerator // 先行分.denominator

# Step 5: Convert 先行分 to 度分
度分 = Fraction(先行分, 1)

# Step 6: Subtract 朔日夜半日所在度分 from 度分
if 度分 >= 朔日夜半日所在度分:
    月所在度分 = 度分 - 朔日夜半日所在度分
else:
    # If 度分 is insufficient, add the full cycle (宿度, 360 degrees or equivalent in 分)
    宿度 = 360 * 60  # Convert degrees to 分
    月所在度分 = 宿度 + 度分 - 朔日夜半日所在度分

# Step 7: If 分不足减, adjust by retreating one degree
if 月所在度分 < 0:
    月所在度分 += 60  # Add one degree (60分) to compensate
    月所在度分 -= 1  # Retreat one degree

# Final result
a = 月所在度分 // 60  # Convert 分 back to 度
print(f"在鬥 {a}度。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Constants**: The constants provided in the problem are directly translated into variables.
2. **Step-by-step procedure**: The procedure described in the problem is implemented step by step, including modular arithmetic and rounding rules.
3. **Adjustments**: If the remainder is insufficient for subtraction, adjustments are made by adding or retreating degrees as described in the problem.
4. **Final result**: The result is converted back into degrees (`a`), which represents the position of the moon.

### Answer:
The moon's position at midnight on the first day of the eleventh month is **在鬥 a度**, where `a` is the calculated degree.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 282"""
