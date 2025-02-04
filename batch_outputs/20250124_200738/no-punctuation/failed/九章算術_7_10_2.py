"""
今有蒲生一日長三尺莞生一日長一尺蒲生日自半莞生日自倍問幾何日而長等
術曰假令二日不足一尺五寸令之三日有餘一尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a日 各長 b尺 
"""

#----- content starts here -----
"""
Suppose there is a cattail (pu) that grows 3 chi per day and a rush (guan) that grows 1 chi per day.
The cattail starts growing from half its length, and the rush starts growing from double its length.
Question: after how many days will they have the same length?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun. 
Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficit" procedure says: Place the rates of growth under the respective excess and deficit.
Multiply the rates of growth by the respective excess and deficit, and add them together to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a fraction, simplify it.
If the excess and deficit are the same, use the rates of growth to calculate the common length.

Answer: *a* days, and each grows to *b* chi.
"""

# 蒲生一日長三尺
蒲日長 = 3

# 莞生一日長一尺
莞日長 = 1

# 蒲生日自半
蒲初長 = Fraction(1, 2)

# 莞生日自倍
莞初長 = 2

# 假令二日不足一尺五寸
不足 = Fraction(15, 10)  # 1 chi 5 cun = 1.5 chi

# 假令三日有餘一尺七寸半
有餘 = Fraction(17.5, 10)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率盈不足各居其下
盈率 = 蒲日長 - 莞日長  # Rate of growth difference
不足率 = 不足
有餘率 = 有餘

# 令維乘所出率并以為實
實 = (盈率 * 不足率) + (盈率 * 有餘率)

# 并盈不足為法
法 = 不足率 + 有餘率

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = (蒲日長 * a) + 蒲初長  # Length after `a` days

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
