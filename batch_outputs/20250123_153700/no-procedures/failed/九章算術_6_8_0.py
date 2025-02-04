"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
荅曰： a里 。
"""

"""
Suppose there is a transportation task. An empty cart travels 70 li per day, while a loaded cart travels 50 li per day.
Now, grain is being transported from Taicang to Shanglin, and in 5 days, the cart makes 3 round trips.
Question: how far is Taicang from Shanglin?

Answer: *a* li.
"""

# 空車日行七十里
空車日行 = 70

# 重車日行五十里
重車日行 = 50

# 五日三返
總天數 = 5
總往返次數 = 3

# Calculate the total distance traveled in one round trip (both loaded and empty)
單程距離 = Fraction(重車日行 * 總天數 + 空車日行 * 總天數, 2 * 總往返次數)

# The distance from Taicang to Shanglin is half of one round trip
a = 單程距離
"""
Variable 'a' has wrong value. Expected: 875/18, Actual: 100"""
