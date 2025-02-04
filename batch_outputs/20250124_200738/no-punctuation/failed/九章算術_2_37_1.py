"""
今有出錢五百七十六買竹七十八箇欲其大小率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a箇 箇 b錢 其 c箇 箇 d錢 
"""

#----- content starts here -----
"""
Suppose there is 576 qian (money) used to buy 78 bamboo poles. It is desired to determine the price ratio of large and small poles and how many of each were bought.

The procedure for ratios says: Place the quantities of what is bought (e.g., large and small poles) as the divisor.
Multiply the money by the ratio to obtain the dividend.
Divide the dividend by the divisor to obtain the result.
If the result is not a whole number, adjust by subtracting the divisor from the dividend.
The divisor corresponds to the cheaper item, and the dividend corresponds to the more expensive item.

Answer: *a* large poles at *b* qian each, and *c* small poles at *d* qian each.
"""

# 出錢五百七十六
錢數 = 576

# 買竹七十八箇
竹數 = 78

# 假設大竹與小竹的比例為 2:1
大竹率 = 2
小竹率 = 1

# 各置所買石鈞斤兩以為法
法 = 大竹率 + 小竹率

# 以所率乘錢數為實
大竹實 = 大竹率 * 錢數
小竹實 = 小竹率 * 錢數

# 實如法而一
大竹單價 = Fraction(大竹實, 法)
小竹單價 = Fraction(小竹實, 法)

# 計算大竹與小竹的數量
a = Fraction(竹數 * 大竹率, 法)
b = 大竹單價
c = Fraction(竹數 * 小竹率, 法)
d = 小竹單價#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 48, Actual: 52
Variable 'b' has wrong value. Expected: 7, Actual: 384
Variable 'c' has wrong value. Expected: 30, Actual: 26
Variable 'd' has wrong value. Expected: 8, Actual: 192"""
