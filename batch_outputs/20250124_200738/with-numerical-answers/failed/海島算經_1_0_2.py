"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a(=251/60)里 ；去表 b(=205/2)里 。
"""

#----- content starts here -----
"""
Suppose there is an island visible from the sea. Two poles are erected, each 3 zhang high, with a distance of 1000 bu between them. The rear pole is aligned with the front pole and the peak of the island.
From the front pole, one walks back 123 bu, and from there, with the eye at ground level, the peak of the island aligns with the top of the pole.
From the rear pole, one walks back 127 bu, and from there, with the eye at ground level, the peak of the island also aligns with the top of the pole.
Question: What are the height of the island and the distance from the front pole to the island?

The procedure says: Multiply the height of the pole by the distance between the poles to obtain the dividend. Subtract the two retreat distances to obtain the divisor. Divide the dividend by the divisor, and add the height of the pole to the result to obtain the height of the island.
To find the distance from the front pole to the island: Multiply the retreat distance from the front pole by the distance between the poles to obtain the dividend. Subtract the two retreat distances to obtain the divisor. Divide the dividend by the divisor to obtain the distance from the front pole to the island.

Answer: The height of the island is *a*(=251/60) li; the distance from the front pole to the island is *b*(=205/2) li.
"""

# 表高三丈
表高 = 3

# 前後相去千步
表間 = 1000

# 從前表卻行一百二十三步
前表卻行 = 123

# 從後表卻行一百二十七步
後表卻行 = 127

# 求島高
# 以表高乘表間為實
島高實 = 表高 * 表間

# 相多為法
島高法 = 後表卻行 - 前表卻行

# 除之
島高 = Fraction(島高實, 島高法)

# 所得加表高，即得島高
a = 島高 + 表高  # 251/60 li

# 求前表去島遠近
# 以前表卻行乘表間為實
島距實 = 前表卻行 * 表間

# 相多為法
島距法 = 後表卻行 - 前表卻行

# 除之，得島去表數
b = Fraction(島距實, 島距法)  # 205/2 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 753
Variable 'b' has wrong value. Expected: 205/2, Actual: 30750"""
