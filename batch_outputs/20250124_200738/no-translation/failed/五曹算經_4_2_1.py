"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a斛 粟主 b斛 。
"""

"""

"""

#----- content starts here -----

# 粟七百斛
粟 = 700

# 每一斛雇七升
雇粟 = Fraction(7, 10)  # 7升 = 7/10斛

# 以雇粟乘粟，得車粟
車粟 = 粟 * 雇粟

# 減本粟七百斛，餘為主粟
主粟 = 粟 - 車粟

# 答案
a = 車粟
b = 主粟
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
