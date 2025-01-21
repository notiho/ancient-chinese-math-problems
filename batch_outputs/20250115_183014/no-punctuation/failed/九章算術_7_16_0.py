"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰善田 a畝 惡田 b畝 
"""

"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, a total of 1 qing of land is purchased for 10,000 qian.
Question: how much good farmland and poor farmland are there respectively?

The procedure for the excess and deficiency method says:
Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds by 1714 qian and 7/10 qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short by 571 qian and 3/10 qian.
Place the rates of output (excess and deficiency) below each case.
Multiply the rates of output by the respective excess or deficiency and combine them into a dividend.
Combine the excess and deficiency into a divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, adjust it.
The excess and deficiency are then used to determine the respective amounts of the purchased items.
Place the rates of output, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the value of the items, and the divisor becomes the number of people.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# Known values
善田價 = 300  # Good farmland price per mu
惡田價 = Fraction(500, 7)  # Poor farmland price per mu
總價 = 10000  # Total price in qian
總畝 = 100  # Total land in mu (1 qing = 100 mu)

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢七分錢之二
善田假1 = 20
惡田假1 = 總畝 - 善田假1
多1 = Fraction(1714, 1) + Fraction(7, 10)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢七分錢之三
善田假2 = 10
惡田假2 = 總畝 - 善田假2
不足2 = Fraction(571, 1) + Fraction(3, 10)

# 盈不足術
# 置所出率盈不足各居其下
率1 = 善田假1 * 善田價 + 惡田假1 * 惡田價
率2 = 善田假2 * 善田價 + 惡田假2 * 惡田價

# 令維乘所出率并以為實
實 = 多1 * 不足2

# 并盈不足為法
法 = 多1 + 不足2

# 實如法而一
善田 = Fraction(實, 法)

# 善田數量
a = 善田

# 惡田數量
b = 總畝 - a
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 97960811/228600
Variable 'b' has wrong value. Expected: 175/2, Actual: -75100811/228600"""
