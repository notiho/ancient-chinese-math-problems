"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=32/13)日 。各長 b(=63/13)尺 。
"""

"""
Suppose there is a cattail (pu) that grows 3 chi in one day, and a rush (guan) that grows 1 chi in one day.
The cattail starts growing from half its length, while the rush starts growing from double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun. Suppose 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficiency" procedure says: Place the rates of growth under the respective excess and deficiency. Multiply the rates by the respective excess or deficiency, and sum them to obtain the dividend. Sum the excess and deficiency to obtain the divisor. Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it. If the excess and deficiency are related to the same object, subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend. The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a*(=32/13) days. Each grows to *b*(=63/13) chi.
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
日數1 = 2
不足 = Fraction(1, 5 / 10)  # 1 chi 5 cun = 1.5 chi

# 令之三日，有餘一尺七寸半
日數2 = 3
有餘 = Fraction(1, 7.5 / 10)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 日數2 * 蒲日長 - 日數2 * 莞日長
不足率 = Fraction(1, 3)
"""
Code error: both arguments should be Rational instances"""
