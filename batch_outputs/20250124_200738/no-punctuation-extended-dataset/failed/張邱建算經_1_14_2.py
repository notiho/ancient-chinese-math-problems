"""
今有客不知其數兩人共盤少兩盤三人共盤長三盤問客及盤㡬何
術曰以二乗少盤三乗長盤倂之為盤數倍之又以二乗少盤數增之得人數
答曰客 a人 b盤
"""

#----- content starts here -----
"""
Suppose there are guests, but their number is unknown. 
Two people share one fewer plate, and three people share one more plate.
Question: how many guests and plates are there?

The procedure says: Square 2 and multiply it by the fewer plates. 
Square 3 and multiply it by the longer plates. 
Add these together to get the number of plates. 
Double this. 
Then square 2 and multiply it by the fewer plates, adding this to the plate count to get the number of people.

Answer: there are *a* guests and *b* plates.
"""

# 少盤
少盤 = 2

# 長盤
長盤 = 3

# 以二乘少盤
二乘少盤 = 2**2 * 少盤

# 三乘長盤
三乘長盤 = 3**2 * 長盤

# 倂之為盤數
盤數 = 二乘少盤 + 三乘長盤

# 倍之
盤數倍 = 2 * 盤數

# 又以二乘少盤數增之得人數
人數 = 二乘少盤 + 盤數倍

a = 人數
b = 盤數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 30, Actual: 78
Variable 'b' has wrong value. Expected: 13, Actual: 35"""
