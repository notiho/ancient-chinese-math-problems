"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a(=333/70)度 。
"""

#----- content starts here -----
"""
Suppose it is the first day of the eleventh month at midnight, and the sun is at 10 degrees and 480/700 of a degree in the constellation Dou.
Using the zhang-sui (章歲) as the base, the fixed movement of the new moon is 9000, the small remainder of the new moon is 10000, the solar divisor is 20000, and the zhang-sui is 700, also called the movement divisor.
Now, we do not consider adding the time or the sun's degree.
Question: At midnight on the first day of the month, where is the moon?

The procedure says:
1. Subtract the fixed movement of the new moon from the zhang-sui. Multiply the remainder by the small remainder of the new moon. Divide by the solar divisor to get the preliminary movement.
2. If there is a remainder, round up if it is greater than or equal to half the divisor; otherwise, discard it.
3. If the preliminary movement exceeds the solar movement divisor, divide by the solar movement divisor to get degrees and fractions. Subtract this from the sun's position at midnight on the first day.
4. If the degrees are insufficient to subtract, add the degrees of the previous constellation. If the fractions are insufficient to subtract, subtract one degree and convert it into fractions to complete the subtraction.
5. The remainder is the moon's position at midnight on the first day of the month.

Answer: It is at *a*(=333/70) degrees in the constellation Dou.
"""

from fractions import Fraction

# 定義已知數據
章歲 = 700
朔月行定分 = 9000
朔日定小余 = 10000
日法 = 20000
朔日夜半日所在度分 = Fraction(10 * 700 + 480, 700)  # 鬥10度7百分度之480

# 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# 余以乘朔日定小余
實 = 余 * 朔日定小余

# 滿日法而一，為先行分
先行分 = Fraction(實, 日法)

# 不盡者，半法已上收成一，已下者棄之
if 先行分.denominator > 1:
    if 先行分 - int(先行分) >= Fraction(1, 2):
        先行分 = int(先行分) + 1
    else:
        先行分 = int(先行分)

# 若先行分滿日行分而一，為度分
度分 = Fraction(先行分, 700)

# 以減朔日夜半日所在度分
月所在度分 = 朔日夜半日所在度分 - 度分

# 若度分不足減，加往宿度
if 月所在度分 < 0:
    月所在度分 += 10  # 假設往宿度為10度

# 余即朔日夜半月行所在度及分
a = 月所在度分  # 333/70#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 1163/70"""
