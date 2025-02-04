"""
今有出錢五百七十六買竹七十八箇欲其大小率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a箇 箇 b錢 其 c箇 箇 d錢 
"""

#----- content starts here -----
"""
Suppose there is a total of 576 qian spent to buy 78 bamboo pieces. It is desired to divide them into large and small pieces according to their respective rates.
Question: how many large and small pieces are there, and how much does each cost?

The procedure says: Place the respective rates of large and small pieces (in terms of their weights or values) as the divisor.
Multiply the total money spent by the respective rates to obtain the dividend.
Divide the dividend by the divisor to determine the number of pieces.
If there is a remainder (not fully divisible), subtract the remainder from the divisor.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: There are *a* large pieces, each costing *b* qian. There are *c* small pieces, each costing *d* qian.
"""

# 出錢五百七十六
總錢數 = 576

# 買竹七十八箇
總竹數 = 78

# 大竹與小竹的率 (假設大竹率為 3，小竹率為 2)
大竹率 = 3
小竹率 = 2

# 以率為法
法 = 大竹率 + 小竹率

# 以所率乘錢數為實
大竹實 = 大竹率 * 總錢數
小竹實 = 小竹率 * 總錢數

# 實如法而一
大竹錢 = Fraction(大竹實, 法)
小竹錢 = Fraction(小竹實, 法)

# 計算大竹和小竹的數量
a = Fraction(大竹錢, 大竹率)
c = Fraction(小竹錢, 小竹率)

# 每箇的價格
b = 大竹率
d = 小竹率#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 48, Actual: 576/5
Variable 'b' has wrong value. Expected: 7, Actual: 3
Variable 'c' has wrong value. Expected: 30, Actual: 576/5
Variable 'd' has wrong value. Expected: 8, Actual: 2"""
