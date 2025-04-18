"""
今有女子不善織日減功遲初日織五尺末日織一尺今三十日織訖問織㡬何
術曰併初末日織尺數半之餘以乗織訖日數即得
答曰 a疋
"""

#----- content starts here -----
"""
Suppose there is a woman who is not skilled at weaving. Each day, her work slows down.
On the first day, she weaves 5 chi, and on the last day, she weaves 1 chi.
In 30 days, she finishes weaving.
Question: how much does she weave in total?

The procedure says: Add together the number of chi woven on the first and last days, halve it, and multiply the result by the number of days weaving is completed. This gives the total.

Answer: *a* bolts of cloth (*a* pi).
"""

# 初日織五尺
初日織 = 5

# 末日織一尺
末日織 = 1

# 三十日織訖
織訖日數 = 30

# 併初末日織尺數
初末和 = 初日織 + 末日織

# 半之
平均每日織 = Fraction(初末和, 2)

# 餘以乘織訖日數即得
總織尺數 = 平均每日織 * 織訖日數

# 1 疋 = 50 尺
疋換算 = 50
a = Fraction(總織尺數, 疋換算)  # 織成的疋數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/4, Actual: 9/5"""
