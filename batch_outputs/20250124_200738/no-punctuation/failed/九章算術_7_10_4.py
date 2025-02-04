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
Question: after how many days will they be of equal length?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun. 
Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "excess and deficiency" procedure says: Place the rates of growth and the excess and deficiency below them.
Multiply the rates of growth by their respective excess or deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days. If there is a fraction, simplify it.
If the excess and deficiency are equal, the rates of growth are used to adjust the calculation.

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
不足日數 = 2
不足差 = 1 + Fraction(5, 10)  # 1 chi 5 cun

# 假令三日有餘一尺七寸半
有餘日數 = 3
有餘差 = 1 + Fraction(7, 10) + Fraction(5, 20)  # 1 chi 7.5 cun

# 盈不足術
# 置所出率盈不足各居其下
所出率 = [蒲日長 - 莞日長, 蒲日長 - 莞日長]  # Growth rate difference
盈不足 = [不足差, 有餘差]  # Excess and deficiency

# 令維乘所出率并以為實
實 = (所出率[0] * 盈不足[1]) + (所出率[1] * 盈不足[0])

# 并盈不足為法
法 = 盈不足[0] + 盈不足[1]

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = 蒲初長 + a * 蒲日長  # Length of either plant after `a` days (they are equal at this point)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 2
Variable 'b' has wrong value. Expected: 63/13, Actual: 13/2"""
