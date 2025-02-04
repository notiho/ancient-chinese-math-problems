"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a(=150000/2603)返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin, carried for 76 steps, with 50 returns.
Now, with a load weighing 1 shi, carried for 100 steps, how many returns are required?

The procedure says: Multiply the current number of steps by the current load weight in jin to obtain the divisor.
Then, multiply the previous load weight in jin by the previous number of steps, and also multiply it by the number of returns to obtain the dividend.
Divide the dividend by the divisor to obtain the number of returns.

Answer: *a*(=150000/2603) returns.
"""

# 負籠重一石一十七斤
故籠重 = 1 * 120 + 17  # 1 石 = 120 斤

# 行七十六步
故步 = 76

# 五十返
故返 = 50

# 今負籠重一石
今籠重 = 1 * 120  # 1 石 = 120 斤

# 行百步
今步 = 100

# 以今所行步數乘今籠重斤數為法
法 = 今步 * 今籠重

# 故籠重斤數乘故步，又以返數乘之，為實
實 = 故籠重 * 故步 * 故返

# 實如法得一返
a = Fraction(實, 法)  # 150000/2603 returns#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
