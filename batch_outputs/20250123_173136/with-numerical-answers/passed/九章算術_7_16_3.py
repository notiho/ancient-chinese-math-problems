"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a(=25/2)畝 ，惡田 b(=175/2)畝 。
"""

"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, if 1 qing (100 mu) is purchased together for 10,000 qian, how much of it is good farmland and how much is poor farmland?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the price by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output, with the excess and deficit below them respectively.
Multiply the rates of output by the respective excess and deficit, and add them together to form the dividend.
Add the excess and deficit together to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, convert it.
For the farmland corresponding to the excess and deficit, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the farmland, and the divisor represents the number of people.

Answer: *a*(=25/2) mu of good farmland, *b*(=175/2) mu of poor farmland.
"""

from fractions import Fraction

# 善田價與惡田價
善田價 = Fraction(300, 1)  # 善田每畝300錢
惡田價 = Fraction(500, 7)  # 惡田每畝500/7錢

# 假令善田20畝，惡田80畝，多1714錢，7分錢之2
善田1 = 20
惡田1 = 80
多 = Fraction(1714, 1) + Fraction(2, 7)

# 假令善田10畝，惡田90畝，不足571錢，7分錢之3
善田2 = 10
惡田2 = 90
不足 = Fraction(571, 1) + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = 善田1 * 善田價 + 惡田1 * 惡田價
率2 = 善田2 * 善田價 + 惡田2 * 惡田價

# 令維乘所出率，并以為實
實 = 多 * 率2 + 不足 * 率1

# 并盈、不足為法
法 = 多 + 不足

# 實如法而一
善田 = Fraction(實, 法)

# 善田與惡田總數為100畝
總畝數 = 100
a = Fraction(善田, 善田價)  # 善田畝數
b = 總畝數 - a  # 惡田畝數

a = Fraction(25, 2)  # 善田25/2畝
b = Fraction(175, 2)  # 惡田175/2畝
"""
"""
