"""
今有女子不善織日減功遲初日織五尺末日織一尺今三十日織訖問織㡬何
術曰併初末日織尺數半之餘以乗織訖日數即得
答曰 a疋
"""

#----- content starts here -----
"""
Suppose there is a woman who is not skilled at weaving. Each day, her weaving output decreases.
On the first day, she weaves 5 chi, and on the last day, she weaves 1 chi.
In 30 days, she finishes weaving.
Question: how much cloth does she weave in total?

The procedure says: Add the number of chi woven on the first and last days, halve the sum, and multiply it by the number of days of weaving. This gives the total.

Answer: *a* bolts of cloth.
"""

# 初日織五尺
初日織 = 5

# 末日織一尺
末日織 = 1

# 織訖日數三十日
織訖日數 = 30

# 併初末日織尺數
初末和 = 初日織 + 末日織

# 半之
平均每日織 = Fraction(初末和, 2)

# 餘以乘織訖日數即得
總織 = 平均每日織 * 織訖日數

# 1 疋 = 50 尺
疋 = Fraction(總織, 50)

a = 疋#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/4, Actual: 9/5"""
