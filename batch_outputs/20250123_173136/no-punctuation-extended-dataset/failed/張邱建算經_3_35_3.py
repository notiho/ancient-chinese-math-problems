"""
今有人舉取他絹重作劵要過限一日息絹一尺二日息二尺如是息絹日多一尺今過限一百日問息絹幾何
術曰併一百一日息以乘百日而半之即得
答曰 a疋
"""

"""
Suppose someone borrows silk from another person and writes a contract. 
The agreement states that for each day past the due date, the interest increases by 1 chi of silk per day:
1 day late = 1 chi, 2 days late = 2 chi, and so on, increasing by 1 chi per day.
Now, if the payment is 100 days overdue, how much silk is owed as interest?

The procedure says: Combine 101 days of interest (1 more than 100) and multiply it by 100 days, then halve the result to obtain the total interest.

Answer: *a* pi (bolts of silk).
"""

# 過限一百日
過限日 = 100

# 併一百一日息
總日息 = 過限日 + 1

# 以乘百日
總息 = 總日息 * 過限日

# 而半之
a = Fraction(總息, 2)
"""
Variable 'a' has wrong value. Expected: 505/4, Actual: 5050"""
