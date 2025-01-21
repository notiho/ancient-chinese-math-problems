"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The solution involves computing the position of the moon at midnight on the first day of the eleventh month. Here's the Python implementation:


"""


from fractions import Fraction

# Given values
章歲 = 700  # "章歲" (Zhang Sui)
朔月行定分 = 9000  # "朔月行定分" (Shuo Yue Xing Ding Fen)
朔日定小余 = 10000  # "朔日定小余" (Shuo Ri Ding Xiao Yu)
日法 = 20000  # "日法" (Ri Fa)
朔日夜半日所在度分 = Fraction(480, 1)  # "朔日夜半日所在度分" (Shuo Ri Ye Ban Ri Suo Zai Du Fen)

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder (余) by 朔日定小余
乘積 = 余 * 朔日定小余

# Step 3: Divide the product (乘積) by 日法 and compute the quotient and remainder
先行分 = 乘積 // 日法  # Quotient
先行分余 = 乘積 % 日法  # Remainder

# Step 4: Round the remainder (先行分余) to the nearest integer
if 先行分余 >= 日法 / 2:
    先行分 += 1

# Step 5: Compute 度分 (Du Fen) by dividing 先行分 by 日行分
度分 = 先行分

# Step 6: Subtract 度分 from 朔日夜半日所在度分
if 度分 <= 朔日夜半日所在度分:
    a = 朔日夜半日所在度分 - 度分
else:
    a = 朔日夜半日所在度分 + (360 - 度分)  # Add 360 degrees if 度分 exceeds the current position

# Final answer
a  # The position of the moon in degrees


"""


This code calculates the position of the moon (`a`) at midnight on the first day of the eleventh month, following the ancient Chinese method described in the problem. The result is stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 4630"""
