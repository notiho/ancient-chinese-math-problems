"""
今有望松生山上不知高下立兩表齊高二丈前後相去五十步令後表與前表參相直從前表卻行七步四尺薄地遙望松末與表端參合又望松本入表二尺八寸复從後表卻行八步五尺薄地遙望松末亦與表端參合問松高及山去表各幾何
術曰以入表乘表間為實相多為法除之加入表即得松高求表去山遠近者置表間以前表卻行乘之為實相多為法除之得山去表
答曰松高 a丈 山去表 b里 
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, with unknown height and distance.
Two poles are erected, each 2 zhang high, and are 50 bu apart from each other. 
The rear pole, the front pole, and the pine tree are aligned in a straight line.
From the front pole, one walks backward 7 bu and 4 chi on level ground, and observes that the top of the pine tree aligns with the top of the pole.
Additionally, the base of the pine tree aligns 2 chi 8 cun into the pole.
From the rear pole, one walks backward 8 bu and 5 chi on level ground, and observes that the top of the pine tree again aligns with the top of the pole.
Question: What are the height of the pine tree and the distance from the mountain to the pole?

The procedure says:
To calculate the height of the pine tree:
Multiply the amount the base of the pine tree enters into the pole by the distance between the poles, obtaining the dividend.
Multiply the distances walked backward from the poles, obtaining the divisor.
Divide the dividend by the divisor, and add the height of the pole to obtain the height of the pine tree.

To calculate the distance from the mountain to the pole:
Take the distance between the poles, and multiply it by the distance walked backward from the front pole, obtaining the dividend.
Multiply the distances walked backward from the poles, obtaining the divisor.
Divide the dividend by the divisor to obtain the distance from the mountain to the pole.

Answer: The height of the pine tree is *a* zhang, and the distance from the mountain to the pole is *b* li.
"""

# 表高
表高 = 2  # 丈

# 表間
表間 = 50  # 步

# 前表卻行
前表卻行 = 7 + Fraction(4, 10)  # 步

# 入表
入表 = Fraction(2, 10) + Fraction(8, 100)  # 丈

# 後表卻行
後表卻行 = 8 + Fraction(5, 10)  # 步

# 求松高
# 以入表乘表間為實
松高實 = 入表 * 表間

# 相多為法
松高法 = 前表卻行 * 後表卻行

# 除之加入表即得松高
a = Fraction(松高實, 松高法) + 表高

# 求山去表
# 置表間以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法
山去表法 = 松高法

# 除之得山去表
b = Fraction(山去表實, 山去表法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1398/629
Variable 'b' has wrong value. Expected: 23/21, Actual: 100/17"""
