"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a complex ancient Chinese astronomical calculation problem. Let's break it down step by step and translate it into Python code.

The problem involves calculating the position of the moon at midnight on the first day of the eleventh month, based on various astronomical constants and relationships. Here's the solution:


"""


from fractions import Fraction

# Given constants
章歲 = 700  # Also called 行分法
朔月行定分 = 9000
朔日定小余 = 10000
日法 = 20000
朔日夜半日所在度分 = Fraction(480, 1)  # Given as 鬥十度七百分度之四百八十

# Step 1: 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# Step 2: 余以乘朔日定小余
先行分 = 余 * 朔日定小余

# Step 3: 滿日法而一
先行分 = Fraction(先行分, 日法)

# Step 4: 不盡者，半法已上收成一，已下者棄之
if 先行分.denominator > 1:
    if 先行分 - int(先行分) >= Fraction(1, 2):
        先行分 = int(先行分) + 1
    else:
        先行分 = int(先行分)

# Step 5: 若先行分滿日行分而一，為度分
度分 = 先行分

# Step 6: 以減朔日夜半日所在度分
度分 -= 朔日夜半日所在度分

# Step 7: 若度分不足減，加往宿度
if 度分 < 0:
    度分 += 360  # Add one full circle (360 degrees)

# Step 8: 其分不足減者，退一度為行分而減之
if 度分 < 1:
    度分 -= 1

# Step 9: 余即朔日夜半月行所在度及分也
a = 度分

# Answer
print(f"在鬥 {a} 度。")


"""


### Explanation of the Code:
1. **Constants**: The problem provides several constants, such as `章歲`, `朔月行定分`, `朔日定小余`, and `日法`. These are used in the calculations.
2. **Step-by-Step Procedure**: The code follows the procedure described in the problem, performing each calculation in sequence.
3. **Fraction Handling**: The `Fraction` class is used to handle non-integer values precisely, as ancient Chinese calculations often involve fractional arithmetic.
4. **Adjustments**: The code handles cases where values need to be rounded up or down, or where negative values need to be adjusted by adding a full circle (360 degrees).

### Final Answer:
The final value of `a` represents the position of the moon at midnight on the first day of the eleventh month, expressed in degrees.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: -4271"""
