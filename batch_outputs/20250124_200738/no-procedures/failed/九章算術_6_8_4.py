"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a transportation task. An empty cart travels 70 li per day, and a loaded cart travels 50 li per day.
Now, grain is transported from Taicang to Shanglin, and it takes 5 days for 3 round trips (3 returns).
Question: how far is Taicang from Shanglin?

Answer: *a* li.
"""

# 空車日行 70 里
空車日行 = 70

# 重車日行 50 里
重車日行 = 50

# 5 日 3 返
日數 = 5
往返次數 = 3

# Total distance traveled in one round trip (Taicang to Shanglin and back)
單次往返距離 = 空車日行 + 重車日行

# Total distance traveled in 3 round trips
總距離 = 單次往返距離 * 往返次數

# Total distance traveled in 5 days
每日距離 = 總距離 / 日數

# Distance from Taicang to Shanglin (half of one round trip)
a = 單次往返距離 / 2#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 875/18, Actual: 60.0"""
