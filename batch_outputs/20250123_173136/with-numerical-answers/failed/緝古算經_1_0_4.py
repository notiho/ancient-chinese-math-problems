"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a(=333/70)度 。
"""

"""
Suppose it is the first day of the eleventh month at midnight. The sun is at 10 degrees and 480/7000 of a degree in the constellation Dou.
Using the "Zhang Sui" (a calendrical system) as the base:
- The fixed motion of the new moon is 9000.
- The small remainder of the new moon is 10000.
- The solar divisor is 20000.
- The Zhang Sui divisor is 700, also called the motion divisor.

We do not consider additional time or solar motion. 
Question: At midnight on the first day of the eleventh month, where is the moon located?

The procedure says:
1. Subtract the fixed motion of the new moon from the Zhang Sui divisor. Multiply the remainder by the small remainder of the new moon.
2. Divide the product by the solar divisor. The quotient is the "initial motion fraction."
3. If there is a remainder, round up if it is greater than or equal to half the divisor; otherwise, discard it.
4. If the "initial motion fraction" exceeds the solar motion fraction, convert it into degrees and fractions.
5. Subtract this from the sun's position at midnight on the first day. If the degrees are insufficient to subtract, add the degrees of the previous constellation.
6. If the fractions are insufficient to subtract, borrow one degree (converted into fractions) and subtract.
7. The remainder is the moon's position at midnight on the first day.

Answer: It is in Dou at *a*(=333/70) degrees.
"""

from fractions import Fraction

# 定義常數
章歲 = 700  # Zhang Sui divisor
朔月行定分 = 9000  # Fixed motion of the new moon
朔日定小余 = 10000  # Small remainder of the new moon
日法 = 20000  # Solar divisor
朔日夜半日所在度分 = Fraction(10 * 7000 + 480, 7000)  # Sun's position at midnight (10 degrees and 480/7000)

# 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# 余以乘朔日定小余
乘積 = 余 * 朔日定小余

# 滿日法而一，為先行分
先行分 = Fraction(乘積, 日法)

# 不盡者，半法已上收成一，已下者棄之
if 乘積 % 日法 >= 日法 / 2:
    先行分 = 先行分.numerator // 1 + 1
else:
    先行分 = 先行分.numerator // 1

# 若先行分滿日行分而一，為度分
度分 = Fraction(先行分, 7000)

# 以減朔日夜半日所在度分
月所在度分 = 朔日夜半日所在度分 -
"""
Code error: invalid syntax (<string>, line 53)"""
