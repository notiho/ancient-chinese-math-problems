"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
Suppose there is good farmland, 1 mu, priced at 300 qian; and poor farmland, 7 mu, priced at 500 qian.
Now, if 1 qing (100 mu) is purchased together for 10,000 qian, how much of it is good farmland and how much is poor farmland?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the price by 1714 qian and 2/7 of 1 qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short of the price by 571 qian and 3/7 of 1 qian.

The "Excess and Deficit" procedure says: Place the rates of output (prices per mu) for the excess and deficit cases, with the excess and deficit amounts below them.
Multiply the rates of output by their respective excess or deficit amounts, and sum these to form the dividend.
Sum the excess and deficit amounts to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, handle it accordingly.
For the good and poor farmland, place the rates of output, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the price of the farmland, and the divisor represents the total number of mu.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# 善田價率
善田價率 = 300

# 惡田價率
惡田價率 = Fraction(500, 7)

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二
善田_假1 = 20
惡田_假1 = 80
多1 = 1714 + Fraction(2, 7)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三
善田_假2 = 10
惡田_假2 = 90
不足2 = 571 + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
所出率1 = 善田_假1 * 善田價率 + 惡田_假1 * 惡田價率
所出率2 = 善田_假2 * 善田價率 + 惡田_假2 * 惡田價率

# 令維乘所出率，并以為實
實 = 多1 * 所出率2 + 不足2 * 所出率1

# 并盈、不足為法
法 = 多1 + 不足2

# 實如法而一
善田 = Fraction(實, 法)

# 善田面積
a = Fraction(善田,善田).
"""
Code error: invalid syntax (<string>, line 52)"""
