"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a(=20/7)斗 。馬主出 b(=10/7)斗 。羊主出 c(=50/7)升 。
"""

"""
Suppose there are a cow, a horse, and a sheep eating someone's crops. The owner of the crops demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half as much as the horse."
The horse owner says: "My horse ate half as much as the cow."
Now, it is desired to proportionally compensate. Question: how much does each pay?

The procedure says: Assign 4 to the cow, 2 to the horse, and 1 to the sheep. Each becomes its own decreasing sequence.
In auxiliary, add them together to form the divisor.
Multiply the 5 dou by the unadded values for each, forming the dividend.
Divide the dividend by the divisor to obtain the amount of millet for each.

Answer: The cow owner pays *a*(=20/7) dou, the horse owner pays *b*(=10/7) dou, and the sheep owner pays *c*(=50/7) sheng.
"""

# 置牛四、馬二、羊一
牛 = 4
馬 = 2
羊 = 1

# 各自為列衰
列衰 = [牛, 馬, 羊]

# 副并為法
法 = sum(列衰)

# 以五斗乘未并者
總補償 = 5  # 5斗
實 = [總補償 * i for i in 列衰]

# 實如法得一斗
a, b, c = [Fraction(i, 法) for i in 実]  # 牛: 20/7斗, 馬: 10/7斗, 羊: 50/7升
"""
Code error: name '実' is not defined"""
