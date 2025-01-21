"""
今有蒲生一日長三尺莞生一日長一尺蒲生日自半莞生日自倍問幾何日而長等
術曰假令二日不足一尺五寸令之三日有餘一尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a日 各長 b尺 
"""

"""
Suppose there are two plants: the pu grows 3 chi per day, and the guan grows 1 chi per day.
The pu starts growing from half its length, and the guan starts growing from double its length.
Question: after how many days will they be of equal length?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun. 
Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficiency" procedure says: Place the rates of growth under the respective excess and deficiency.
Multiply the rates of growth by the respective excess and deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a remainder, simplify it.
If the excess and deficiency are the same, place the rates of growth, subtract the smaller from the larger, and simplify the divisor and dividend.
The result is the number of days.
The answer says: *a* days, and each plant grows to *b* chi.
"""

# 蒲生一日長三尺
蒲日長 = 3

# 莞生一日長一尺
莞日長 = 1

# 蒲生日自半
蒲初長 = Fraction(1, 2)

# 莞生日自倍
莞初長 = 2

# 盈不足術
# 假令二日不足一尺五寸
盈 = Fraction(15, 10)  # 1 chi 5 cun = 1.5 chi
盈日 = 2

# 假令三日有餘一尺七寸半
不足 = Fraction(17.5, 10)  # 1 chi 7.5 cun = 1.75 chi
不足日 = 3

# 置所出率盈不足各居其下
盈率 = 蒲日長 - 莞日長
不足率 = 蒲日長 - 莞日長

# 令維乘所出率并以為實
盈實 = 盈 * 不足率
不足實 = 不足 * 盈率
實 = 盈實 + 不足實

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = 蒲初長 + a * 蒲日長  # Both plants will have the same length after `a` days

a, b
"""
Code error: both arguments should be Rational instances"""
