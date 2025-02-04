"""
今有客不知其數兩人共盤少兩盤三人共盤長三盤問客及盤㡬何
術曰以二乗少盤三乗長盤倂之為盤數倍之又以二乗少盤數增之得人數
答曰客 a人 b盤
"""

#----- content starts here -----
"""
Suppose there are guests, but their number is unknown.
Two people share one less than the total number of plates, and three people share three more than the total number of plates.
Question: how many guests and how many plates are there?

The procedure says: Square 2 and multiply it by the number of plates less by 1. 
Square 3 and multiply it by the number of plates more by 3. Add these together to get the total number of plates.
Double this result. Then, square 2 and multiply it by the total number of plates, and add this to the result to get the total number of people.

Answer: there are *a* guests and *b* plates.
"""

# Initialize the given conditions
少盤 = -1  # Two people share one less than the total plates
長盤 = 3   # Three people share three more than the total plates

# 以二乘少盤
二 = 2
少盤項 = 二**2 * 少盤

# 三乘長盤
三 = 3
長盤項 = 三**2 * 長盤

# 倂之為盤數
盤數 = 少盤項 + 長盤項

# 倍之
盤數 *= 2

# 又以二乘少盤數增之
人數 = 二**2 * 盤數 + 盤數

# Final results
a = 人數
b = 盤數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 30, Actual: 230
Variable 'b' has wrong value. Expected: 13, Actual: 46"""
