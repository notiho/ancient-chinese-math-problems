"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a(=25/2)畝 ，惡田 b(=175/2)畝 。
"""

"""
Suppose there is good land, 1 mu, priced at 300 qian; and poor land, 7 mu, priced at 500 qian.
Now, suppose 1 qing of land is purchased together for 10,000 qian.
Question: how much good land and poor land are there respectively?

The procedure says: Suppose there are 20 mu of good land and 80 mu of poor land, resulting in an excess of 1714 qian and 2/7 qian.
Suppose there are 10 mu of good land and 90 mu of poor land, resulting in a deficit of 571 qian and 3/7 qian.

The procedure for excess and deficit says: Place the rates of output, with the excess and deficit placed below them respectively.
Multiply the rates of output by their respective excess or deficit, and add them to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain 1 unit.
If there are fractions, convert them.
For the good land and poor land, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the land, and the divisor becomes the number of people.

Answer: *a*(=25/2) mu of good land, and *b*(=175/2) mu of poor land.
"""

from fractions import Fraction

# 善田價三百
善田價 = 300

# 惡田價五百
惡田價 = 500

# 一頃 = 100 畝
總畝數 = 100

# 總價錢一萬
總價 = 10000

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二
善田_假1 = 20
惡田_假1 = 80
多1 = Fraction(1714, 1) + Fraction(2, 7)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三
善田_假2 = 10
惡田_假2 = 90
不足2 = Fraction(571, 1) + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = 善田_假1 * 善田價 + 惡田_假1 * 惡田價
率2 = 善田_假2 * 善田價 + 惡田_假2 * 惡田價

# 令維乘所出率，并以為實
實 = 多1 * rate2 + 不足2 * rate1

# 并盈、不足為法
法 = 多1 + 不足2

# 實如法而一
一畝善田 = Fraction(實, 法)

# 善田
a = Fraction(善田價 * 一畝善田
"""
Code error: '(' was never closed (<string>, line 60)"""
