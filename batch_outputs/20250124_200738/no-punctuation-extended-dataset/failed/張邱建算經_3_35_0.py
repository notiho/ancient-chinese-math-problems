"""
今有人舉取他絹重作劵要過限一日息絹一尺二日息二尺如是息絹日多一尺今過限一百日問息絹幾何
術曰併一百一日息以乘百日而半之即得
答曰 a疋
"""

#----- content starts here -----
"""
Suppose someone borrows silk from another person and makes a contract. If the repayment exceeds the due date, for every day past the limit, the interest is 1 chi of silk for the first day, 2 chi for the second day, and so on, increasing by 1 chi per day.
Now, if the repayment is 100 days past the limit, how much interest silk is owed?

The procedure says: Add 101 (the total number of days including the first day) to the interest rate for 100 days. Multiply this by 100 days, then divide it by 2 to obtain the result.

Answer: *a* pi (bolts of silk).
"""

# 過限一百日
過限日數 = 100

# 併一百一日息
總日息 = 過限日數 + 1

# 以乘百日
總息 = 總日息 * 過限日數

# 而半之
a = Fraction(總息, 2)  # 結果以疋為單位#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 505/4, Actual: 5050"""
