"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。各長 b尺 。
"""

"""

"""


from fractions import Fraction

# 蒲生一日，長三尺
蒲日長 = 3

# 莞生一日，長一尺
莞日長 = 1

# 蒲生日自半
蒲初長 = Fraction(1, 2)

# 莞生日自倍
莞初長 = 2

# 假令二日，不足一尺五寸
不足 = Fraction(3, 2)  # 一尺五寸 = 1.5 尺

# 令之三日，有餘一尺七寸半
有餘 = Fraction(17, 2)  # 一尺七寸半 = 1.75 尺

# 盈不足術曰：置所出率，盈、不足各居其下
盈率 = 3  # 三日
不足率 = 2  # 二日

# 令維乘所出率，并以為實
實 = (盈率 * 不足) + (不足率 * 有餘)

# 并盈、不足為法
法 = 盈率 + 不足率

# 實如法而一
a = Fraction(實, 法)

# 各長 b 尺
b = 蒲初長 + a * 蒲日長  # 蒲和莞長度相等，計算其中一個即可

# Output results
a日 = a
b尺 = b


"""

"""


"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 43/10
Variable 'b' has wrong value. Expected: 63/13, Actual: 67/5"""
