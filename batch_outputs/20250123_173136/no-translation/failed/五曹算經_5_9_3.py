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
每陌錢 = Fraction(錢, 陌)

# 轉換為貫與文
a = 每陌錢 // 1000  # 貫
b = 每陌錢 % 1000  # 文


"""

"""


"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
