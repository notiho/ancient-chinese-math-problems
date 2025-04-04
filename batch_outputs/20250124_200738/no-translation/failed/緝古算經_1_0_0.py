"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
To solve this problem, we will follow the procedure step by step and encode it into Python. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
章歲 = 700  # 章歲 (行分法)
朔月行定分 = 9000  # 朔月行定分
朔日定小余 = 10000  # 朔日定小余
日法 = 20000  # 日法
朔日夜半日所在度分 = Fraction(480, 1)  # 日在鬥十度七百分度之四百八十

# Step 1: 以章歲減朔月行定分
余 = 章歲 - 朔月行定分

# Step 2: 余以乘朔日定小余
先行分 = 余 * 朔日定小余

# Step 3: 滿日法而一
先行分 = Fraction(先行分, 日法)

# Step 4: 不盡者，半法已上收成一，已下者棄之
if 先行分.denominator > 1:  # Check if it's not a whole number
    if 先行分 - int(先行分) >= Fraction(1, 2):  # 半法已上收成一
        先行分 = int(先行分) + 1
    else:  # 已下者棄之
        先行分 = int(先行分)

# Step 5: 若先行分滿日行分而一，為度分
度分 = Fraction(先行分, 1)

# Step 6: 以減朔日夜半日所在度分
度分 -= 朔日夜半日所在度分

# Step 7: 若度分不足減，加往宿度
if 度分 < 0:
    度分 += 10  # 加往宿度 (一宿为10度)

# Step 8: 其分不足減者，退一度為行分而減之
if 度分 < 0:
    度分 += 1  # 退一度
    度分 -= Fraction(1, 1)  # 行分而减之

# Step 9: 余即朔日夜半月行所在度及分也
a = int(度分)  # 度
#----- content ends here -----


"""


### Final Answer:
The moon is at **a degrees** in the constellation 鬥 at the specified time.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: -4620"""
