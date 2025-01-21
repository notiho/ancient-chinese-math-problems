"""
今有負籠重一石一十七斤行七十六步五十返今負籠重一石行百步問返幾何
術曰以今所行步數乘今籠重斤數為法故籠重斤數乘故步又以返數乘之為實實如法得一返
荅曰 a返 
"""

"""
Suppose there is a load weighing 1 shi and 17 jin. It is carried for 76 steps and returned 50 times.
Now, with a load weighing 1 shi, it is carried for 100 steps.
Question: how many returns are made?

The procedure says: Multiply the current number of steps by the current load weight in jin to obtain the divisor.
Then, multiply the previous load weight in jin by the previous number of steps, and also multiply it by the number of returns to obtain the dividend.
Divide the dividend by the divisor to obtain the number of returns.

The answer says: *a* returns.
"""

# 今負籠重一石一十七斤
今籠重 = 1 * 120 + 17  # 1石 = 120斤

# 行七十六步
今步數 = 76

# 五十返
今返數 = 50

# 故負籠重一石
故籠重 = 1 * 120  # 1石 = 120斤

# 行百步
故步數 = 100

# 以今所行步數乘今籠重斤數為法
法 = 今步數 * 今籠重

# 故籠重斤數乘故步
實 = 故籠重 * 故步數

# 又以返數乘之
實 *= 今返數

# 實如法得一返
a = Fraction(實, 法)
"""
"""
