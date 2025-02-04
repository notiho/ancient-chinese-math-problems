"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu, worth 300 coins, and poor farmland, 7 mu, worth 500 coins.
Now, buying 1 qing (100 mu) together costs 10,000 coins.
Question: how many mu of good and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland, resulting in an excess of 1714 coins and 2/7 of a coin.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland, resulting in a deficit of 571 coins and 3/7 of a coin.

The method of excess and deficit says: Place the rates of the outcomes, with the excess and deficit below them respectively.
Multiply the rates by the outcomes, summing them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the result.
If there are fractions, handle them accordingly.
For the excess and deficit corresponding to the same purchased item, place the rates of the outcomes, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend represents the price of the item, and the divisor represents the total number of items.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# 善田價錢與惡田價錢
善田價 = 300
惡田價 = Fraction(500, 7)

# 假設情況 1：善田 20 畝，惡田 80 畝，多 1714 錢，7分錢之2
善田1 = 20
惡田1 = 80
盈 = Fraction(1714) + Fraction(2, 7)

# 假設情況 2：善田 10 畝，惡田 90 畝，不足 571 錢，7分錢之3
善田2 = 10
惡田2 = 90
不足 = Fraction(571) + Fraction(3, 7)

# 盈不足術計算
# 置所出率，盈、不足各居其下
率1 = 善田1 * 善田價 + 惡田1 * 惡田價
率2 = 善田2 * 善田價 + 惡田2 * 惡田價

# 令維乘所出率，并以為實
實 = 盈 * 率2 + 不足 * 率1

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
善田 = Fraction(實, 法)

# 計算善田與惡田
a = Fraction(善田)
b = 100 - a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 10000
Variable 'b' has wrong value. Expected: 175/2, Actual: -9900"""
