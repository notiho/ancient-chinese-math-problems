"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 23 people. There are 533,680 guests.
Question: how many mats are needed, and how many people are left over?

Answer: *a* mats are needed, with *b* people left over.
"""

# One mat seats 23 people
席容量 = 23

# Total number of guests
客人數 = 533680

# Calculate the number of full mats needed
a = 客人數 // 席容量

# Calculate the number of leftover people
b = 客人數 % 席容量#----- content ends here -----

"""
"""
