"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
荅曰： a里 。
"""

"""
Suppose there is a transport task. An empty cart travels 70 li per day, while a loaded cart travels 50 li per day.
Now, grain is transported from Taicang to Shanglin, completing 3 round trips in 5 days.
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
# Distance for one round trip = distance going (重車) + distance returning (空車)
單次往返距離 = 重車日行 + 空車日行

# Total distance traveled in 3 round trips
總距離 = 單次往返距離 * 往返次數

# Total distance traveled in 5 days
每日距離 = 總距離 / 日數

# Distance from Taicang to Shanglin (half of one round trip)
a = 單次往返距離 / 2
"""
Variable 'a' has wrong value. Expected: 875/18, Actual: 60.0"""
