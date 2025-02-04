"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰善田 a畝 惡田 b畝 
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, buying 1 qing (100 mu) of land together costs 10,000 qian.
Question: how many mu of good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland, resulting in an excess of 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland, resulting in a deficit of 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output (excess and deficit) below their respective assumptions.
Multiply the rates of output by their respective assumptions and add them together to form the dividend.
Add the excess and deficit together to form the divisor.
Divide the dividend by the divisor to find the unit value. If there is a fraction, simplify it.
The excess and deficit are then adjusted to match the total purchase amount.
Place the rates of output, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend represents the value of the goods, and the divisor represents the total number of units.

Answer: the good farmland is *a* mu, and the poor farmland is *b* mu.
"""

from fractions import Fraction

# Known values
善田價 = 300  # 善田每畝價
惡田價 = Fraction(500, 7)  # 惡田每畝價
總價 = 10000  # 總價錢
總畝 = 100  # 總畝數 (1頃 = 100畝)

# 假設 1: 善田 20 畝，惡田 80 畝
善田假設1 = 20
惡田假設1 = 80
假設1_總價 = 善田假設1 * 善田價 + 惡田假設1 * 惡田價
盈 = 假設1_總價 - 總價  # 盈餘

# 假設 2: 善田 10 畝，惡田 90 畝
善田假設2 = 10
惡田假設2 = 90
假設2_總價 = 善田假設2 * 善田價 + 惡田假設2 * 惡田價
不足 = 總價 - 假設2_總價  # 不足

# 盈不足術
# 盈不足各居其下
盈 = Fraction(1714, 1) + Fraction(2, 7)  # 盈餘
不足 = Fraction(571, 1) + Fraction(3, 7)  # 不足

# 令維乘所出率并以為實
實 = 盈 * 善田假設2 + 不足 * 善田假設1

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
善田 = 實 / 法

# 惡田 = 總畝 - 善田
惡田 = 總畝 - 善田

# Final answer
a = 善田
b = 惡田#----- content ends here -----

"""
"""
