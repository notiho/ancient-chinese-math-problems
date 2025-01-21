"""
今有席一領坐客二十三人有客五十三萬三千六百八十人問席㡬何
術曰列五十三萬三千六百八十人以二十三人除之即得
答曰 a領 奇 b人 
"""

"""
Suppose there is 1 mat that can seat 23 people. There are 533,680 people.
Question: how many mats are needed?

The procedure says: Arrange 533,680 people and divide by 23 people. The result is obtained.

Answer: *a* mats, with *b* people left over.
"""

# 總人數
總人數 = 533680

# 每席可坐客數
每席人數 = 23

# 以二十三人除之，即得
a = 總人數 // 每席人數  # 整數部分，席數
b = 總人數 % 每席人數   # 餘數部分，剩餘人數
"""
"""
