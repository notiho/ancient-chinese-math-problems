"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=48)箇 ，箇 b(=7)錢 。其 c(=30)箇 ，箇 d(=8)錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 576 qian to buy 78 bamboo pieces.
It is desired to determine the rate of large and small bamboo pieces.
Question: how many of each, and at what price per piece?

The procedure for rates says: Place the quantities of each type (e.g., shi, jun, jin, liang) as the divisor.
Multiply the expenditure by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the result.
If the result does not match the divisor, subtract the dividend from the divisor.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: 48 pieces at 7 qian each, and 30 pieces at 8 qian each.
"""

# 出錢五百七十六
總錢 = 576

# 買竹七十八箇
總竹 = 78

# 大竹每箇 8 錢，小竹每箇 7 錢
大竹價 = 8
小竹價 = 7

# 設大竹數為 x，小竹數為 y
# x + y = 總竹
# 8x + 7y = 總錢

# 解聯立方程
# x = 總竹 - y
# 8(總竹 - y) + 7y = 總錢
# 8總竹 - 8y + 7y = 總錢
# -y = 總錢 - 8總竹
# y = 8總竹 - 總錢

小竹數 = 8 * 總竹 - 總錢
大竹數 = 總竹 - 小竹數

# 計算結果
a = 大竹數  # 48
b = 小竹價  # 7
c = 小竹數  # 30
d = 大竹價  # 8#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 48, Actual: 30
Variable 'c' has wrong value. Expected: 30, Actual: 48"""
