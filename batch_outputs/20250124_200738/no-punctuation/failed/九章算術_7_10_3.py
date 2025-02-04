"""
今有蒲生一日長三尺莞生一日長一尺蒲生日自半莞生日自倍問幾何日而長等
術曰假令二日不足一尺五寸令之三日有餘一尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a日 各長 b尺 
"""

#----- content starts here -----
"""
Suppose there is a cattail (pu) that grows 3 chi in one day, and a rush (guan) that grows 1 chi in one day.
The cattail starts growing at half its length, and the rush starts growing at double its length.
Question: after how many days will they be of equal length?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun.
Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "excess and deficiency" procedure says: Place the rates of growth under the respective excess and deficiency.
Multiply the rates of growth by the respective excess and deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
If the excess and deficiency are of the same type, adjust accordingly.

Answer: *a* days, and each grows to *b* chi.
"""

from fractions import Fraction

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
不足 = Fraction(1, 2) * 2 * 蒲日長 - 2 * 莞日長 - Fraction(1, 5)

# 假令三日有餘一尺七寸半
有餘 = Fraction(1, 2) * 3 * 蒲日長 - 3 * 莞日長 + Fraction(1, 2) + Fraction(1, 20)

# 盈不足各居其下
盈率 = 3
不足率 = 2

# 令維乘所出率并以為實
實 = 盈率 * abs(不足) + 不足率 * abs(有餘)

# 并盈不足為法
法 = abs(不足) + abs(有餘)

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = 蒲初長 + a * 蒲日長

a = a.limit_denominator()
b = b.limit_denominator()#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 130/57
Variable 'b' has wrong value. Expected: 63/13, Actual: 279/38"""
