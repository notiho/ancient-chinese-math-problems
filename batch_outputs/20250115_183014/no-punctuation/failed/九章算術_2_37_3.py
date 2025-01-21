"""
今有出錢五百七十六買竹七十八箇欲其大小率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a箇 箇 b錢 其 c箇 箇 d錢 
"""

"""
Suppose there is a total of 576 qian spent to buy 78 bamboo poles. It is desired to determine the price ratio of the larger and smaller poles and how many of each type were purchased.

The procedure says: Place the quantities of the larger and smaller poles as the divisor.
Multiply the total money spent by the ratio to obtain the dividend.
Divide the dividend by the divisor to determine the price per pole.
If the remainder is less than the divisor, subtract the remainder from the divisor.
The divisor corresponds to the cheaper poles, and the dividend corresponds to the more expensive poles.

Answer: *a* poles at *b* qian each, and *c* poles at *d* qian each.
"""

# 出錢五百七十六
總錢 = 576

# 買竹七十八箇
總竹 = 78

# 假設大小竹的比例為 2:1
大竹率 = 2
小竹率 = 1

# 各置所買石鈞斤兩以為法
法 = 大竹率 + 小竹率

# 以所率乘錢數為實
大竹實 = 總錢 * 大竹率
小竹實 = 總錢 * 小竹率

# 實如法而一
大竹每箇錢 = Fraction(大竹實, 法)
小竹每箇錢 = Fraction(小竹實, 法)

# 計算大竹和小竹的數量
大竹數量 = Fraction(總竹 * 大竹率, 法)
小竹數量 = Fraction(總竹 * 小竹率, 法)

# 結果
a = 大竹數量
b = 大竹每箇錢
c = 小竹數量
d = 小竹每箇錢
"""
Variable 'a' has wrong value. Expected: 48, Actual: 52
Variable 'b' has wrong value. Expected: 7, Actual: 384
Variable 'c' has wrong value. Expected: 30, Actual: 26
Variable 'd' has wrong value. Expected: 8, Actual: 192"""
