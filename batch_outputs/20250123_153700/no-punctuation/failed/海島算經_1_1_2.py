"""
今有望松生山上不知高下立兩表齊高二丈前後相去五十步令後表與前表參相直從前表卻行七步四尺薄地遙望松末與表端參合又望松本入表二尺八寸复從後表卻行八步五尺薄地遙望松末亦與表端參合問松高及山去表各幾何
術曰以入表乘表間為實相多為法除之加入表即得松高求表去山遠近者置表間以前表卻行乘之為實相多為法除之得山去表
答曰松高 a丈 山去表 b里 
"""

"""
Suppose there is a pine tree growing on a mountain, and its height is unknown. Two poles are erected, each 2 zhang tall, and they are 50 bu apart. 
The rear pole is aligned with the front pole and the pine tree. From the front pole, one walks back 7 bu and 4 chi, and observes that the top of the pine tree aligns with the top of the pole, while the base of the pine tree aligns 2 chi 8 cun into the pole. 
Then, from the rear pole, one walks back 8 bu and 5 chi, and observes again that the top of the pine tree aligns with the top of the pole.

Question: What is the height of the pine tree and the distance from the mountain to the poles?

The procedure says: Multiply the amount the tree base enters the pole by the distance between the poles to obtain the dividend. Multiply the total distances walked back to obtain the divisor. Divide the dividend by the divisor, and add the height of the pole to obtain the height of the pine tree.
To find the distance from the mountain to the poles, take the distance between the poles, multiply it by the distance walked back from the front pole, and divide by the divisor. This gives the distance from the mountain to the poles.

Answer: The pine tree is *a* zhang tall, and the mountain is *b* li away from the poles.
"""

from fractions import Fraction

# 表高 2 丈
表高 = 2

# 表間距離 50 步
表間 = 50

# 前表卻行 7 步 4 尺
前表卻行 = 7 + Fraction(4, 10)

# 松本入表 2 尺 8 寸
松本入表 = 2 + Fraction(8, 10)

# 後表卻行 8 步 5 尺
後表卻行 = 8 + Fraction(5, 10)

# 術曰：以入表乘表間為實
實 = 松本入表 * 表間

# 相多為法
法 = 前表卻行 * 後表卻行

# 除之加入表即得松高
松高 = Fraction(實, 法) + 表高

# 求表去山遠近者置表間以前表卻行乘之為實
實_山 = 表間 * 前表卻行

# 相多為法除之得山去表
山去表 = Fraction(實_山, 法)

# 答案
a = 松高  # 松高 in 丈
b = Fraction(山去表, 180)  # 山去表 converted to 里 (1 里 = 180 步)
"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 2658/629
Variable 'b' has wrong value. Expected: 23/21, Actual: 5/153"""
