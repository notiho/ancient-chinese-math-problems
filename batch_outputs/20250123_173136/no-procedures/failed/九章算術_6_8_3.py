"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
荅曰： a里 。
"""

"""
Suppose there is a transportation task. An empty cart travels 70 li per day, while a loaded cart travels 50 li per day.
Now, grain is being transported from Taicang to Shanglin, and in 5 days, the cart completes 3 round trips (to and back).
Question: What is the distance between Taicang and Shanglin?

Answer: *a* li.
"""

# 空車日行七十里
空車日行 = 70

# 重車日行五十里
重車日行 = 50

# 5日3返，總行程為3個來回（即6次單程）
總單程次數 = 6

# 總行程 = 空車行程 + 重車行程
# 空車行程次數 = 3次（每次來回有1次空車）
# 重車行程次數 = 3次（每次來回有1次重車）
總行程 = (空車日行 * 3) + (重車日行 * 3)

# 總行程用時5天
每日行程 = 總行程 / 5

# 單程距離 = 每日行程 / 單程次數
a = Fraction(每日行程, 總單程次數)

a
"""
Code error: both arguments should be Rational instances"""
