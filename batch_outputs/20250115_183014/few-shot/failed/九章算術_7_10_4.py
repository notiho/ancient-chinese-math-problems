"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。各長 b尺 。
"""

"""
Suppose a cattail grows 3 chi per day, and a rush grows 1 chi per day.
The cattail starts at half its length on the first day, and the rush starts at double its length on the first day.
Question: after how many days will their lengths be equal?

The procedure says: Assume for 2 days, the difference is less than 1 chi 5 cun. Assume for 3 days, the difference is more than 1 chi 7.5 cun.
The procedure for excess and deficiency says: Place the rates of growth, with the excess and deficiency below each. Multiply the rates of growth by the excess and deficiency, summing them to form the dividend. Sum the excess and deficiency to form the divisor. Divide the dividend by the divisor to find the answer. If there is a fraction, simplify it. For problems involving buying goods, place the rates of growth, subtract the smaller from the larger, and reduce the dividend and divisor. The dividend becomes the price of the goods, and the divisor becomes the number of people.

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
不足 = Fraction(1, 5, 10)  # 1 chi 5 cun = 1.5 chi

# 令之三日，有餘一尺七寸半
有餘 = Fraction(1, 7, 20)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 3 * 有餘
不足率 = 1 * 不足

# 令維乘所出率，并以為實
實 = 盈率 + 不足率

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = 蒲初長 + a * 蒲日長  # Length of either plant after a days

a, b
"""
Code error: Fraction.__new__() takes from 1 to 3 positional arguments but 4 were given"""
