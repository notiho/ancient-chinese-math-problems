"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
To solve this problem, we will follow the procedure step by step, translating the ancient Chinese mathematical method into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
章歲 = 700  # 章歲 (行分法)
朔月行定分 = 9000  # 朔月行定分
朔日定小余 = 10000  # 朔日定小余
日法 = 20000  # 日法
朔日夜半日所在度分 = Fraction(480, 1)  # 朔日夜半日所在度分 (480分 = 鬥10度7分)

# Step 1: 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# Step 2: 余以乘朔日定小余
先行分 = 余 * 朔日定小余

# Step 3: 滿日法而一
先行分 = Fraction(先行分, 日法)

# Step 4: 不盡者，半法已上收成一，已下者棄之
if 先行分 - int(先行分) >= Fraction(1, 2):
    先行分 = int(先行分) + 1
else:
    先行分 = int(先行分)

# Step 5: 若先行分滿日行分而一，為度分
度分 = Fraction(先行分, 1)

# Step 6: 以減朔日夜半日所在度分
度分 -= 朔日夜半日所在度分

# Step 7: 若度分不足減，加往宿度
if 度分 < 0:
    度分 += 360  # 加往宿度 (一周天 = 360度)

# Step 8: 其分不足減者，退一度為行分而減之
度 = int(度分)  # 整數部分為度
分 = (度分 - 度) * 日法  # 小數部分轉為分

# Final result
a = 度  # 鬥 a度
print(f"在鬥 {a}度。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1:** Subtract `朔月行定分` from `章歲` to get the remainder.
2. **Step 2:** Multiply the remainder by `朔日定小余`.
3. **Step 3:** Divide the result by `日法` to normalize it.
4. **Step 4:** Apply rounding rules: if the fractional part is greater than or equal to 0.5, round up; otherwise, round down.
5. **Step 5:** Convert the result into degrees and fractions.
6. **Step 6:** Subtract the given `朔日夜半日所在度分`.
7. **Step 7:** If the result is negative, add 360 degrees to adjust.
8. **Step 8:** Handle fractional parts by converting them into degrees and fractions.

This code follows the ancient procedure step by step to determine the position of the moon at the specified time.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: -4270"""
