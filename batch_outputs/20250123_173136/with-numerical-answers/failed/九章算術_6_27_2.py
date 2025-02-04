"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a(=6/5)斤 。
"""

"""
Suppose a person carries gold through five checkpoints. 
At the first checkpoint, for every 2 jin, 1 jin is taxed. 
At the second checkpoint, for every 3 jin, 1 jin is taxed. 
At the third checkpoint, for every 4 jin, 1 jin is taxed. 
At the fourth checkpoint, for every 5 jin, 1 jin is taxed. 
At the fifth checkpoint, for every 6 jin, 1 jin is taxed. 
The total tax across all five checkpoints amounts to exactly 1 jin. 
Question: how much gold was originally carried?

The procedure says: Place 1 jin [the total tax], and multiply it by the product of all the tax rates to get the dividend. 
Also, multiply the product of all the non-taxed portions to subtract from the total product, and the remainder is the divisor. 
Divide the dividend by the divisor to get the original amount of gold.

Answer: *a*(=6/5) jin.
"""

# 稅率：前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一
稅率 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# 不稅率：1 - 稅率
不稅率 = [1 - rate for rate in 稅率]

# 置一斤
稅總 = 1

# 通所稅者以乘之為實
實 = 稅總
for rate in 稅率:
    実 = 實 * rate

# 亦通其不稅者以減所通，餘為法
法 = 1
for rate in 不稅率:
  
"""
Code error: expected an indented block after 'for' statement on line 35 (<string>, line 36)"""
