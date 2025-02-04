"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=32/13)日 。各長 b(=63/13)尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (pu) that grows 3 chi in one day, and a rush (guan) that grows 1 chi in one day.
The cattail starts growing from half its length, and the rush starts growing from double its length.
Question: after how many days will they be of equal length?

The procedure says: Suppose after 2 days, the difference is less than 1 chi 5 cun.
Suppose after 3 days, the difference exceeds 1 chi 7.5 cun.

The "excess and deficiency" procedure says: Place the growth rates under the excess and deficiency values respectively.
Multiply the rates by the respective excess and deficiency values, and sum them to obtain the dividend.
Sum the excess and deficiency values to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a remainder, simplify it.
For the lengths, multiply the number of days by the growth rates, and adjust for the starting lengths.

Answer: *a*(=32/13) days. Each grows to *b*(=63/13) chi.
"""

# 蒲生一日，長三尺
蒲日長 = 3

# 莞生一日，長一尺
莞日長 = 1

# 蒲生日自半
蒲初長 = Fraction(1, 2)

# 莞生日自倍
莞初長 = 2

# 假令二日，不足一尺五寸
不足日數 = 2
不足差 = Fraction(15, 10)  # 1 chi 5 cun = 1.5 chi

# 令之三日，有餘一尺七寸半
有餘日數 = 3
有餘差 = Fraction(17.5, 10)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
不足率 = 蒲日長 * 不足日數 - 莞日長 * 不足日數
有餘率 = 蒲日長 * 有餘日數 - 莞日長 * 有餘日數

# 令維乘所出率，并以為實
實 = 不足差 * 有餘率 + 有餘差 * 不足率

# 并盈、不足為法
法 = 有餘差 + 不足差

# 實如法而一
a = Fraction(實, 法)  # 32/13 days

# 各長
蒲長 = 蒲初長 + a * 蒲日長
莞長 = 莞初長 + a * 莞日長
b = 蒲長  # 63/13 chi (both lengths are equal at this point)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
