"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
To solve this problem, we will compute the amount of grain lost in one year (`a`) and in nine years (`b`). The total amount of grain is given as 369,980斛7斗, and the annual loss is 3升 per 斛. 

Since 1斛 = 10斗 and 1斗 = 10升, we will first convert the total grain into 升 for easier computation.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total grain in 升
total_grain = 369980 * 10 * 10 + 7 * 10  # Convert 369,980斛7斗 to 升

# Annual loss in 升 per 斛
annual_loss_per_斛 = 3

# Total annual loss in 升
annual_loss = total_grain // (10 * 10) * annual_loss_per_斛  # Convert total grain to 斛 and multiply by 3升

# Total loss in nine years in 升
nine_year_loss = annual_loss * 9

# Convert losses back to 斛
a = Fraction(annual_loss, 10 * 10)  # Convert annual loss from 升 to 斛
b = Fraction(nine_year_loss, 10 * 10)  # Convert nine-year loss from 升 to 斛

# Results
a, b
#----- content ends here -----


"""


This code will compute the values of `a` (annual loss in 斛) and `b` (nine-year loss in 斛).
"""


"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 55497/5
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 499473/5"""
