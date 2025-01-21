"""
今有蒲生一日長三尺莞生一日長一尺蒲生日自半莞生日自倍問幾何日而長等
術曰假令二日不足一尺五寸令之三日有餘一尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a日 各長 b尺 
"""

"""
Suppose there is a cattail (pu) that grows 3 chi in one day, and a rush (guan) that grows 1 chi in one day.
The cattail starts growing at half its height, and the rush starts growing at double its height.
Question: after how many days will they be of equal height?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun. Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficit" procedure says: Place the rates of growth under the excess and deficit respectively. Multiply the rates of growth by the excess and deficit, and add them to form the dividend. Add the excess and deficit to form the divisor. Divide the dividend by the divisor to find the number of days. If there is a remainder, simplify it. If the excess and deficit are the same, use the smaller rate of growth to adjust the result.

Answer: *a* days, and each grows to *b* chi.
"""

# 蒲生一日長三尺
蒲日長 = 3

# 莞生一日長一尺
莞日長 = 1

# 蒲生日自半
蒲初始 = Fraction(1, 2)

# 莞生日自倍
莞初始 = 2

# 盈不足術
# 假令二日不足一尺五寸
不足 = Fraction(1, 2) + 1  # 1 chi 5 cun = 1.5 chi

# 假令三日有餘一尺七寸半
有餘 = Fraction(7, 2) + 1  # 1 chi 7.5 cun = 1.75 chi

# 盈不足各居其下
盈 = 有餘
不足 = 不足

# 置所出率
蒲率 = 蒲日長
莞率 = 莞日長

# 盈不足相與同
盈不足和 = 盈 + 不足

# 維乘所出率并以為實
實 = (蒲率 * 不足) + (莞率 * 盈)

# 并盈不足為法
法 = 盈不足和

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = (蒲日長 * a) + 蒲初始  # Both will have the same height after `a` days.

a, b
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/2
Variable 'b' has wrong value. Expected: 63/13, Actual: 5"""
