"""
今有絲三百二十四斤欲九兩為絹一匹問絹幾何
術曰置絲斤數二而八之以九而一即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 324 jin of silk, and it is desired to make one bolt of silk cloth for every 9 liang.
Question: how many bolts of silk cloth can be made?

The procedure says: Place the number of jin of silk, multiply it by 2 and then by 8, and divide it by 9 to obtain the result.

Answer: *a* bolts.
"""

# 絲三百二十四斤
絲斤數 = 324

# 置絲斤數，二而八之
絲轉兩 = 絲斤數 * 2 * 8

# 以九而一，即得
a = Fraction(絲轉兩, 9)#----- content ends here -----

"""
"""
