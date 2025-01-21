"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰善田 a畝 惡田 b畝 
"""

"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, if 1 qing (100 mu) is purchased for 10,000 qian, how much good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the price by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short of the price by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output (prices per mu) for the excess and deficit cases below each.
Multiply the rates of output by the respective excess and deficit amounts, and sum them to form the dividend.
Sum the excess and deficit amounts to form the divisor.
Divide the dividend by the divisor to find the unit amount. If there is a remainder, adjust it proportionally.
The excess and deficit amounts are then used to adjust the unit amount to find the quantities of the goods.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# Rates and values
善田價 = 300  # 善田每畝價
惡田價 = Fraction(500, 7)  # 惡田每畝價 (7畝500錢)

# 假設 20 畝善田，80 畝惡田，多 1714錢7分錢之2
善田1 = 20
惡田1 = 80
盈 = Fraction(1714) + Fraction(2, 7)

# 假設 10 畝善田，90 畝惡田，少 571錢7分錢之3
善田2 = 10
惡田2 = 90
不足 = Fraction(571) + Fraction(3, 7)

# 盈不足術
# 置所出率盈不足各居其下
所出率1 = 善田1 * 善田價 + 惡田1 * 惡田價
所出率2 = 善田2 * 善田價 + 惡田2 * 惡田價

# 令維乘所出率并以為實
實 = 盈 * 所出率2 + 不足 * 所出率1

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
單位量 = 實 / 法

# 善田和惡田
a = (單位量 - 不足) / (盈 - 不足) * 善田1
b = 100 - a  # 總田數為 100 畝

a, b  # 善田 a 畝, 惡田 b 畝
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 165
Variable 'b' has wrong value. Expected: 175/2, Actual: -65"""
