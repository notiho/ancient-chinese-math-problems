"""
今有牛馬羊食人苗苗主責之粟五斗羊主曰我羊食半馬馬主曰我馬食半牛今欲衰償之問各出幾何
術曰置牛四馬二羊一各自為列衰副并為法以五斗乘未并者各自為實實如法得一斗
荅曰牛主出 a斗 馬主出 b斗 羊主出 c升 
"""

#----- content starts here -----
"""
Suppose there are oxen, horses, and sheep that ate a farmer's crops. The farmer demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half."
The horse owner says: "My horse ate half of what the ox ate."
Question: How much should each owner pay?

The procedure says: Assign 4 to the ox, 2 to the horse, and 1 to the sheep. Each becomes its own term in the sequence.
In auxiliary, add them together to form the divisor.
Multiply the uncompensated millet (5 dou) by the unadded terms, making them the dividends.
Divide the dividends by the divisor to find the amount of millet each owes.

The answer says: The ox owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

# 置牛四，馬二，羊一
牛 = 4
馬 = 2
羊 = 1

# 各自為列，衰副并為法
法 = 牛 + 馬 + 羊

# 以五斗乘未并者
總斗 = 5
牛實 = 總斗 * 牛
馬實 = 總斗 * 馬
羊實 = 總斗 * 羊

# 實如法得一斗
a = Fraction(牛實, 法)  # 牛主出
b = Fraction(馬實, 法)  # 馬主出
c = Fraction(羊實, 法) * 10  # 羊主出 (converted to 升, as 1 斗 = 10 升)#----- content ends here -----

"""
"""
