"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a里 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves calculating the distance between 太倉 (Taicang) and 上林 (Shanglin) based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given data
empty_car_daily_distance = 70  # 空車日行七十里
loaded_car_daily_distance = 50  # 重車日行五十里
round_trips = 3  # 三返
days = 5  # 五日

# Calculation
total_distance_per_round_trip = empty_car_daily_distance + loaded_car_daily_distance  # 并空、重里數
total_distance_all_trips = total_distance_per_round_trip * round_trips  # 以三返乘之，為法
product_of_distances_and_days = empty_car_daily_distance * loaded_car_daily_distance * days  # 空、重相乘，又以五日乘之，為實

# Solve for the distance (a) between 太倉 and 上林
a = Fraction(product_of_distances_and_days, total_distance_all_trips)  # 實如法得一里

# The result
a  # 太倉去上林的距離


"""


The variable `a` will contain the distance in "里" (Chinese miles) between 太倉 and 上林.
"""


"""
"""
