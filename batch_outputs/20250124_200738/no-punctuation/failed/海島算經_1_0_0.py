"""
今有望海島立兩表齊高三丈前後相去千步令後表與前表參相直從前表卻行一百二十三步人目著地取望島峯與表末參合從後表卻行一百二十七步人目著地取望島峯亦與表末參合問島高及去表各幾何
術曰以表高乘表間為實相多為法除之所得加表高即得島高求前表去島遠近者以前表卻行乘表間為實相多為法除之得島去表數
答曰島高 a里 去表 b里 
"""

#----- content starts here -----
"""
Suppose there is an island visible from the sea. Two poles of equal height, each 3 zhang tall, are erected. 
The distance between the front pole and the rear pole is 1000 bu. 
The rear pole and the front pole are aligned in a straight line with the island's peak.
From the front pole, one walks backward 123 bu, and with their eyes at ground level, observes the island's peak aligning with the top of the pole.
From the rear pole, one walks backward 127 bu, and with their eyes at ground level, observes the island's peak aligning with the top of the pole.
Question: What are the height of the island and its distance from the poles?

The procedure says:
- Multiply the height of the pole by the distance between the poles to get the dividend.
- Multiply the distances walked backward (123 and 127) to get the divisor.
- Divide the dividend by the divisor, and add the height of the pole to get the height of the island.
- To find the distance from the front pole to the island, multiply the distance walked backward from the front pole (123) by the distance between the poles to get the dividend.
- Divide this by the divisor to get the distance from the front pole to the island.

Answer: The height of the island is *a* li, and the distance from the poles is *b* li.
"""

# 表高
表高 = 3  # 丈

# 表間
表間 = 1000  # 步

# 前表卻行
前表卻行 = 123  # 步

# 後表卻行
後表卻行 = 127  # 步

# 求島高
# 表高乘表間為實
島高實 = 表高 * 表間

# 相多為法
島高法 = 前表卻行 * 後表卻行

# 除之所得，加表高，即得島高
島高 = Fraction(島高實, 島高法) + 表高

# 求前表去島遠
# 前表卻行乘表間為實
島遠實 = 前表卻行 * 表間

# 相多為法
島遠法 = 島高法

# 除之，得島去表數
島遠 = Fraction(島遠實, 島遠法)

# Convert to li (1 丈 = 1/300 里, 1 步 = 6/300 里)
a = 島高 * Fraction(1, 300)  # 島高 in 里
b = 島遠 * Fraction(6, 300)  # 島遠 in 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 16621/1562100
Variable 'b' has wrong value. Expected: 205/2, Actual: 20/127"""
