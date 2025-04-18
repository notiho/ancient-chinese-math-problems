"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

"""

"""


from fractions import Fraction

# 錢二百三十八貫五百七十三文足
錢 = 238 * 1000 + 573  # 1貫 = 1000文

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
結果 = Fraction(錢, 陌)

# 得貫數和餘文數
a = 結果.numerator // 結果.denominator  # 貫數
b = 結果.numerator % 結果.denominator  # 餘文數


"""

"""


"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2593
Variable 'b' has wrong value. Expected: 22/5, Actual: 17"""
