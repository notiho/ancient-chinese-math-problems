"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a(=95/66)升 ，次 b(=4/3)升 ，次 c(=27/22)升 ，次 d(=37/33)升 ，次 e(=67/66)升 ，次 f(=10/11)升 ，次 g(=53/66)升 ，次 h(=23/33)升 ，次 i(=13/22)升 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo with nine nodes. The bottom three nodes hold 4 sheng, and the top four nodes hold 3 sheng.
Question: how much should the middle two nodes hold to balance the capacity evenly?

The procedure says: Divide the 4 sheng among the bottom three nodes to get the lower rate, and divide the 3 sheng among the top four nodes to get the upper rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the four nodes and three nodes, halve each, and subtract from the nine nodes. The remainder is the divisor.
Divide the dividend by the divisor to get one sheng, which is the amount by which the rates decrease progressively.
The lower rate plus one sheng and half a sheng less gives the capacity of the second node from the bottom.

Answer: The capacities of the nodes are as follows:
*a*(=95/66) sheng, *b*(=4/3) sheng, *c*(=27/22) sheng, *d*(=37/33) sheng, *e*(=67/66) sheng, *f*(=10/11) sheng, *g*(=53/66) sheng, *h*(=23/33) sheng, *i*(=13/22) sheng.
"""

from fractions import Fraction

# 下三節容四升
下三節 = 3
下容 = 4

# 上四節容三升
上四節 = 4
上容 = 3

# 以下三節分四升為下率
下率 = Fraction(下容, 下三節)

# 以上四節分三升為上率
上率 = Fraction(上容, 上四節)

# 上下率以少減多，餘為實
實 = 下率 - 上率

# 置四節、三節，各半之
四節半 = Fraction(上四節, 2)
三節半 = Fraction(下三節, 2)

# 以減九節，餘為法
九節 = 9
法 = 九節 - (四節半 + 三節半)

# 實如法得一升，即衰相去也
衰相去 = Fraction(實, 法)

# 計算每節的容量
節數 = 9
節容量 = []
for i in range(節數):
    if i < 下三節:
        # 下節：從下率遞減
        容量 = 下率 - i * 衰相去
    elif i < 下三節 + 2:
        # 中間兩節：均容
        容量 = 下率 - 下三節 * 衰相去
    else:
        # 上節：從上率遞減
        容量 = 上率 + (節數 - 1 - i) * 衰相去
    節容量.append(容量)

# 分配結果
a, b, c, d, e, f, g, h, i = 節容量  # 分別對應九節的容量#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: 27/22
Variable 'c' has wrong value. Expected: 27/22, Actual: 37/33
Variable 'd' has wrong value. Expected: 37/33, Actual: 67/66
Variable 'f' has wrong value. Expected: 10/11, Actual: 47/44
Variable 'g' has wrong value. Expected: 53/66, Actual: 127/132
Variable 'h' has wrong value. Expected: 23/33, Actual: 113/132
Variable 'i' has wrong value. Expected: 13/22, Actual: 3/4"""
