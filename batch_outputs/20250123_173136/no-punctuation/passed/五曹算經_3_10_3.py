"""
今有席一領坐客二十三人有客五十三萬三千六百八十人問席㡬何
術曰列五十三萬三千六百八十人以二十三人除之即得
答曰 a領 奇 b人 
"""

"""
Suppose there is one mat that accommodates 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 guests and divide by 23 people. The result is obtained.

Answer: *a* mats, with *b* people remaining.
"""

# 客五十三萬三千六百八十人
客人數 = 533680

# 坐客二十三人
每席人數 = 23

# 以二十三人除之
a = 客人數 // 每席人數  # Number of full mats
b = 客人數 % 每席人數   # Remaining people
"""
"""
