"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰善田 a畝 惡田 b畝 
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu of which costs 300 qian, and poor farmland, 7 mu of which costs 500 qian.
Now, buying 1 qing (100 mu) costs 10,000 qian.
Question: how many mu of good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland.
This exceeds the target by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland.
This falls short of the target by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output (cost per mu) under the excess and deficit values.
Multiply the rates of output by the respective excess or deficit values, and sum them up to form the dividend.
Sum the excess and deficit values to form the divisor.
Divide the dividend by the divisor to find the result.
If there is a fraction, resolve it.
The excess and deficit values are then used to adjust the result.
Finally, use the rates of output to determine the quantities of the goods.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

# Known values
善田價 = 300  # 善田每畝價
惡田價 = Fraction(500, 7)  # 惡田每畝價

總畝數 = 100  # 一頃 = 100 畝
總價錢 = 10000  # 總價錢

# 假令善田 20 畝，惡田 80 畝，多 1714 錢 7分錢之2
盈善田 = 20
盈惡田 = 80
盈多 = 1714 + Fraction(2, 7)

# 假令善田 10 畝，惡田 90 畝，不足 571 錢 7分錢之3
不足善田 = 10
不足惡田 = 90
不足少 = 571 + Fraction(3, 7)

# 盈不足術
# 置所出率 (善田價與惡田價)
盈率 = 善田價 * 盈善田 + 惡田價 * 盈惡田
不足率 = 善田價 * 不足善田 + 惡田價 * 不足惡田

# 盈不足各居其下
盈實 = 盈多 * 不足率
不足實 = 不足少 * 盈率

# 并以為實
實 = 盈實 + 不足實

# 并盈不足為法
法 = 盈多 + 不足少

# 實如法而一
善田數 = Fraction(實, 法)

# 善田數
a = 善田數

# 惡田數
b = 總畝數 - a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 10000
Variable 'b' has wrong value. Expected: 175/2, Actual: -9900"""
