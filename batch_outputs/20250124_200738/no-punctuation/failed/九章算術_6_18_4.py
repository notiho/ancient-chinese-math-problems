"""
今有竹九節下三節容四升上四節容三升問中間二節欲均容各多少
術曰以下三節分四升為下率以上四節分三升為上率上下率以少減多餘為實置四節三節各半之以減九節餘為法實如法得一升即衰相去也下率一升少半升者下第二節容也
荅曰下初 a升 次 b升 次 c升 次 d升 次 e升 次 f升 次 g升 次 h升 次 i升 
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: how much should the middle 2 nodes hold if they are to hold an equal amount?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to obtain the bottom rate.
Divide the 3 sheng among the top 4 nodes to obtain the top rate.
Subtract the smaller rate from the larger rate to obtain the difference, which is the dividend.
Place the 4 nodes and 3 nodes, each halved, and subtract them from the 9 nodes to obtain the divisor.
Divide the dividend by the divisor to obtain 1 sheng, which is the rate of decrease between adjacent nodes.
Subtract half a sheng from the bottom rate to get the amount for the second node from the bottom.

Answer: The bottom node holds *a* sheng, the second node holds *b* sheng, ..., and the top node holds *i* sheng.
"""

# 下三節容四升
下節數 = 3
下容積 = 4

# 上四節容三升
上節數 = 4
上容積 = 3

# 中間二節
中節數 = 2

# 以下三節分四升為下率
下率 = Fraction(下容積, 下節數)

# 以上四節分三升為上率
上率 = Fraction(上容積, 上節數)

# 上下率以少減多餘為實
實 = abs(下率 - 上率)

# 置四節三節各半之
半下節數 = Fraction(下節數, 2)
半上節數 = Fraction(上節數, 2)

# 以減九節餘為法
法 = 9 - (半下節數 + 半上節數)

# 實如法得一升，即衰相去也
衰相去 = Fraction(實, 法)

# 計算每節的容積
a = 下率
b = 下率 - 衰相去
c = b - 衰相去
d = c - 衰相去
e = d - 衰相去
f = e - 衰相去
g = f - 衰相去
h = g - 衰相去
i = h - 衰相去#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: 27/22
Variable 'c' has wrong value. Expected: 27/22, Actual: 37/33
Variable 'd' has wrong value. Expected: 37/33, Actual: 67/66
Variable 'e' has wrong value. Expected: 67/66, Actual: 10/11
Variable 'f' has wrong value. Expected: 10/11, Actual: 53/66
Variable 'g' has wrong value. Expected: 53/66, Actual: 23/33
Variable 'h' has wrong value. Expected: 23/33, Actual: 13/22
Variable 'i' has wrong value. Expected: 13/22, Actual: 16/33"""
