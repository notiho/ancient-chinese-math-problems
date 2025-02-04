"""
又有席，一領坐客一十五人，有客四萬四千六百二十五人。問：席㡬何？
答曰： a領 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 15 people. There are 44,625 guests.
Question: how many mats are needed?

Answer: *a* mats.
"""

# 一領席可坐客 15 人
席容量 = 15

# 有客 44,625 人
客人數 = 44625

# 計算所需席數
a = Fraction(客人數, 席容量)  # 使用分數表示，確保精確計算

# 如果需要整數結果，可以取整數部分或進行進位（視需求而定）。#----- content ends here -----

"""
"""
