"""
今有席一領坐客二十三人有客五十三萬三千六百八十人問席㡬何
術曰列五十三萬三千六百八十人以二十三人除之即得
答曰 a領 奇 b人 
"""

#----- content starts here -----
"""
Suppose there is one mat that can seat 23 people. There are 533,680 people.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 people and divide by 23 people. The quotient is the number of mats, and the remainder is the number of extra people.

Answer: *a* mats, with *b* people left over.
"""

# 總客數
總客數 = 533680

# 每席可坐客數
每席客數 = 23

# 以二十三人除之，即得
a = 總客數 // 每席客數  # Mats (quotient)
b = 總客數 % 每席客數   # Remaining people (remainder)#----- content ends here -----

"""
"""
