"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 23 people. There are 533,680 guests.
Question: how many mats are needed, and how many people will be left without a seat?

Answer: *a* mats and *b* people left.
"""

# 每席可坐客
每席客 = 23

# 總客數
總客 = 533680

# 計算席數
a = 總客 // 每席客  # 整數部分，表示完整的席數

# 計算剩餘人數
b = 總客 % 每席客  # 餘數部分，表示剩餘無法坐下的人數

# a 領奇 b 人
a, b#----- content ends here -----

"""
"""
