"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
Suppose there is good farmland, 1 mu, worth 300 coins; and poor farmland, 7 mu, worth 500 coins.
Now, buying 1 qing (100 mu) together costs 10,000 coins.
Question: how many mu of good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland, resulting in an excess of 1714 coins and 2/7 of a coin.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland, resulting in a deficit of 571 coins and 3/7 of a coin.

The method of excess and deficit says: Place the rates of output (good and poor farmland) with the excess and deficit below them, respectively.
Multiply the rates of output by their respective excess or deficit, and sum them to obtain the dividend.
Sum the excess and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result.
If there are fractions, handle them accordingly.
For the good and poor farmland, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the farmland, and the divisor represents the total number of mu.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# 善田價錢率
善田價 = 300

# 惡田價錢率
惡田價 = Fraction(500, 7)

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二
善田_1 = 20
惡田_1 = 80
盈 = Fraction(1714) + Fraction(2, 7)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三
善田_2 = 10
惡田_2 = 90
不足 = Fraction(571) + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
所出率_1 = 善田_1 * 善田價 + 惡田_1 * 惡田價
所出率_2 = 善田_2 * 善田價 + 惡田_2 * 惡田價

# 令維乘所出率，并以為實
實 = 盈 * 所出率_2 + 不足 * 所出率_1

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
結果 = Fraction(實, 法)

# 善田和惡田的比例
善田比例 = 善田_1 - 善田_2
惡田比例 = 惡田_2 - 惡田_1

# 善田 a畝，惡田 b畝
a = 善田比例 * 結果
b = 惡田比例 * 結果
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 100000
Variable 'b' has wrong value. Expected: 175/2, Actual: 100000"""
