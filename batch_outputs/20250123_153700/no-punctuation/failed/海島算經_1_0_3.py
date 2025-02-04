"""
今有望海島立兩表齊高三丈前後相去千步令後表與前表參相直從前表卻行一百二十三步人目著地取望島峯與表末參合從後表卻行一百二十七步人目著地取望島峯亦與表末參合問島高及去表各幾何
術曰以表高乘表間為實相多為法除之所得加表高即得島高求前表去島遠近者以前表卻行乘表間為實相多為法除之得島去表數
答曰島高 a里 去表 b里 
"""

"""
Suppose there is an island in the sea. Two poles of equal height, each 3 zhang tall, are erected. 
The distance between the front pole and the back pole is 1000 bu. 
The back pole is aligned with the front pole and the peak of the island in a straight line. 
From the front pole, one walks backward 123 bu, and with the eye on the ground, the peak of the island aligns with the top of the pole. 
From the back pole, one walks backward 127 bu, and with the eye on the ground, the peak of the island again aligns with the top of the pole. 
Question: What are the height of the island and the distance from the poles to the island?

The procedure says: Multiply the height of the pole by the distance between the poles to obtain the dividend. 
Multiply the distances walked backward to obtain the divisor. 
Divide the dividend by the divisor, and add the height of the pole to obtain the height of the island. 
To find the distance from the front pole to the island, multiply the distance walked backward from the front pole by the distance between the poles to obtain the dividend. 
Multiply the distances walked backward to obtain the divisor. 
Divide the dividend by the divisor to obtain the distance from the pole to the island.

Answer: The height of the island is *a* li, and the distance to the poles is *b* li.
"""

# 表高三丈
表高 = 3

# 前後相去千步
表間 = 1000

# 前表卻行一百二十三步
前表卻行 = 123

# 後表卻行一百二十七步
後表卻行 = 127

# 以表高乘表間為實
實_島高 = 表高 * 表間

# 相多為法
法 = 前表卻行 * 後表卻行

# 除之所得，加表高，即得島高
島高 = Fraction(實_島高, 法) + 表高

# 以前表卻行乘表間為實
實_去表 = 前表卻行 * 表間

# 相多為法
法_去表 = 前表卻行 * 後表卻行

# 除之，得島去表數
島去表 = Fraction(實_去表, 法_去表)

# Convert to li (1 zhang = 1/300 li, 1 bu = 1/1500 li)
a = 島高 * Fraction(1, 300)
b = 島去表 * Fraction(1, 1500)
"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 16621/1562100
Variable 'b' has wrong value. Expected: 205/2, Actual: 2/381"""
