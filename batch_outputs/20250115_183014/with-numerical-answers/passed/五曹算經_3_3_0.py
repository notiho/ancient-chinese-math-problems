"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a(=3801/25)斛 。
"""

"""
Suppose there are 362 hu of unhusked millet.
Question: how much polished rice does it make?

The procedure says: Place 362 hu of millet, multiply it by 21 sheng, obtaining 7602 hu.
Divide it by 50, and the result is obtained.

Answer: *a*(=3801/25) hu.
"""

from fractions import Fraction

# 粟三百六十二斛
粟 = 362

# 以二十一升乘之
實 = 21 * 粟

# 得七千六百二斛，以五十除之即得
a = Fraction(實, 50)  # 3801/25

"""
"""
