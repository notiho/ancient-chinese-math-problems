"""
今有人舉取他絹重作劵要過限一日息絹一尺二日息二尺如是息絹日多一尺今過限一百日問息絹幾何
術曰併一百一日息以乘百日而半之即得
答曰 a疋
"""

"""
Suppose someone borrows silk from another and creates a contract. If the repayment exceeds the deadline, the interest is 1 chi of silk for the first day, 2 chi for the second day, and so on, increasing by 1 chi per day.
Now, if the repayment exceeds the deadline by 100 days, how much silk is owed as interest?

The procedure says: Combine the 101 days of interest and multiply it by 100 days, then take half of it to obtain the result.

Answer: *a* pi (silk bolts).
"""

# 過限一百日
過限日 = 100

# 併一百一日息
日息總 = 過限日 + 1

# 以乘百日
總息 = 日息總 * 過限日

# 而半之
a = Fraction(總息, 2)
"""
Variable 'a' has wrong value. Expected: 505/4, Actual: 5050"""
