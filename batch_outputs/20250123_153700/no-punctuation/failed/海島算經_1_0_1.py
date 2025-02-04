"""
今有望海島立兩表齊高三丈前後相去千步令後表與前表參相直從前表卻行一百二十三步人目著地取望島峯與表末參合從後表卻行一百二十七步人目著地取望島峯亦與表末參合問島高及去表各幾何
術曰以表高乘表間為實相多為法除之所得加表高即得島高求前表去島遠近者以前表卻行乘表間為實相多為法除之得島去表數
答曰島高 a里 去表 b里 
"""

"""
Suppose there is an island visible from the sea. Two poles of equal height, each 3 zhang tall, are erected. 
The distance between the two poles is 1000 bu. 
The rear pole is aligned with the front pole and the peak of the island. 
From the front pole, one walks backward 123 bu, lies on the ground, and observes the peak of the island aligning with the top of the pole. 
Similarly, from the rear pole, one walks backward 127 bu, lies on the ground, and observes the same alignment. 
Question: What is the height of the island and its distance from the poles?

The procedure says: Multiply the height of the pole by the distance between the poles to get the dividend. 
Multiply the distances walked backward from the poles to get the divisor. 
Divide the dividend by the divisor, then add the height of the pole to obtain the height of the island. 
To find the distance from the front pole to the island, multiply the distance walked backward from the front pole by the distance between the poles to get the dividend. 
Divide this by the divisor to obtain the distance from the island to the poles.

Answer: The height of the island is *a* li, and the distance from the poles is *b* li.
"""

# 表高三丈
表高 = 3

# 前後相去千步
表間 = 1000

# 前表卻行一百二十三步
前表卻行 = 123

# 後表卻行一百二十七步
後表卻行 = 127

# 求島高
# 以表高乘表間為實
島高實 = 表高 * 表間

# 相多為法
島高法 = 前表卻行 * 後表卻行

# 除之所得，加表高，即得島高
島高 = Fraction(島高實, 島高法) + 表高

# 求前表去島遠
# 以前表卻行乘表間為實
去島實 = 前表卻行 * 表間

# 相多為法
去島法 = 島高法

# 除之，得島去表數
去表 = Fraction(去島實, 去島法)

# Convert zhang to li (1 zhang = 1/300 li)
a = Fraction(島高, 300)
b = Fraction(去表, 300)
"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 16621/1562100
Variable 'b' has wrong value. Expected: 205/2, Actual: 10/381"""
