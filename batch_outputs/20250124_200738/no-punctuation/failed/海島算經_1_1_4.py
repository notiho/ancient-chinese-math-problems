"""
今有望松生山上不知高下立兩表齊高二丈前後相去五十步令後表與前表參相直從前表卻行七步四尺薄地遙望松末與表端參合又望松本入表二尺八寸复從後表卻行八步五尺薄地遙望松末亦與表端參合問松高及山去表各幾何
術曰以入表乘表間為實相多為法除之加入表即得松高求表去山遠近者置表間以前表卻行乘之為實相多為法除之得山去表
答曰松高 a丈 山去表 b里 
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height and distance are unknown.
Two poles are erected, each 2 zhang tall, and the distance between the poles is 50 bu.
The rear pole is aligned with the front pole and the pine tree.
From the front pole, one walks backward 7 bu and 4 chi along the ground.
Looking up, the top of the pine tree aligns with the top of the pole, and the base of the pine tree is observed to be 2 chi and 8 cun below the top of the pole.
Then, from the rear pole, one walks backward 8 bu and 5 chi along the ground.
Looking up again, the top of the pine tree aligns with the top of the pole.

Question: What is the height of the pine tree and the distance from the mountain to the pole?

The procedure says:
To find the height of the pine tree:
Multiply the amount the base of the pine tree enters below the pole by the distance between the poles to get the dividend.
Multiply the distances walked backward to get the divisor.
Divide the dividend by the divisor, then add the height of the pole to get the height of the pine tree.

To find the distance from the mountain to the pole:
Take the distance between the poles and multiply it by the distance walked backward from the front pole to get the dividend.
Multiply the distances walked backward to get the divisor.
Divide the dividend by the divisor to get the distance from the mountain to the pole.

Answer: The height of the pine tree is *a* zhang, and the distance from the mountain to the pole is *b* li.
"""

# 表高
表高 = 2  # 丈

# 表間
表間 = 50  # 步

# 前表卻行
前表卻行 = 7 + Fraction(4, 10)  # 步 (7步4尺)

# 松本入表
松本入表 = Fraction(2, 10) + Fraction(8, 100)  # 丈 (2尺8寸)

# 後表卻行
後表卻行 = 8 + Fraction(5, 10)  # 步 (8步5尺)

# 求松高
# 以入表乘表間為實
松高實 = 松本入表 * 表間

# 相多為法
松高法 = 前表卻行 * 後表卻行

# 除之加入表即得松高
松高 = Fraction(松高實, 松高法) + 表高

# 求表去山遠近
# 置表間以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法
山去表法 = 前表卻行 * 後表卻行

# 除之得山去表
山去表 = Fraction(山去表實, 山去表法)

# Convert 山去表 from 步 to 里 (1 里 = 300 步)
山去表 = Fraction(山去表, 300)

# Final answers
a = 松高  # 松高 in 丈
b = 山去表  # 山去表 in 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1398/629
Variable 'b' has wrong value. Expected: 23/21, Actual: 1/51"""
