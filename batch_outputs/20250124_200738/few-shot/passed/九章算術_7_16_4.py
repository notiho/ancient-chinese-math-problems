"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

#----- content starts here -----
"""
Suppose there is good land, 1 mu, priced at 300 qian; and poor land, 7 mu, priced at 500 qian.
Now, buying 1 qing of land in total costs 10,000 qian.
Question: how many mu of good land and poor land are there?

The procedure says: Suppose there are 20 mu of good land and 80 mu of poor land, resulting in an excess of 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good land and 90 mu of poor land, resulting in a deficit of 571 qian and 3/7 of a qian.

The method of excess and deficit says: Place the rates of the outcomes, with the excess and deficit below them, respectively.
Multiply the rates by the outcomes, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the unit.
If there are fractions, adjust them.
For the excess and deficit corresponding to the same purchased item, place the rates of the outcomes, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of units.

Answer: *a* mu of good land, *b* mu of poor land.
"""

from fractions import Fraction

# Known values
善田價 = 300  # 善田每畝價
惡田價 = Fraction(500, 7)  # 惡田每畝價 (7畝價500錢)
總價 = 10000  # 總價錢
總畝 = 100  # 一頃 = 100畝

# 假設 1: 善田 20 畝，惡田 80 畝
善田1 = 20
惡田1 = 總畝 - 善田1
假設1_價 = 善田1 * 善田價 + 惡田1 * 惡田價
盈 = 假設1_價 - 總價  # 盈餘

# 假設 2: 善田 10 畝，惡田 90 畝
善田2 = 10
惡田2 = 總畝 - 善田2
假設2_價 = 善田2 * 善田價 + 惡田2 * 惡田價
不足 = 總價 - 假設2_價  # 不足

# 盈不足術
盈不足_法 = 盈 + 不足
盈不足_實 = 善田1 * 不足 + 善田2 * 盈
善田 = Fraction(盈不足_實, 盈不足_法)

# 計算惡田
惡田 = 總畝 - 善田

# 答案
a = 善田
b = 惡田#----- content ends here -----

"""
"""
