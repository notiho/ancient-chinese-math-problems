"""
今有出錢五百七十六買竹七十八箇欲其大小率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a箇 箇 b錢 其 c箇 箇 d錢 
"""

"""
Suppose there is a total of 576 qian spent to buy 78 bamboo poles.
It is desired to determine the price of the larger and smaller poles based on their relative sizes.
Question: how many of each type, and how much does each cost?

The procedure for proportional rates says: Place the quantities of the items purchased (e.g., stones, jun, jin, liang) as the divisor.
Multiply the total money by the rate to obtain the dividend.
Divide the dividend by the divisor to determine the price per item.
If the dividend is less than the divisor, subtract the dividend from the divisor.
The divisor corresponds to the cheaper item, and the dividend corresponds to the more expensive item.

Answer: there are *a* poles at *b* qian each, and *c* poles at *d* qian each.
"""

# 出錢五百七十六
總錢數 = 576

# 買竹七十八箇
總竹數 = 78

# 假設大小竹的比例為 2:1
大竹率 = 2
小竹率 = 1

# 各置所買石鈞斤兩以為法 (以比例和為法)
法 = 大竹率 + 小竹率

# 以所率乘錢數為實 (計算大竹和小竹的總價)
大竹總價 = 大竹率 * 總錢數
小竹總價 = 小竹率 * 總錢數

# 實如法而一 (計算每箇的價格)
大竹單價 = Fraction(大竹總價, 法)
小竹單價 = Fraction(小竹總價, 法)

# 計算各自的數量
大竹數 = Fraction(總竹數 * 大竹率, 法)
小竹數 = Fraction(總竹數 * 小竹率, 法)

# 答案
a = 大竹數
b = 大竹單價
c = 小竹數
d = 小竹單價
"""
Variable 'a' has wrong value. Expected: 48, Actual: 52
Variable 'b' has wrong value. Expected: 7, Actual: 384
Variable 'c' has wrong value. Expected: 30, Actual: 26
Variable 'd' has wrong value. Expected: 8, Actual: 192"""
