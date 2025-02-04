"""
今有人舉取他絹重作劵要過限一日息絹一尺二日息二尺如是息絹日多一尺今過限一百日問息絹幾何
術曰併一百一日息以乘百日而半之即得
答曰 a疋
"""

#----- content starts here -----
"""
Suppose someone borrows silk from another and makes an agreement. If the repayment exceeds the deadline, for each day past the deadline, the interest increases by 1 chi of silk per day. 
For example, on the first day past the deadline, the interest is 1 chi; on the second day, the interest is 2 chi, and so on, increasing by 1 chi per day.
Now, if the repayment is 100 days past the deadline, how much silk is owed as interest?

The procedure says: Combine (add) 101 days of interest and multiply it by 100 days, then take half of the result to obtain the total interest.

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

# Convert chi to bolts of silk (assuming 1 bolt = 240 chi)
chi_per_bolt = 240
a = Fraction(總息, chi_per_bolt)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 505/4, Actual: 505/24"""
