"""
今有望松生山上不知高下立兩表齊高二丈前後相去五十步令後表與前表參相直從前表卻行七步四尺薄地遙望松末與表端參合又望松本入表二尺八寸复從後表卻行八步五尺薄地遙望松末亦與表端參合問松高及山去表各幾何
術曰以入表乘表間為實相多為法除之加入表即得松高求表去山遠近者置表間以前表卻行乘之為實相多為法除之得山去表
答曰松高 a丈 山去表 b里 
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height is unknown. Two poles, each 2 zhang tall, are erected at equal heights. The distance between the two poles is 50 bu. The rear pole, the front pole, and the pine tree are aligned in a straight line. From the front pole, step back 7 bu and 4 chi on flat ground, and observe that the top of the pine tree aligns with the top of the pole. The base of the pine tree is observed to be 2 chi and 8 cun below the top of the pole. Then, from the rear pole, step back 8 bu and 5 chi on flat ground, and observe again that the top of the pine tree aligns with the top of the pole.

Question: What are the height of the pine tree and the distance from the mountain to the poles?

The procedure says: To find the height of the pine tree, multiply the amount the tree base enters below the pole by the distance between the poles to get the dividend. Multiply the distances stepped back to get the divisor. Divide the dividend by the divisor, and add the height of the pole to get the height of the pine tree.

To find the distance from the mountain to the poles, take the distance between the poles and multiply it by the distance stepped back from the front pole to get the dividend. Multiply the distances stepped back to get the divisor. Divide the dividend by the divisor to get the distance from the mountain to the poles.

Answer: The height of the pine tree is *a* zhang, and the distance from the mountain to the poles is *b* li.
"""

# 表高二丈
表高 = 2

# 前後相去五十步
表間 = 50

# 前表卻行七步四尺
前表卻行 = 7 + Fraction(4, 10)

# 松本入表二尺八寸
松本入表 = 2 + Fraction(8, 10)

# 後表卻行八步五尺
後表卻行 = 8 + Fraction(5, 10)

# 求松高
# 以入表乘表間為實
松高實 = 松本入表 * 表間

# 相多為法
松高法 = 前表卻行 * 後表卻行

# 除之加入表即得松高
松高 = Fraction(松高實, 松高法) + 表高

# 求表去山遠近
# 置表間以前表卻行乘之為實
表去山實 = 表間 * 前表卻行

# 相多為法
表去山法 = 前表卻行 * 後表卻行

# 除之得山去表
山去表 = Fraction(表去山實, 表去山法)

# Convert 山去表 from bu to li (1 li = 300 bu)
山去表 = Fraction(山去表, 300)

# Final answers
a = 松高  # 松高 in zhang
b = 山去表  # 山去表 in li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 2658/629
Variable 'b' has wrong value. Expected: 23/21, Actual: 1/51"""
