"""
今有程傳委輸，空車日行七十里，重車日行五十里。今載太倉粟輸上林，五日三返。問︰太倉去上林幾何？
術曰：并空、重里數，以三返乘之，為法。令空、重相乘，又以五日乘之，為實。實如法得一里。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
empty_distance_per_day = 70  # 空車日行七十里
loaded_distance_per_day = 50  # 重車日行五十里
round_trips = 3  # 三返
days = 5  # 五日

# Calculation
total_distance_per_round_trip = empty_distance_per_day + loaded_distance_per_day  # 并空、重里數
total_distance_all_trips = total_distance_per_round_trip * round_trips  # 以三返乘之，為法
product_of_distances = empty_distance_per_day * loaded_distance_per_day  # 空、重相乘
total_product = product_of_distances * days  # 又以五日乘之，為實
a = Fraction(total_product, total_distance_all_trips)  # 實如法得一里

# Result
a  # 太倉去上林幾何
#----- content ends here -----


"""


The variable `a` represents the distance from 太倉 (Taicang) to 上林 (Shanglin) in "里".
"""


"""
"""
