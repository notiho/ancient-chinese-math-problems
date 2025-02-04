"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet, and how far does each mouse dig?

The procedure says: Suppose for 2 days, the total is less than 5 cun. Suppose for 3 days, the total exceeds 3 chi and 7.5 cun.
The "Excess and Deficiency" procedure says: Place the rates of progress, and the excess and deficiency below them respectively.
Multiply the rates of progress by the respective excess and deficiency, and add them together to form the dividend.
Add the excess and deficiency together to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For the excess and deficiency to correspond to the same object, place the rates of progress, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠速率 = 2
小鼠速率 = Fraction(1, 2)

# 假令二日，不足五寸
假日1 = 2
不足 = 5 / 10  # 5 cun = 0.5 chi
大鼠穿1 = 大鼠初速 * (大鼠速率 ** (假日1 - 1))
小鼠穿1 = 小鼠初速 * (小鼠速率 ** (假日1 - 1))
總穿1 = 大鼠穿1 + 小鼠穿1

# 令之三日，有餘三尺七寸半
假日2 = 3
有餘 = 3 + 7.5 / 10  # 3 chi 7.5 cun = 3.75 chi
大鼠穿2 = 大鼠初速 * (大鼠速率 ** (假日2 - 1))
小鼠穿2 = 小鼠初速 * (小鼠速率 ** (假日2 - 1))
總穿2 = 大鼠穿2 + 小鼠穿2

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 總穿2 - 垣厚
不足 = 垣厚 - 總穿1

# 令維乘所出率，并以為實
實 = (假日1 * 盈) + (假日2 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 計算各鼠穿距
大鼠穿 = sum([大鼠初速 * (大鼠速率 ** (i - 1)) for i in range(1, int(a) + 1)])
小鼠穿 = sum([小鼠初速 * (小鼠速率 ** (i - 1)) for i in range(1, int(a) + 1)])

b = 大鼠穿
c = 小鼠穿#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 24/7
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 7/4"""
