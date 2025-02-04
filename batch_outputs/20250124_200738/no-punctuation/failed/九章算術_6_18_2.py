"""
今有竹九節下三節容四升上四節容三升問中間二節欲均容各多少
術曰以下三節分四升為下率以上四節分三升為上率上下率以少減多餘為實置四節三節各半之以減九節餘為法實如法得一升即衰相去也下率一升少半升者下第二節容也
荅曰下初 a升 次 b升 次 c升 次 d升 次 e升 次 f升 次 g升 次 h升 次 i升 
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: for the middle 2 nodes, how much should each hold to make the distribution even?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to get the lower rate.
Divide the 3 sheng among the top 4 nodes to get the upper rate.
Subtract the smaller rate from the larger rate, the remainder is the dividend.
Place the 4 nodes and 3 nodes, each halved, and subtract this from the 9 nodes, the remainder is the divisor.
Divide the dividend by the divisor to get 1 sheng, which is the difference between successive nodes.
For the lower rate, subtract half a sheng to get the second node's capacity.

The answer says: the first node holds *a* sheng, the second node holds *b* sheng, ..., the ninth node holds *i* sheng.
"""

# 下三節容四升
下節數 = 3
下升數 = 4

# 上四節容三升
上節數 = 4
上升數 = 3

# 中間二節
中節數 = 2

# 以下三節分四升為下率
下率 = Fraction(下升數, 下節數)

# 以上四節分三升為上率
上率 = Fraction(上升數, 上節數)

# 上下率以少減多餘為實
實 = abs(下率 - 上率)

# 置四節三節各半之以減九節餘為法
法 = 9 - (下節數 / 2 + 上節數 / 2)

# 實如法得一升即衰相去也
衰 = Fraction(實, 法)

# 計算每節的容量
a = 下率 + 2 * 衰  # 下初
b = 下率 + 衰      # 下次
c = 下率           # 下次
d = 下率 - 衰      # 中初
e = 下率 - 2 * 衰  # 中次
f = 上率 + 2 * 衰  # 上初
g = 上率 + 衰      # 上次
h = 上率           # 上次
i = 上率 - 衰      # 上次#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
