"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=48)箇 ，箇 b(=7)錢 。其 c(=30)箇 ，箇 d(=8)錢 。
"""

"""
Suppose there is an expenditure of 576 qian to buy 78 bamboo poles. It is desired to determine the rates of large and small bamboo poles.
Question: how many of each type, and at what price per pole?

The procedure for rates says: Place the quantities of each type (e.g., large and small) as the divisor.
Multiply the total money by the rates to obtain the dividend.
Divide the dividend by the divisor to obtain the result.
If the dividend does not match the divisor, subtract the divisor from the dividend. The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: There are *a*(=48) large poles, each costing *b*(=7) qian. There are *c*(=30) small poles, each costing *d*(=8) qian.
"""

# 出錢五百七十六
錢數 = 576

# 買竹七十八箇
竹數 = 78

# 大竹率 7 錢， 小竹率 8 錢
大竹率 = 7
小竹率 = 8

# 設大竹數為 a， 小竹數為 c
# 大竹數 + 小竹數 = 竹數
# 大竹數 * 大竹率 + 小竹數 * 小竹率 = 錢數

# 解聯立方程
# 大竹數 = a, 小竹數 = c
# a + c = 78
# 7a + 8c = 576

# 由 a + c = 78 得 c = 78 - a
# 將 c = 78 - a 代入 7a + 8c = 576
# 7a + 8(78 - a) = 576
# 7a + 624 - 8a = 576
# -a + 624 = 576
# -a = -48
# a = 48

a = 48  # 大竹數
c = 竹數 - a  # 小竹數

# 算出每箇錢數
b = 大竹率  # 大竹每箇 7 錢
d = 小竹率  # 小竹每箇 8 錢
"""
"""
