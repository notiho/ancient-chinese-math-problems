"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a(=23203)領 奇 b(=11)人 。
"""

"""
Suppose there is a mat, one of which seats 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 guests, divide by 23 people, and the result is obtained.

Answer: *a*(=23203) mats, with *b*(=11) people left over.
"""

# 客五十三萬三千六百八十人
客人數 = 533680

# 一領坐客二十三人
每席人數 = 23

# 以二十三人除之即得
a = 客人數 // 每席人數  # 23203 mats
b = 客人數 % 每席人數   # 11 people left over
"""
"""
