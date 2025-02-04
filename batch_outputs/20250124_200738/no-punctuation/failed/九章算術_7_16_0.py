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

The procedure says: 
Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the target by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short of the target by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says:
Place the rates of output (the prices per mu) for excess and deficit below their respective cases.
Multiply the rates of output by the respective excess and deficit, and sum them to obtain the dividend.
Sum the excess and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
The excess and deficit are used to adjust the result proportionally to find the quantities of the items being bought.
Place the rates of output, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the value of the goods, and the divisor represents the number of people.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

# Known values
善田價 = 300  # 善田每畝價
惡田價 = Fraction(500, 7)  # 惡田每畝價

# 假令善田二十畝，惡田八十畝，多一千七百一十四錢七分錢之二
善田_假1 = 20
惡田_假1 = 80
多1 = 1714 + Fraction(2, 7)

# 假令善田一十畝，惡田九十畝，不足五百七十一錢七分錢之三
善田_假2 = 10
惡田_假2 = 90
不足2 = 571 + Fraction(3, 7)

# 盈不足術
# 置所出率盈不足各居其下
所出率1 = 善田_假1 * 善田價 + 惡田_假1 * 惡田價
所出率2 = 善田_假2 * 善田價 + 惡田_假2 * 惡田價

# 盈不足相與同
盈 = 多1
不足 = 不足2

# 令維乘所出率并以為實
實 = 盈 * 所出率2 + 不足 * 所出率1

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
善田 = Fraction(實, 法)

# 善田數量
a = 善田

# 惡田數量
b = 100 - a  # Total land is 1 qing = 100 mu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 10000
Variable 'b' has wrong value. Expected: 175/2, Actual: -9900"""
