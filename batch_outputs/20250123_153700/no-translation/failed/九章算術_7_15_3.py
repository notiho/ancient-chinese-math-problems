"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""

"""


# 玉方一寸，重七兩
玉重每寸 = 7

# 石方一寸，重六兩
石重每寸 = 6

# 石立方三寸，中有玉，并重十一斤
總重 = 11 * 16  # 轉換為兩
總體積 = 3

# 假令皆玉，多十三兩
假皆玉 = 玉重每寸 * 總體積
多重 = 假皆玉 - 總重  # 多十三兩

# 令之皆石，不足十四兩
假皆石 = 石重每寸 * 總體積
不足重 = 總重 - 假皆石  # 不足十四兩

# 不足為玉，多為石
# 設玉體積為 x，石體積為 (3 - x)
# 玉重 + 石重 = 總重
# 7x + 6(3 - x) = 總重
# 解方程得 x
from fractions import Fraction

玉體積 = Fraction(不足重, 多重 + 不足重) * 總體積
石體積 = 總體積 - 玉體積

# 各以一寸之重乘之，得玉石之積重
玉重 = 玉體積 * 玉重每寸
石重 = 石體積 * 石重每寸

# 結果
a = 玉體積
b = Fraction(玉重, 16)  # 轉換為斤
c = 石體積
d = Fraction(石重, 16)  # 轉換為斤


"""

"""


"""
Variable 'a' has wrong value. Expected: 14, Actual: 158
Variable 'b' has wrong value. Expected: 49/8, Actual: 553/8
Variable 'c' has wrong value. Expected: 13, Actual: -155
Variable 'd' has wrong value. Expected: 39/8, Actual: -465/8"""
