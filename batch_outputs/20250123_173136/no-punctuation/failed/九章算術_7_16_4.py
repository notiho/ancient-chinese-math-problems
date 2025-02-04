"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰善田 a畝 惡田 b畝 
"""

"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, buying a total of 1 qing (100 mu) costs 10,000 qian.
Question: how many mu of good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the price by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short of the price by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output (prices per unit) under the excess and deficit respectively.
Multiply the rates of output by the respective excess and deficit, and add them together to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
If the excess and deficit are of the same type, adjust accordingly.
Finally, use the rates of output to calculate the quantities of the items.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

# 善田價 300 錢/畝
善田價 = 300

# 惡田價 500 錢/7 畝 -> 每畝價
惡田價 = Fraction(500, 7)

# 總價錢 10,000 錢
總價 = 10000

# 假令善田 20 畝，惡田 80 畝，多 1714 錢 2/7
善田1 = 20
惡田1 = 80
多1 = 1714 + Fraction(2, 7)

# 假令善田 10 畝，惡田 90 畝，不足 571 錢 3/7
善田2 = 10
惡田2 = 90
不足2 = 571 + Fraction(3, 7)

# 盈不足術
# 置所出率盈不足各居其下
率1 = 善田1 * 善田價 + 惡田1 * 惡田價
率2 = 善田2 * 善田價 + 惡田2 * 惡田價

# 令維乘所出率并以為實
實 = 多1 * abs(不足2) + abs(多1) * 不足2

# 并盈不足為法
法 = 多1 + abs(不足2)

# 實如法而一
善田數 = Fraction(實, 法)

# 善田數即為善田畝數
a = 善田數

# 惡田數 = 總田數 - 善田數
b = 100 - a
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 6000/7
Variable 'b' has wrong value. Expected: 175/2, Actual: -5300/7"""
