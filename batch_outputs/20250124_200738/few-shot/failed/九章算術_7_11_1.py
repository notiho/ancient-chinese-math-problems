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
The large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose it takes 2 days, but this is less than 5 cun. Suppose it takes 3 days, but this exceeds 3 chi 7 cun and a half.
The procedure for excess and deficiency says: Place the rates of progress, with the excess and deficiency below each. Multiply the rates of progress by the excess and deficiency, and sum them to form the dividend. Sum the excess and deficiency to form the divisor. Divide the dividend by the divisor to find the result. If there is a fraction, simplify it. For the excess and deficiency, if they share the same "purchasing object," place the rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend. The dividend is the "price of the object," and the divisor is the "number of people."

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
# 假令二日，不足五寸
假日1 = 2
大鼠穿1 = 大鼠初速 * (2 ** (假日1 - 1))
小鼠穿1 = 小鼠初速 * (1 / (2 ** (假日1 - 1)))
總穿1 = 大鼠穿1 + 小鼠穿1
不足 = 垣厚 - 總穿1

# 令之三日，有餘三尺七寸半
假日2 = 3
大鼠穿2 = 大鼠初速 * (2 ** (假日2 - 1))
小鼠穿2 = 小鼠初速 * (1 / (2 ** (假日2 - 1)))
總穿2 = 大鼠穿2 + 小鼠穿2
有餘 = 總穿2 - 垣厚

# 盈不足術
# 置所出率，盈、不足各居其下
所出率1 = 總穿1
所出率2 = 總穿2

# 令維乘所出率，并以為實
實 = (所出率1 * 有餘) + (所出率2 * 不足)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b尺，小鼠穿 c尺
b = 大鼠初速 * (2 ** (a - 1))
c = 小鼠初速 * (1 / (2 ** (a - 1)))#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
