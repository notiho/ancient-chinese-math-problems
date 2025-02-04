"""
今有負籠重一石一十七斤行七十六步五十返今負籠重一石行百步問返幾何
術曰以今所行步數乘今籠重斤數為法故籠重斤數乘故步又以返數乘之為實實如法得一返
荅曰 a返 
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin. The person carrying it walks 76 steps forward and 50 steps back.
Now, with a load weighing 1 shi, the person walks 100 steps forward.
Question: how many steps back does the person walk?

The procedure says: Multiply the current number of steps walked by the current load weight in jin to obtain the divisor.
Then multiply the previous load weight in jin by the previous number of steps, and also multiply it by the number of return steps to obtain the dividend.
Divide the dividend by the divisor to obtain the number of return steps.

Answer: *a* steps back.
"""

# 今負籠重一石一十七斤
今籠重 = 1 * 120 + 17  # 1 石 = 120 斤

# 行七十六步五十返
今步數 = 76
今返數 = 50

# 故負籠重一石
故籠重 = 1 * 120  # 1 石 = 120 斤

# 行百步
故步數 = 100

# 以今所行步數乘今籠重斤數為法
法 = 今步數 * 今籠重

# 故籠重斤數乘故步
實 = 故籠重 * 故步數

# 又以返數乘之
實 *= 今返數

# 實如法得一返
a = Fraction(實, 法)#----- content ends here -----

"""
"""
