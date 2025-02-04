"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin. The person carrying it walks 76 steps and returns 50 times.
Now, with a load weighing 1 shi, the person walks 100 steps.
Question: how many returns does the person make?

The procedure says: Multiply the current number of steps walked by the current load weight in jin to obtain the divisor.
Then, multiply the former load weight in jin by the former steps walked, and also multiply it by the number of returns, to obtain the dividend.
Divide the dividend by the divisor to obtain the number of returns.

Answer: *a* returns.
"""

# 負籠重一石一十七斤
故籠重 = 1 * 120 + 17  # 1石 = 120斤

# 行七十六步
故步數 = 76

# 五十返
故返數 = 50

# 今負籠重一石
今籠重 = 1 * 120  # 1石 = 120斤

# 行百步
今步數 = 100

# 以今所行步數乘今籠重斤數為法
法 = 今步數 * 今籠重

# 故籠重斤數乘故步，又以返數乘之，為實
實 = 故籠重 * 故步數 * 故返數

# 實如法得一返
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
