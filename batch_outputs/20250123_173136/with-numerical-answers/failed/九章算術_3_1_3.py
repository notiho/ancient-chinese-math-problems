"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a(=20/7)斗 。馬主出 b(=10/7)斗 。羊主出 c(=50/7)升 。
"""

"""
Suppose there are a cow, a horse, and a sheep that ate someone's crops. The crop owner demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half as much as a horse."
The horse owner says: "My horse ate half as much as a cow."
Now, dividing the compensation proportionally, how much should each pay?

The procedure says: Assign 4 to the cow, 2 to the horse, and 1 to the sheep. Each becomes its own element in the decreasing sequence.
In auxiliary, add them together to get the divisor.
Multiply the 5 dou by the uncombined numbers, each becoming its own dividend.
Divide the dividends by the divisor to get the amount of millet.

The answer says: The cow owner pays *a*(=20/7) dou, the horse owner pays *b*(=10/7) dou, and the sheep owner pays *c*(=50/7) sheng.
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

# 各自為實，實如法得一斗
a, b, c = [Fraction(i, 法) for i in 实]  # 牛主出20/7斗, 馬主出10/7斗, 羊主出50/7升
"""
Code error: name '实' is not defined"""
