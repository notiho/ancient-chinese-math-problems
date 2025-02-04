"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This problem involves ancient Chinese calendrical calculations to determine the position of the moon at midnight on the first day of the eleventh month. The procedure is described in detail, and we will translate it into Python step by step.


"""

#----- content starts here -----

from fractions import Fraction

# 天正十一月朔夜半，日在鬥十度七百分度之四百八十
日所在度 = 10  # 日在鬥十度
日所在分 = Fraction(480, 700)  # 七百分度之四百八十 (converted to a fraction)

# 定义常量
章歲 = 700  # 章歲亦名行分法
朔月行定分 = 9000  # 朔月行定分
朔日定小余 = 10000  # 朔日定小余
日法 = 20000  # 日法

# 術曰：以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# 余以乘朔日定小余
先行分 = 余 * 朔日定小余

# 滿日法而一，為先行分
先行分 = Fraction(先行分, 日法)

# 不盡者，半法已上收成一，已下者棄之
if 先行分.denominator > 1:
    if 先行分 - int(先行分) >= Fraction(1, 2):
        先行分 = int(先行分) + 1
    else:
        先行分 = int(先行分)

# 若先行分滿日行分而一，為度分
度分 = Fraction(先行分, 章歲)

# 以減朔日夜半日所在度分
月所在度 = 度分 - 日所在度

# 若度分不足減，加往宿度
if 月所在度 < 0:
    月所在度 += 12  # 一宿为12度

# 其分不足減者，退一度為行分而減之
if 月所在度 < 0:
    月所在度 += 1
    月所在分 = 章歲 - abs(月所在度)

# 答曰：在鬥 a度
a = 月所在度
print(f"在鬥 {a} 度")
#----- content ends here -----


"""
 

This Python code follows the ancient procedure step by step, using fractions to handle non-integer values and ensuring that all calculations adhere to the described method. The result will give the position of the moon at midnight on the specified date.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: -41/14"""
