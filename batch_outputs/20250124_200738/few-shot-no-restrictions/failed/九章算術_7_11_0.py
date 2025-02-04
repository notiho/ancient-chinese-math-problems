"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice dig through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet? How much has each mouse dug?

The procedure says: Suppose for 2 days, the progress is insufficient by 5 cun. Suppose for 3 days, the progress exceeds by 3 chi and 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, with the excess and deficiency below them, respectively.
Multiply the rates of progress by the excess and deficiency, summing them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
For the excess and deficiency, if they correspond to the same "purchasing object," place the rates of progress, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the "price of the object," and the divisor becomes the "number of people."

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# Wall thickness
垣厚 = 5  # chi

# Large mouse daily progress
大鼠日初進 = 1  # chi
# Small mouse daily progress
小鼠日初進 = 1  # chi

# Hypothesis for 2 days
假令二日不足 = Fraction(5, 10)  # 5 cun = 0.5 chi

# Hypothesis for 3 days
假令三日有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi

# Rates of progress (difference in daily progress for 2 and 3 days)
大鼠二日進 = 大鼠日初進 * (2**2 - 1)  # Large mouse doubles daily
小鼠二日進 = 小鼠日初進 * (1 - Fraction(1, 2)**2)

大鼠三日進 = 大鼠日初進 * (2**3 - 1)
小鼠三日進 = 小鼠日初進 * (1 - Fraction(1, 2)**3)

# Total progress for 2 days and 3 days
二日進 = 大鼠二日進 + 小鼠二日進
三日進 = 大鼠三日進 + 小鼠三日進

# Excess and deficiency method
盈不足實 = (二日進 * 假令三日有餘) + (三日進 * 假令二日不足)
盈不足法 = 假令三日有餘 + 假令二日不足

# Days until meeting
a = 盈不足實 / 盈不足法

# Total progress of each mouse
大鼠穿 = 大鼠日初進 * (2**a - 1)
小鼠穿 = 小鼠日初進 * (1 - Fraction(1, 2)**a)

b = 大鼠穿
c = 小鼠穿

# Final results
a日 = a
b尺 = b
c尺 = c#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
