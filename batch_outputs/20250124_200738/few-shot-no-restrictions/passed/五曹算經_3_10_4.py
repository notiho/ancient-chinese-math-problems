"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席), which can seat 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 guests, divide by 23 people per mat, and the result is obtained.

Answer: *a* mats, with *b* people left over.
"""

# Total guests
總客人數 = 533680

# Guests per mat
每席客人數 = 23

# Divide to find the number of mats and the remainder
a = 總客人數 // 每席客人數  # Number of full mats
b = 總客人數 % 每席客人數   # Remaining guests

# Output: a mats, b people
a, b#----- content ends here -----

"""
"""
