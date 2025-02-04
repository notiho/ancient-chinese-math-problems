"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a(=25/2)畝 ，惡田 b(=175/2)畝 。
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, buying 1 qing (100 mu) together costs 10,000 qian.
Question: how many mu of good and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the price by 1714 qian and 2/7 qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short of the price by 571 qian and 3/7 qian.

The method of excess and deficiency says: Place the rates of output, with the excess and deficiency below each.
Multiply the rates of output by their respective excess or deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain 1 unit.
If there are fractions, adjust them.
For the excess and deficiency corresponding to the same item being purchased, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=25/2) mu of good farmland, *b*(=175/2) mu of poor farmland.
"""

from fractions import Fraction

# 善田價率
善田價率 = 300

# 惡田價率
惡田價率 = Fraction(500, 7)

# 總價
總價 = 10000

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二
善田1 = 20
惡田1 = 80
多1 = Fraction(1714, 1) + Fraction(2, 7)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三
善田2 = 10
惡田2 = 90
不足2 = Fraction(571, 1) + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = 善田1 * 善田價率 + 惡田1 * 惡田價率
率2 = 善田2 * 善田價率 + 惡田2 * 惡田價率

# 令維乘所出率，并以為實
實 = 多1 * 率2 + 不足2 * 率1

# 并盈、不足為法
法 = 多1 + 不足2

# 實如法而一
單位 = 實 / 法

# 善田
a = (總價 - 惡田價率 * 100) / (善田價率 - 惡田價率) # 25/2

# 惡田
b = 100 - a # 175/2#----- content ends here -----

"""
"""
