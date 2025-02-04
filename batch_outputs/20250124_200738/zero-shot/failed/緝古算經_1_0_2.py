"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves calculating the position of the moon at midnight on the first day of the eleventh month. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
章歲 = 700  # 行分法
朔月行定分 = 9000  # 定分
朔日定小余 = 10000  # 小余
日法 = 20000  # 日法
朔日夜半日所在度分 = Fraction(480, 1)  # 日所在度分 (480 in the question)

# Step 1: Calculate 先行分
余 = 章歲 - 朔月行定分
先行分 = (余 * 朔日定小余) // 日法  # Full units of 日法
先行分余 = (余 * 朔日定小余) % 日法  # Remainder

# Step 2: Adjust 先行分 based on the remainder
if 先行分余 >= 日法 / 2:
    先行分 += 1

# Step 3: Calculate 度分
度分 = 先行分 // 章歲  # Full units of 章歲
度分余 = 先行分 % 章歲  # Remainder

# Step 4: Subtract 朔日夜半日所在度分
if 度分 >= 朔日夜半日所在度分:
    a = 度分 - 朔日夜半日所在度分
else:
    a = 章歲 + 度分 - 朔日夜半日所在度分

# Final result
a = Fraction(a)  # Moon's position in 鬥 degrees
#----- content ends here -----


"""


The variable `a` will contain the moon's position in 鬥 degrees at midnight on the first day of the eleventh month.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 214"""
