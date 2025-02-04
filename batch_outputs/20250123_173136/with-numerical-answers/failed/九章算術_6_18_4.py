"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a(=95/66)升 ，次 b(=4/3)升 ，次 c(=27/22)升 ，次 d(=37/33)升 ，次 e(=67/66)升 ，次 f(=10/11)升 ，次 g(=53/66)升 ，次 h(=23/33)升 ，次 i(=13/22)升 。
"""

"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: how much should the middle 2 nodes hold to balance the capacity evenly?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to get the bottom rate, and divide the 3 sheng among the top 4 nodes to get the top rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the 4 nodes and 3 nodes, halve each, and subtract from the 9 nodes. The remainder is the divisor.
Divide the dividend by the divisor to get 1 sheng, which is the difference between successive nodes.
The bottom rate, plus 1 sheng and half a sheng less, gives the capacity of the second node from the bottom.

Answer: The capacities of the nodes are:
*a*(=95/66) sheng, *b*(=4/3) sheng, *c*(=27/22) sheng, *d*(=37/33) sheng, *e*(=67/66) sheng, *f*(=10/11) sheng, *g*(=53/66) sheng, *h*(=23/33) sheng, *i*(=13/22) sheng.
"""

from fractions import Fraction

# 下三節容四升
下節數 = 3
下總升 = 4

# 上四節容三升
上節數 = 4
上總升 = 3

# 以下三節分四升為下率
下率 = Fraction(下總升, 下節數)

# 以上四節分三升為上率
上率 = Fraction(上總升, 上節數)

# 上下率以少減多，餘為實
實 = abs(下率 - 上率)

# 置四節、三節，各半之
上半節數 = Fraction(上節數, 2)
下半節數 = Fraction(下節數, 2)

# 以減九節，餘為法
總節數 = 9
法 = 總節數 - (上半節數 + 下半節數)

# 實如法得一升，即衰相去也
一升 = Fraction(實, 法)

# 計算每節的容量
節容量 = []
for i in range(總節數):
    if i < 下節數:  # 下三節
        容量 = 下率 + i * 一升
    elif i < 下節數 + 2:  # 中間二節
        容量 = 下率 + 下節數 * 一升 + (i - 下節數) * 一升
    else:  # 上四節
        容量 = 上率 + (總節數 - 1 - i) * 一升
    節容量.append(容量)

# Assigning results to variables
a, b, c, d, e, f, g, h, i = 節容量  # 95/66, 4/3, 27/22, 37/33, 67/66, 10/11, 53/66, 23/33, 13/22
"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: 95/66
Variable 'c' has wrong value. Expected: 27/22, Actual: 17/11
Variable 'd' has wrong value. Expected: 37/33, Actual: 109/66
Variable 'e' has wrong value. Expected: 67/66, Actual: 58/33
Variable 'f' has wrong value. Expected: 10/11, Actual: 47/44
Variable 'g' has wrong value. Expected: 53/66, Actual: 127/132
Variable 'h' has wrong value. Expected: 23/33, Actual: 113/132
Variable 'i' has wrong value. Expected: 13/22, Actual: 3/4"""
