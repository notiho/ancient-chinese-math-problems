"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu, worth 300 coins; and poor farmland, 7 mu, worth 500 coins.
Now, buying 1 qing (100 mu) together costs 10,000 coins.
Question: how much good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland, resulting in an excess of 1714 2/7 coins.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland, resulting in a deficit of 571 3/7 coins.

The method of excess and deficit says: Place the rates of the outcomes, with the excess and deficit below each.
Multiply the rates by their respective outcomes, summing them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain 1 unit.
If there are fractions, adjust them.
For the excess and deficit corresponding to the same purchased item, place the rates of the outcomes, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# 善田價三百，惡田價五百
善田價 = 300
惡田價 = 500

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二
善田_假1 = 20
惡田_假1 = 80
多1 = Fraction(1714 * 7 + 2, 7)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三
善田_假2 = 10
惡田_假2 = 90
不足2 = Fraction(571 * 7 + 3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = 善田_假1 * 善田價 + 惡田_假1 * 惡田價
率2 = 善田_假2 * 善田價 + 惡田_假2 * 惡田價

# 令維乘所出率，并以為實
實 = 多1 * 率2 + 不足2 * 率1

# 并盈、不足為法
法 = 多1 + 不足2

# 實如法而一
一單位 = Fraction(實, 法)

# 善田 a畝，惡田 b畝
a = Fraction(善田_假1 * 不足2 + 善田_假2 * 多1, 多1 + 不足2)
b = 100 - a#----- content ends here -----

"""
"""
