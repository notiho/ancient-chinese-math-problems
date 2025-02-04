"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The solution involves several steps of calculations as described in the problem. Here's the Python implementation:


"""


from fractions import Fraction

# Given values
章歲 = 700  # "章歲" as the base unit
朔月行定分 = 9000  # 定分 for the new moon
朔日定小余 = 10000  # 定小余 for the new moon
日法 = 20000  # 日法
朔日夜半日所在度分 = Fraction(480, 1)  # 日所在度分 (480 in the problem)

# Step 1: Calculate 先行分
先行分 = (章歲 - 朔月行定分) * 朔日定小余 // 日法

# Step 2: Handle rounding for 先行分
if (章歲 - 朔月行定分) * 朔日定小余 % 日法 >= 日法 / 2:
    先行分 += 1

# Step 3: Calculate 度分
度分 = 先行分 // 朔日定小余
度分余 = 先行分 % 朔日定小余

# Step 4: Adjust 度分 based on 朔日夜半日所在度分
if 度分 < 朔日夜半日所在度分:
    度分 += 360  # Add one full circle (360 degrees)

if 度分余 < 朔日夜半日所在度分:
    度分 -= 1
    度分余 += 朔日定小余

# Final result
a = 度分 + Fraction(度分余, 朔日定小余)


"""


The variable `a` will contain the final answer for the location of the moon at midnight on the new moon day.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 71917/200"""
