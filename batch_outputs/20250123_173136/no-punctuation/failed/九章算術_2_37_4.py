"""
今有出錢五百七十六買竹七十八箇欲其大小率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a箇 箇 b錢 其 c箇 箇 d錢 
"""

"""
Suppose there is a total of 576 qian spent to buy 78 bamboo poles. It is desired to determine the price ratio of large and small poles and how many of each were purchased.

The procedure for ratios says: Place the quantities of large and small poles as the divisor.
Multiply the total money by the respective ratios to obtain the dividend.
Divide the dividend by the divisor to calculate the number of poles.
If there is a remainder (less than the divisor), adjust by subtracting the remainder from the divisor.
The cheaper corresponds to the divisor, and the more expensive corresponds to the dividend.

Answer: *a* large poles at *b* qian each, and *c* small poles at *d* qian each.
"""

# 出錢五百七十六
總錢數 = 576

# 買竹七十八箇
總竹數 = 78

# 假設大竹與小竹的價格比例為 2:1
大竹率 = 2
小竹率 = 1

# 各置所買石鈞斤兩以為法
法 = 大竹率 + 小竹率

# 以所率乘錢數為實
大竹實 = 大竹率 * 總錢數
小竹實 = 小竹率 * 總錢數

# 實如法而一
大竹價格 = Fraction(大竹實, 法)
小竹價格 = Fraction(小竹實, 法)

# 計算大竹與小竹的數量
大竹數量 = Fraction(總竹數 * 大竹率, 法)
小竹數量 = Fraction(總竹數 * 小竹率, 法)

# 答案
a = 大竹數量
b = 大竹價格
c = 小竹數量
d = 小竹價格
"""
Variable 'a' has wrong value. Expected: 48, Actual: 52
Variable 'b' has wrong value. Expected: 7, Actual: 384
Variable 'c' has wrong value. Expected: 30, Actual: 26
Variable 'd' has wrong value. Expected: 8, Actual: 192"""
