"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is a mat, and one mat accommodates 23 people. There are 533,680 people.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 people and divide by 23 people per mat to obtain the result.

Answer: *a* mats and *b* leftover people.
"""

# Total number of people
總人數 = 533680

# Number of people per mat
每席人數 = 23

# Calculate the number of full mats
a = 總人數 // 每席人數

# Calculate the leftover people
b = 總人數 % 每席人數

# Output: a mats and b people
a, b#----- content ends here -----

"""
"""
