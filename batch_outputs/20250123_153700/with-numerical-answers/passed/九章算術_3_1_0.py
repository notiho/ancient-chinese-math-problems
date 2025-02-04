"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a(=20/7)斗 。馬主出 b(=10/7)斗 。羊主出 c(=50/7)升 。
"""

"""
Suppose there are oxen, horses, and sheep eating a farmer's crops. The farmer demands 5 dou of millet as compensation.
The sheep's owner says: "My sheep ate half as much as a horse."
The horse's owner says: "My horse ate half as much as an ox."
Now, dividing the compensation proportionally, how much should each pay?

The procedure says: Assign 4 to the ox, 2 to the horse, and 1 to the sheep. Each becomes its own element in the decreasing sequence.
In auxiliary, add them together to form the divisor.
Multiply the 5 dou by the unadded elements, each becoming its own dividend.
Divide the dividends by the divisor to obtain the millet owed by each.

The answer says: The ox's owner pays *a*(=20/7) dou, the horse's owner pays *b*(=10/7) dou, and the sheep's owner pays *c*(=50/7) sheng.
"""

# 牛、馬、羊的比例
牛 = 4
馬 = 2
羊 = 1

# 副并為法
法 = 牛 + 馬 + 羊

# 置五斗
總補償 = 5  # 5斗

# 以五斗乘未并者
牛實 = 總補償 * 牛
馬實 = 總補償 * 馬
羊實 = 總補償 * 羊

# 實如法得一斗
a = Fraction(牛實, 法)  # 20/7 斗
b = Fraction(馬實, 法)  # 10/7 斗
c = Fraction(羊實, 法) * 10  # 50/7 升 (1斗 = 10升)
"""
"""
