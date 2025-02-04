"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a(=23203)領 奇 b(=11)人 。
"""

#----- content starts here -----
"""
Suppose there is a mat, and one mat accommodates 23 people. There are 533,680 people.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 people and divide by 23 people. The result is obtained.

Answer: *a*(=23,203) mats, with *b*(=11) people left over.
"""

# 客五十三萬三千六百八十人
總客數 = 533680

# 一領坐客二十三人
每席客數 = 23

# 以二十三人除之即得
a = 總客數 // 每席客數  # 23203 mats
b = 總客數 % 每席客數   # 11 people left over#----- content ends here -----

"""
"""
