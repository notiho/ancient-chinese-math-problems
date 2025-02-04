"""
今有客不知其數兩人共盤少兩盤三人共盤長三盤問客及盤㡬何
術曰以二乗少盤三乗長盤倂之為盤數倍之又以二乗少盤數增之得人數
答曰客 a人 b盤
"""

#----- content starts here -----
"""
Suppose there are guests, but their number is unknown.
Two people share one less than the total number of plates.
Three people share three more than the total number of plates.
Question: how many guests and how many plates are there?

The procedure says: Square 2 and multiply it by the number of plates less by 2.
Square 3 and multiply it by the number of plates more by 3.
Add these together to obtain the total number of plates.
Double this result.
Then, square 2 and multiply it by the number of plates less by 2, and add this to the total number of plates.
This gives the total number of guests.

Answer: there are *a* guests and *b* plates.
"""

# 少盤數
少盤 = -2

# 長盤數
長盤 = 3

# 以二乘少盤
少盤項 = (2**2) * 少盤

# 以三乘長盤
長盤項 = (3**2) * 長盤

# 倂之為盤數
盤數 = 少盤項 + 長盤項

# 倍之
盤數 *= 2

# 又以二乘少盤數增之
人數 = (2**2) * 少盤 + 盤數

# 答
a = 人數
b = 盤數#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 13, Actual: 38"""
