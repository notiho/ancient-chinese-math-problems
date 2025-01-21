"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。各長 b尺 。
"""

"""
Suppose a cattail grows 3 chi in one day, and a rush grows 1 chi in one day.
The cattail starts at half its length, and the rush starts at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose for 2 days, the difference is less than 1 chi and 5 cun.
Suppose for 3 days, the difference exceeds 1 chi and 7.5 cun.

The "Excess and Deficiency" procedure says: Place the rates of growth, with the excess and deficiency below each.
Multiply the rates by their respective excess or deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a remainder, simplify it.
For cases where the excess and deficiency are related to the same item, place the rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend is the price of the item, and the divisor is the number of people.

Answer: *a* days. Each grows to *b* chi.
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
日數1 = 2
不足 = Fraction(1, 2) + 1  # 1 chi 5 cun = 1.5 chi

# 令之三日，有餘一尺七寸半
日數2 = 3
有餘 = Fraction(7, 2) + 1  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = (蒲日長 - 莞日長) * 日數1
率2 = (蒲日長 - 莞日長) * 日數2

# 令維乘所出率，并以為實
實 = (率1 * 有餘) + (率2 * 不足)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 各長 b尺
b = 蒲初長 + a * 蒲日長  # Both will have the same length when equal

a日 = a
b尺 = b
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 9/2
Variable 'b' has wrong value. Expected: 63/13, Actual: 14"""
