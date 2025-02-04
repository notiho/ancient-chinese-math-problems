"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

"""
Suppose a cattail (pu) grows 3 chi in one day, and a rush (guan) grows 1 chi in one day.
The cattail starts at half its length, and the rush starts at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun.
Suppose for 3 days, the difference exceeds 1 chi 7 cun and a half.

The procedure for excess and deficiency says: Place the growth rates, with the excess and deficiency below them respectively.
Multiply the growth rates by the respective excess and deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a remainder, simplify it.
If the excess and deficiency correspond to the same item, place the growth rates, subtract the smaller from the larger, and reduce the remainder with the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# 蒲生一日，長三尺
蒲日長 = 3

# 莞生一日，長一尺
莞日長 = 1

# 蒲生日自半
蒲初長 = Fraction(1, 2)

# 莞生日自倍
莞初長 = 2

# 假令二日，不足一尺五寸
不足日 = 2
不足差 = Fraction(1, 5)  # 1 chi 5 cun = 1.5 chi

# 令之三日，有餘一尺七寸半
有餘日 = 3
有餘差 = Fraction(17, 10)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 有餘日
不足率 = 不足日

# 令維乘所出率，并以為實
盈實 = 盈率 * 不足差
不足實 = 不足率 * 有餘差
實 = 盈實 + 不足實

# 并盈、不足為法
法 = 盈率 + 不足率

# 實如法而一
a = Fraction(實, 法)

# 各長 b尺
b = 蒲初長 + a * 蒲日長  # Both will have the same length at this point

a日 = a
b尺 = b
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 4/5
Variable 'b' has wrong value. Expected: 63/13, Actual: 29/10"""
