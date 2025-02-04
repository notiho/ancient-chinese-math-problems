"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

#----- content starts here -----
"""
Suppose there is an island visible from the sea. Two poles are erected, both of equal height at 3 zhang, and the distance between the two poles is 1000 bu. 
The rear pole is aligned with the front pole and the island peak. 
From the front pole, a person walks back 123 bu, and with their eyes at ground level, aligns the island peak with the top of the front pole. 
From the rear pole, a person walks back 127 bu, and with their eyes at ground level, aligns the island peak with the top of the rear pole. 
Question: What are the height of the island and the distance from the front pole to the island?

The procedure says: Multiply the height of the pole by the distance between the poles to get the dividend. 
The difference between the two distances walked back is the divisor. Divide the dividend by the divisor, and add the height of the pole to get the height of the island. 
To find the distance from the front pole to the island, multiply the distance walked back from the front pole by the distance between the poles to get the dividend. 
The difference between the two distances walked back is the divisor. Divide the dividend by the divisor to get the distance from the front pole to the island.

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

# Convert to li (1 zhang = 1/300 li, 1 bu = 1/1500 li)
a = Fraction(島高, 300)  # 島高 in li
b = Fraction(島去表數, 1500)  # 島去表數 in li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/100
Variable 'b' has wrong value. Expected: 205/2, Actual: 41/2"""
