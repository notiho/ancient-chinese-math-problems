"""
今有人舉取他絹重作劵要過限一日息絹一尺二日息二尺如是息絹日多一尺今過限一百日問息絹幾何
術曰併一百一日息以乘百日而半之即得
答曰 a疋
"""

#----- content starts here -----
"""
Suppose someone borrows silk from another person and agrees to a contract where interest is accrued if the repayment exceeds the agreed time limit.
For every day past the limit, the interest increases by 1 chi of silk per day:
- 1 day past the limit: 1 chi of interest,
- 2 days past the limit: 2 chi of interest,
- and so on, increasing by 1 chi per day.

Now, if the repayment is 100 days past the limit, how much interest in silk is accrued?

The procedure says: Combine (add) 100 and 1, obtaining the total number of interest days. Multiply this by 100 days, then divide by 2 to obtain the total interest.

The answer says: *a* bolts of silk.
"""

# 過限一百日
過限日數 = 100

# 併一百一日息
總日息 = 過限日數 + 1

# 以乘百日
總息 = 總日息 * 過限日數

# 而半之
總息 = Fraction(總息, 2)

# 1 疋 = 240 尺 (convert chi to bolts of silk)
a = Fraction(總息, 240)  # Convert to bolts of silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 505/4, Actual: 505/24"""
