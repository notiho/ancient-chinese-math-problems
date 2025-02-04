"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a(=23203)領 奇 b(=11)人 。
"""

#----- content starts here -----
"""
Suppose there is a mat, and one mat accommodates 23 guests. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange the number 533,680 guests, divide it by 23 guests, and the result is obtained.

Answer: *a*(=23,203) mats, with *b*(=11) guests remaining.
"""

# 客五十三萬三千六百八十人
客人數 = 533680

# 一領坐客二十三人
每席客人數 = 23

# 以二十三人除之即得
a = 客人數 // 每席客人數  # 23203 mats
b = 客人數 % 每席客人數   # 11 guests remaining#----- content ends here -----

"""
"""
