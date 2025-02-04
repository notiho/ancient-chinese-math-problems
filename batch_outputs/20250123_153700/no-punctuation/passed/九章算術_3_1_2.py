"""
今有牛馬羊食人苗苗主責之粟五斗羊主曰我羊食半馬馬主曰我馬食半牛今欲衰償之問各出幾何
術曰置牛四馬二羊一各自為列衰副并為法以五斗乘未并者各自為實實如法得一斗
荅曰牛主出 a斗 馬主出 b斗 羊主出 c升 
"""

"""
Suppose there are cattle, horses, and sheep that ate a farmer's crops. The farmer demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half."
The horse owner says: "My horse ate half of what the cattle ate."
Now, it is desired to calculate the proportional compensation. 
Question: how much does each owner pay?

The procedure says: Assign 4 to the cattle, 2 to the horse, and 1 to the sheep. 
Each becomes its own term in the sequence.
In auxiliary, add them together to form the divisor.
Multiply the 5 dou by the uncombined terms, and each becomes its own dividend.
Divide the dividends by the divisor to obtain the compensation in dou.

The answer says: the cattle owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

# 牛四，馬二，羊一
牛 = 4
馬 = 2
羊 = 1

# 各自為列
列 = [牛, 馬, 羊]

# 衰副并為法
法 = sum(列)

# 置五斗
總斗 = 5

# 以五斗乘未并者，各自為實
實 = [總斗 * i for i in 列]

# 實如法得一斗
a = Fraction(實[0], 法)  # 牛主出
b = Fraction(實[1], 法)  # 馬主出
c = Fraction(實[2], 法) * 10  # 羊主出 (converted to 升 since 1 斗 = 10 升)
"""
"""
