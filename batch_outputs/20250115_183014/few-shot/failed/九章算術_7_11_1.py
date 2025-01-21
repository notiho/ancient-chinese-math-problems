"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
The large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet? How much has each mouse dug?

The procedure says: Suppose for 2 days, they do not reach 5 cun. Suppose for 3 days, they exceed by 3 chi and 7.5 cun.
The method of excess and deficiency says: Place the rates of progress, and place the excess and deficiency below them respectively.
Multiply the rates of progress by the respective excess and deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a fraction, simplify it.
For the excess and deficiency, if they share the same unit, place the rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the "price of the object," and the divisor becomes the "number of people."

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
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
假二日 = 2
大鼠二日穿 = 大鼠初速 * (大鼠速率 ** (假二日 - 1))
小鼠二日穿 = 小鼠初速 * (小鼠速率 ** (假二日 - 1))
二日總穿 = 大鼠二日穿 + 小鼠二日穿
二日不足 = 垣厚 - 二日總穿

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi
假三日 = 3
大鼠三日穿 = 大鼠初速 * (大鼠速率 ** (假三日 - 1))
小鼠三日穿 = 小鼠初速 * (小鼠速率 ** (假三日 - 1))
三日總穿 = 大鼠三日穿 + 小鼠三日穿
三日有餘 = 三日總穿 - 垣厚

# 盈不足術
# 置所出率，盈、不足各居其下
大鼠速率_盈 = 大鼠速率 ** (假三日 - 1)
小鼠速率_盈 = 小鼠速率 ** (假三日 - 1)
大鼠速率_不足 = 大鼠速率 ** (假二日 - 1)
小鼠速率_不足 = 小鼠速率 ** (假二日 - 1)

# 令維乘所出率，并以為實
實 = (大鼠速率_盈 + 小鼠速率_盈) * 有餘 + (大鼠速率_不足 + 小鼠速率_不足) * 不足

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b尺，小鼠穿 c尺
大鼠穿 = 大鼠初速 * (大鼠速率 ** (a - 1))
小鼠穿 = 小鼠初速 * (小鼠速率 ** (a - 1))

b = 大鼠穿
c = 小鼠穿
"""
Code error: both arguments should be Rational instances"""
