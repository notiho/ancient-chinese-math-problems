"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are a cow, a horse, and a sheep eating a farmer's crops. The farmer demands 5 dou of millet as compensation.
The sheep owner says: "My sheep eats half as much as a horse."
The horse owner says: "My horse eats half as much as a cow."
Now, to divide the compensation proportionally, how much should each pay?

The procedure says: Assign 4 to the cow, 2 to the horse, and 1 to the sheep. Each becomes its own term in the sequence.
Add these together to form the divisor.
Multiply the 5 dou by the uncombined terms for each, forming the dividend.
Divide the dividend by the divisor to obtain the share for each.

The answer says: the cow owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

# 置牛四、馬二、羊一
牛 = 4
馬 = 2
羊 = 1

# 各自為列衰
列衰 = [牛, 馬, 羊]

# 副并為法
法 = sum(列衰)

# 以五斗乘未并者各自為實
總補償 = 5  # in dou
實 = [總補償 * i for i in 列衰]

# 實如法得一斗
a = Fraction(實[0], 法)  # 牛主出
b = Fraction(實[1], 法)  # 馬主出
c = Fraction(實[2], 法) * 10  # 羊主出 (convert dou to sheng, as 1 dou = 10 sheng)#----- content ends here -----

"""
"""
