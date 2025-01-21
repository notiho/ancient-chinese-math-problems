"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
Suppose there is an island visible from the sea. Two poles are erected, both of equal height of 3 zhang, and the distance between the two poles is 1000 bu. 
The rear pole is aligned with the front pole and the island peak. From the front pole, stepping back 123 bu, the observer's eye level aligns the peak of the island with the top of the pole. 
From the rear pole, stepping back 127 bu, the observer's eye level also aligns the peak of the island with the top of the pole. 
Question: What are the height of the island and the distance from the front pole to the island?

The procedure says: Multiply the height of the pole by the distance between the poles to get the dividend. 
The difference between the two backward steps is the divisor. Divide the dividend by the divisor, and add the height of the pole to get the height of the island. 
To find the distance from the front pole to the island, multiply the backward step from the front pole by the distance between the poles to get the dividend. 
The difference between the two backward steps is the divisor. Divide the dividend by the divisor to get the distance from the front pole to the island.

Answer: The height of the island is *a* li; the distance from the front pole to the island is *b* li.
"""

# 表高三丈
表高 = 3

# 前後相去千步
表間 = 1000

# 從前表卻行一百二十三步
前表卻行 = 123

# 從後表卻行一百二十七步
後表卻行 = 127

# 相多為法
相多 = 後表卻行 - 前表卻行

# 以表高乘表間為實
島高實 = 表高 * 表間

# 除之，所得加表高，即得島高
島高 = Fraction(島高實, 相多) + 表高

# 以前表卻行乘表間為實
島去表實 = 前表卻行 * 表間

# 除之，得島去表數
島去表數 = Fraction(島去表實, 相多)

# Convert to li (1 zhang = 10 chi, 1 bu = 6 chi, 1 li = 300 bu)
島高_里 = Fraction(島高 * 10, 300 * 6)
島去表_里 = Fraction(島去表數, 300)

a = 島高_里
b = 島去表_里
"""
"""
