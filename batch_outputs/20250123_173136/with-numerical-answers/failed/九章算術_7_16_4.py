"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a(=25/2)畝 ，惡田 b(=175/2)畝 。
"""

"""
Suppose there is good land, 1 mu, valued at 300 qian; and poor land, 7 mu, valued at 500 qian.
Now, buying 1 qing (100 mu) together costs 10,000 qian.
Question: how much good land and poor land are there respectively?

The procedure says: Suppose there are 20 mu of good land and 80 mu of poor land. This exceeds the price by 1714 qian and 2/7 qian.
Suppose there are 10 mu of good land and 90 mu of poor land. This falls short of the price by 571 qian and 3/7 qian.

The "Excess and Deficit" procedure says: Place the rates of output, with the excess and deficit each below their respective rates.
Multiply the rates of output by their respective excess or deficit, and add them together to form the dividend.
Add the excess and deficit together to form the divisor.
Divide the dividend by the divisor to find 1 unit. If there are fractions, handle them accordingly.
For the good and poor land, place the rates of output. Subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: *a*(=25/2) mu of good land, and *b*(=175/2) mu of poor land.
"""

from fractions import Fraction

# 善田價
善田價 = 300

# 惡田價
惡田價 = Fraction(500, 7)

# 總價
總價 = 10000

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二
善田1 = 20
惡田1 = 80
多1 = 1714 + Fraction(2, 7)

# 令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三
善田2 = 10
惡田2 = 90
不足2 = 571 + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = 善田1 * 善田價 + 惡田1 * 惡田價
率2 = 善田2 * 善田價 + 惡田2 * 惡田價

# 令維乘所出率，并以為實
實 = 多1 * 率2 + 不足2 * 率1

# 并盈、不足為法
法 = 多1 + 不足2

# 實如法而一
善田 = Fraction(實, 法)

# 善田數
a = 善田 / 善田價  # 善田數 (25/2)

# 惡田數
b = 100 - a  # 惡田數 (175/2)
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 100/3
Variable 'b' has wrong value. Expected: 175/2, Actual: 200/3"""
