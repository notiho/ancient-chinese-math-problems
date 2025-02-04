"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

#----- content starts here -----
"""
Suppose there is a sea island in view. Two poles are erected, both of equal height of 3 zhang, and spaced 1000 bu apart front to back. 
The rear pole is aligned with the front pole and the peak of the island. 
From the front pole, walking backward 123 bu, a person places their eye at ground level and observes the peak of the island aligning with the top of the pole. 
From the rear pole, walking backward 127 bu, the same observation is made.
Question: what is the height of the island and its distance from the poles?

The procedure says: Multiply the height of the pole by the distance between the poles to obtain the dividend. 
The difference between the backward distances is the divisor. Divide the dividend by the divisor. Add the height of the pole to the result to obtain the height of the island.
To find the distance from the front pole to the island: Multiply the backward distance from the front pole by the distance between the poles to obtain the dividend. 
The difference between the backward distances is the divisor. Divide the dividend by the divisor to obtain the distance from the front pole to the island.

Answer: the height of the island is *a* li; the distance from the front pole to the island is *b* li.
"""

# 表高三丈
表高 = 3  # 丈

# 前後相去千步
表間 = 1000  # 步

# 從前表卻行一百二十三步
前表卻行 = 123  # 步

# 從後表卻行一百二十七步
後表卻行 = 127  # 步

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

# Convert to li (1 丈 = 1/300 里, 1 步 = 1/1500 里)
a = 島高 * Fraction(1, 300)  # 島高 in 里
b = 島去表數 * Fraction(1, 1500)  # 島去表數 in 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/100
Variable 'b' has wrong value. Expected: 205/2, Actual: 41/2"""
