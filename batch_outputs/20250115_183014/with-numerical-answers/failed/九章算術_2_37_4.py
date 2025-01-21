"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=48)箇 ，箇 b(=7)錢 。其 c(=30)箇 ，箇 d(=8)錢 。
"""

"""
Suppose there is an expenditure of 576 qian to buy 78 bamboo pieces. It is desired to divide them into large and small pieces proportionally.
Question: how many of each size, and at what price per piece?

The procedure for proportional division says: Place the respective quantities of shi, jun, jin, and liang (or other proportional factors) as the divisor.
Multiply the proportional factor by the total money spent to obtain the dividend.
Divide the dividend by the divisor to obtain the result for each category.
If the dividend does not fully divide by the divisor, subtract the remainder from the divisor. The divisor corresponds to the cheaper category, and the dividend corresponds to the more expensive category.

Answer: There are *a*(=48) large pieces, each costing *b*(=7) qian. There are *c*(=30) small pieces, each costing *d*(=8) qian.
"""

# 出錢五百七十六
總錢 = 576

# 買竹七十八箇
總竹 = 78

# 大竹比例
大竹率 = 7

# 小竹比例
小竹率 = 8

# 各置所買石、鈞、斤、兩以為法
法 = 大竹率 + 小竹率

# 以所率乘錢數為實
大竹實 = 大竹率 * 總錢
小竹實 = 小竹率 * 總錢

# 實如法而一
大竹錢 = Fraction(大竹實, 法)
小竹錢 = Fraction(小竹實, 法)

# 算出數量
a = Fraction(總竹 * 大竹率, 法)  # 48
b = 大竹錢 / a  # 7

c = Fraction(總竹 * 小竹率, 法)  # 30
d = 小竹錢 / c  # 8
"""
Variable 'a' has wrong value. Expected: 48, Actual: 182/5
Variable 'b' has wrong value. Expected: 7, Actual: 96/13
Variable 'c' has wrong value. Expected: 30, Actual: 208/5
Variable 'd' has wrong value. Expected: 8, Actual: 96/13"""
