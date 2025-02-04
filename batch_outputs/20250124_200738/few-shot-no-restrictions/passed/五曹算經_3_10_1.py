"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席), which can seat 23 people. There are 533,680 guests.
Question: how many mats are required?

The procedure says: Place the number of guests, 533,680, and divide it by 23 people per mat to obtain the result.

Answer: *a* mats with *b* people left over.
"""

# Total number of guests
總客數 = 533680

# Number of people per mat
每席人數 = 23

# Calculate the number of full mats
a = 總客數 // 每席人數

# Calculate the remaining people
b = 總客數 % 每席人數

# Output: a mats, b people left over
a, b#----- content ends here -----

"""
"""
