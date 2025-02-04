"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
To solve this problem, we will calculate the amount of grain lost in one year (`a`) and in nine years (`b`). The total amount of grain is given as 369,980斛7斗, and the annual loss is 3升 per 斛. Note that 1斛 = 10斗, and 1斗 = 10升. 

Here is the Python code:


"""


from fractions import Fraction

# Total grain in 斛
total_grain = Fraction(369980) + Fraction(7, 10)  # 7斗 = 7/10斛

# Annual loss per 斛 in 升
annual_loss_per_斛 = Fraction(3, 10)  # 3升 = 3/10斗

# Loss in one year (a斛)
a = total_grain * annual_loss_per_斛

# Loss in nine years (b斛)
b = a * 9

# Results
a, b


"""


This code calculates the values of `a` and `b` in terms of 斛. The results will be stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
