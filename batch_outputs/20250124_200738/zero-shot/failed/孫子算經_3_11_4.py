"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
To solve this problem, we will compute the amount of grain lost in one year (`a`) and in nine years (`b`). The total initial amount of grain is given as 369,980斛7斗, and the annual loss rate is 3升. Note that 1斛 = 10斗 and 1斗 = 10升.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Initial amount of grain in 斛
initial_grain = Fraction(369980) + Fraction(7, 10)  # 369980斛7斗 = 369980 + 7/10斛

# Annual loss rate in 斛
annual_loss_rate = Fraction(3, 100)  # 3升 = 3/100斛

# Loss in one year
a = annual_loss_rate

# Loss in nine years
b = annual_loss_rate * 9

# Results
a, b
#----- content ends here -----


"""


This code calculates the loss in one year (`a`) and in nine years (`b`) in units of 斛.
"""


"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 3/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 27/100"""
