"""
今有竹九節下三節容四升上四節容三升問中間二節欲均容各多少
術曰以下三節分四升為下率以上四節分三升為上率上下率以少減多餘為實置四節三節各半之以減九節餘為法實如法得一升即衰相去也下率一升少半升者下第二節容也
荅曰下初 a升 次 b升 次 c升 次 d升 次 e升 次 f升 次 g升 次 h升 次 i升 
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: how much should the middle 2 nodes hold if distributed evenly?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to find the bottom rate.
Divide the 3 sheng among the top 4 nodes to find the top rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the 4 nodes and 3 nodes, each halved, and subtract from the 9 nodes. The remainder is the divisor.
Divide the dividend by the divisor to find 1 sheng, which is the difference between successive nodes.
Subtract half a sheng from the bottom rate to find the second node's volume.

Answer: The bottom node holds *a* sheng, the second node holds *b* sheng, ..., the ninth node holds *i* sheng.
"""

# 下三節容四升
下節數 = 3
下容積 = 4

# 上四節容三升
上節數 = 4
上容積 = 3

# 中間二節
中節數 = 2

# 竹九節
總節數 = 9

# 以下三節分四升為下率
下率 = Fraction(下容積, 下節數)

# 以上四節分三升為上率
上率 = Fraction(上容積, 上節數)

# 上下率以少減多餘為實
實 = abs(上率 - 下率)

# 置四節三節各半之
四節半 = Fraction(4, 2)
三節半 = Fraction(3, 2)

# 以減九節餘為法
法 = 總節數 - (四節半 + 三節半)

# 實如法得一升
一升 = Fraction(實, 法)

# 計算每節的容積
a = 下率  # 下初節
b = 下率 - 一升  # 下第二節
c = 下率 - 2 * 一升  # 下第三節
d = 下率 - 3 * 一升  # 中間第一節
e = 下率 - 4 * 一升  # 中間第二節
f = 上率 + 3 * 一升  # 上第一節
g = 上率 + 2 * 一升  # 上第二節
h = 上率 + 一升  # 上第三節
i = 上率  # 上第四節#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: 27/22
Variable 'c' has wrong value. Expected: 27/22, Actual: 37/33
Variable 'd' has wrong value. Expected: 37/33, Actual: 67/66
Variable 'e' has wrong value. Expected: 67/66, Actual: 10/11
Variable 'f' has wrong value. Expected: 10/11, Actual: 47/44
Variable 'g' has wrong value. Expected: 53/66, Actual: 127/132
Variable 'h' has wrong value. Expected: 23/33, Actual: 113/132
Variable 'i' has wrong value. Expected: 13/22, Actual: 3/4"""
