"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

"""
Suppose there is one mat, which accommodates 23 people. There are 533,680 guests.
Question: how many mats are required?

The procedure says: Arrange the 533,680 guests, and divide by 23 people. The quotient is the number of mats, and the remainder is the number of extra people.

Answer: *a* mats and *b* people.
"""

# 一領坐客二十三人
每席容納人數 = 23

# 有客五十三萬三千六百八十人
總客數 = 533680

# 以二十三人除之即得
a = 總客數 // 每席容納人數  # Mats required
b = 總客數 % 每席容納人數   # Remaining people
"""
"""
