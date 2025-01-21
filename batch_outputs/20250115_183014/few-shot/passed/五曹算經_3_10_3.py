"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

"""
Suppose there is one mat, which can seat 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 guests, divide by 23 people, and the result is obtained.

Answer: *a* mats with *b* people left over.
"""

# 一領坐客二十三人
席容量 = 23

# 有客五十三萬三千六百八十人
客人數 = 533680

# 以二十三人除之即得
a = 客人數 // 席容量  # Number of full mats
b = 客人數 % 席容量   # Remaining people
"""
"""
