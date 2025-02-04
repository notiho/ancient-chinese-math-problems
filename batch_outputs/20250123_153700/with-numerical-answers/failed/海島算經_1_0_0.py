"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a(=251/60)里 ；去表 b(=205/2)里 。
"""

"""
Suppose there is an island visible from the sea. Two poles are erected, each 3 zhang high, and they are 1000 bu apart from each other. 
The rear pole is aligned with the front pole and the peak of the island. 
From the front pole, one walks backward 123 bu, and from this point, with one's eyes at ground level, the peak of the island aligns with the top of the front pole. 
From the rear pole, one walks backward 127 bu, and from this point, with one's eyes at ground level, the peak of the island aligns with the top of the rear pole. 
Question: What are the height of the island and its distance from the poles?

The procedure says: Multiply the height of the pole by the distance between the poles to get the dividend. 
The difference between the backward distances is the divisor. Divide the dividend by the divisor. Add the height of the pole to the result to get the height of the island. 
To find the distance from the front pole to the island, multiply the backward distance from the front pole by the distance between the poles to get the dividend. 
The difference between the backward distances is the divisor. Divide the dividend by the divisor to get the distance from the front pole to the island.

Answer: The height of the island is *a*(=251/60) li, and the distance from the front pole to the island is *b*(=205/2) li.
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
法 = 後表卻行 - 前表卻行

# 以表高乘表間為實
實_島高 = 表高 * 表間

# 除之，所得加表高，即得島高
島高 = Fraction(實_島高, 法) + 表高

# 以前表卻行乘表間為實
實_去表 = 前表卻行 * 表間

# 除之，得島去表數
島去表 = Fraction(實_去表, 法)

# Convert to li (1 zhang = 1/30 li, 1 bu = 1/180 li)
島高_li = Fraction(島高, 30)  # Convert zhang to li
島去表_li = Fraction(島去表, 180)  # Convert bu to li

a = 島高_li  # 251/60 li
b = 島去表_li  # 205/2 li
"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/10
Variable 'b' has wrong value. Expected: 205/2, Actual: 1025/6"""
