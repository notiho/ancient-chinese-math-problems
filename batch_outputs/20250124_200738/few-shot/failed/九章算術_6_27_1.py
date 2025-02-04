"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints. 
At the first checkpoint, for every 2 jin, 1 jin is taxed.
At the second checkpoint, for every 3 jin, 1 jin is taxed.
At the third checkpoint, for every 4 jin, 1 jin is taxed.
At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
At the fifth checkpoint, for every 6 jin, 1 jin is taxed.
The total tax collected across the five checkpoints equals exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin [the total tax], and multiply it by the product of all the tax rates to obtain the dividend.
Also, subtract the product of all the non-taxed parts from the total product to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a* jin.
"""

# Tax rates for each checkpoint
稅率_前關 = Fraction(1, 2)
稅率_次關1 = Fraction(1, 3)
稅率_次關2 = Fraction(1, 4)
稅率_次關3 = Fraction(1, 5)
稅率_次關4 = Fraction(1, 6)

# Non-taxed rates for each checkpoint
不稅率_前關 = 1 - 稅率_前關
不稅率_次關1 = 1 - 稅率_次關1
不稅率_次關2 = 1 - 稅率_次關2
不稅率_次關3 = 1 - 稅率_次關3
不稅率_次關4 = 1 - 稅率_次關4

# Total tax collected
總稅 = 1

# 通所稅者以乘之為實
所稅乘積 = 稅率_前關 * 稅率_次關1 * 稅率_次關2 * 稅率_次關3 * 稅率_次關4
實 = 總稅 * 所稅乘積

# 亦通其不稅者以減所通，餘為法
所不稅乘積 = 不稅率_前關 * 不稅率_次關1 * 不稅率_次關2 * 不稅率_次關3 * 不稅率_次關4
法 = 所不稅乘積 - 所稅乘積

# 實如法得一斤
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 1/119"""
