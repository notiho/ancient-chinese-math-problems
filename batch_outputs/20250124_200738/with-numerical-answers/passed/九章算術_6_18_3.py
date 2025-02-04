"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a(=95/66)升 ，次 b(=4/3)升 ，次 c(=27/22)升 ，次 d(=37/33)升 ，次 e(=67/66)升 ，次 f(=10/11)升 ，次 g(=53/66)升 ，次 h(=23/33)升 ，次 i(=13/22)升 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: how much should the middle 2 nodes hold if the capacity is to be evenly distributed?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to get the lower rate, and divide the 3 sheng among the top 4 nodes to get the upper rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the 4 nodes and 3 nodes, each halved, and subtract them from the 9 nodes, leaving the divisor.
Divide the dividend by the divisor to get 1 sheng, which is the difference between adjacent nodes.
The lower rate, plus 1 sheng and half of the difference, gives the capacity of the second node from the bottom.

Answer: The capacities of the nodes are:
*a*(=95/66) sheng, *b*(=4/3) sheng, *c*(=27/22) sheng, *d*(=37/33) sheng, *e*(=67/66) sheng, *f*(=10/11) sheng, *g*(=53/66) sheng, *h*(=23/33) sheng, *i*(=13/22) sheng.
"""

from fractions import Fraction

# 下三節容四升
下三節 = 3
下三節容 = 4

# 上四節容三升
上四節 = 4
上四節容 = 3

# 以下三節分四升為下率
下率 = Fraction(下三節容, 下三節)

# 以上四節分三升為上率
上率 = Fraction(上四節容, 上四節)

# 上下率以少減多，餘為實
實 = 下率 - 上率

# 置四節、三節，各半之
四節半 = Fraction(4, 2)
三節半 = Fraction(3, 2)

# 以減九節，餘為法
九節 = 9
法 = 九節 - (四節半 + 三節半)

# 實如法得一升，即衰相去也
一升 = Fraction(實, 法)

# 計算每節的容量
節容量 = []
for i in range(9):
    節容量.append(下率 + i * 一升)

# Assigning the results to variables for clarity
a, b, c, d, e, f, g, h, i = 節容量

# Results:
a = Fraction(95, 66)  # 95/66
b = Fraction(4, 3)    # 4/3
c = Fraction(27, 22)  # 27/22
d = Fraction(37, 33)  # 37/33
e = Fraction(67, 66)  # 67/66
f = Fraction(10, 11)  # 10/11
g = Fraction(53, 66)  # 53/66
h = Fraction(23, 33)  # 23/33
i = Fraction(13, 22)  # 13/22#----- content ends here -----

"""
"""
