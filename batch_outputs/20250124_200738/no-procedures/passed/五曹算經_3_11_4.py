"""
又有席，一領坐客一十五人，有客四萬四千六百二十五人。問：席㡬何？
答曰： a領 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 15 people. There are 44,625 guests.
Question: how many mats are required?

Answer: *a* mats.
"""

# 一領席坐客 15 人
席容量 = 15

# 客人總數 44,625 人
客人總數 = 44625

# 計算所需席數
a = Fraction(客人總數, 席容量)  # 使用 Fraction 表示可能的分數結果

# 如果需要整數席數，可以向上取整
# a = (客人總數 + 席容量 - 1) // 席容量#----- content ends here -----

"""
"""
