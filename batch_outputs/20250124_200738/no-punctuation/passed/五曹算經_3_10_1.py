"""
今有席一領坐客二十三人有客五十三萬三千六百八十人問席㡬何
術曰列五十三萬三千六百八十人以二十三人除之即得
答曰 a領 奇 b人 
"""

#----- content starts here -----
"""
Suppose there is one mat that can seat 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange 533,680 guests and divide by 23 people. The quotient is the number of mats, and the remainder is the number of leftover people.

Answer: *a* mats, with *b* people left over.
"""

# 客五十三萬三千六百八十人
客人數 = 533680

# 坐客二十三人
每席人數 = 23

# 以二十三人除之，即得
a = 客人數 // 每席人數  # Number of mats
b = 客人數 % 每席人數   # Leftover people#----- content ends here -----

"""
"""
