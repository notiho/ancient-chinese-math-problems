"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a(=333/70)度 。
"""

"""
Suppose it is the first day of the eleventh month at midnight, and the sun is at 10 degrees and 480/700 of a degree in the constellation Dou.
Using the zhang-sui (章歲) as the base, the fixed motion of the new moon is 9000, the fixed minor remainder of the new moon is 10000, the solar divisor is 20000, and the zhang-sui is 700, also known as the divisor of motion.
Now, we do not consider adding time or solar degrees.
Question: At midnight on the first day of the month, where is the moon?

The procedure says: Subtract the fixed motion of the new moon from the zhang-sui. Multiply the remainder by the fixed minor remainder of the new moon. Divide by the solar divisor to get the initial motion. If there is a remainder, round up if it is greater than or equal to half the divisor, and discard it otherwise.
If the initial motion reaches the solar motion divisor, convert it into degrees and fractions. Subtract the degrees and fractions from the sun's position at midnight on the first day of the month. If the degrees are insufficient for subtraction, add the degrees of the previous constellation. If the fractions are insufficient for subtraction, borrow one degree and convert it into fractions for subtraction. The remainder is the moon's position at midnight on the first day of the month.

Answer: It is at *a*(=333/70) degrees in the constellation Dou.
"""

from fractions import Fraction

# 定義給定數據
章歲 = 700
朔月行定分 = 9000
朔日定小余 = 10000
日法 = 20000
朔日夜半日所在度分 = Fraction(10 * 700 + 480, 700)  # 鬥10度7百分度之480/700

# 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# 余以乘朔日定小余
初行分 = 余 * 朔日定小余

# 滿日法而一
初行分 = Fraction(初行分, 日法)

# 半法已上收成一，已下者棄之
if 初行分.denominator == 1:  # 如果是整數，直接取值
    初行分 = int(初行分)
else:
    if 初行分 - int(初行分) >= Fraction(1, 2):
        初行分 = int(初行分) + 1
    else:
        初行分 = int(初行分)

# 若先行分滿日行分而一，為度分
度分 = Fraction(初行分, 1)

# 以減朔日夜半日所在度分
月所在度分 = 朔日夜半日所在度分 - 度分

# 若度分不足減，加往宿度
if 月所在度分 < 0:
    月所在度分 += 700  # 加往宿度

# 余即朔日夜半月行所在度及分
a = 月所在度分  # 333/70
"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 145624/35"""
