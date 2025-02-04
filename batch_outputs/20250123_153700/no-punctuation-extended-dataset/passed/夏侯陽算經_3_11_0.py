"""
今有絹一匹當腳一十五文問丈尺寸各幾何
術曰置腳價一十五文以四丈除之得一丈腳數退一等得尺再退得寸腳數
答曰丈 a文 尺 b分 寸 c氂
"""

"""
Suppose there is one bolt of silk worth 15 wen per bolt.
Question: how much is the value per zhang, chi, and cun?

The procedure says: Place the value of the bolt, 15 wen.
Divide it by 4 zhang, obtaining the value per zhang.
Decrease the value by one level to get the value per chi.
Decrease it again to get the value per cun.

Answer: *a* wen per zhang, *b* fen per chi, and *c* li per cun.
"""

from fractions import Fraction

# 絹一匹當腳一十五文
腳價 = 15  # in wen

# 以四丈除之，得一丈腳數
丈價 = Fraction(腳價, 4)

# 退一等，得尺
尺價 = 丈價 / 10  # 1 zhang = 10 chi

# 再退，得寸
寸價 = 尺價 / 10  # 1 chi = 10 cun

# 答案
a = 丈價  # 丈價 in wen
b = 尺價 * 10  # 尺價 in fen (1 wen = 10 fen)
c = 寸價 * 100  # 寸價 in li (1 wen = 100 li)
"""
"""
