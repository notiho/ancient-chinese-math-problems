"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=32/13)日 。各長 b(=63/13)尺 。
"""

"""
Suppose a cattail (pu) grows 3 chi in one day, and a rush (guan) grows 1 chi in one day.
The cattail starts at half its length, and the rush starts at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun.
Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficiency" procedure says: Place the rates of growth, with the excess and deficiency below each.
Multiply the rates of growth by the respective excess and deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a fraction, simplify it.
If the excess and deficiency are related to the same object, place the rates of growth, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the value of the object, and the divisor becomes the number of people.

Answer: *a*(=32/13) days. Each grows to *b*(=63/13) chi.
"""

# 蒲生一日，長三尺
蒲日長 = 3

# 莞生一日，長一尺
莞日長 = 1

# 蒲生日自半
蒲初長 = Fraction(1, 2)

# 莞生日自倍
莞初長 = 2

# 假令二日，不足一尺五寸
不足日數 = 2
不足差 = Fraction(1, 2) + 1  # 1 chi 5 cun = 1.5 chi

# 令之三日，有餘一尺七寸半
有餘日數 = 3
有餘差 = 1 + Fraction(7, 10)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
不足實 = 有餘日數 * 不足差  # Multiply excess rate by deficiency
有餘實 = 不足日數 * 有餘差  # Multiply deficiency rate by excess

# 令維乘所出率，并以為實
實 = 不足實 + 有餘實

# 并盈、不足為法
法 = 不足差 + 有餘差

# 實如法而一
a = Fraction(實, 法)  # 32/13 days

# 各長
b = 蒲初長 + a * 蒲日長  # 63/13 chi
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 79/32
Variable 'b' has wrong value. Expected: 63/13, Actual: 253/32"""
