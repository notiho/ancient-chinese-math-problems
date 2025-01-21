"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
To solve this problem, we will calculate the amount of grain lost in one year and nine years. The total grain is given as 369,980斛7斗, and the yearly loss is 3升 per 斛. We will compute the losses accordingly.

1斛 = 10斗, and 1斗 = 10升. So, we need to convert the total grain into 升 for accurate calculations.

Here is the Python code:


"""


from fractions import Fraction

# Total grain in 升
total_grain = 369980 * 10 * 10 + 7 * 10  # Convert 369,980斛7斗 to 升

# Yearly loss in 升 per 斛
yearly_loss_per_斛 = 3

# Total yearly loss
a = Fraction(total_grain, 10 * 10) * yearly_loss_per_斛  # Loss in 1 year

# Total loss in 9 years
b = a * 9  # Loss in 9 years

# Convert back to 斛 and 斗 for the answer
a_斛 = a // (10 * 10)
a_斗 = (a % (10 * 10)) // 10
a_升 = a % 10

b_斛 = b // (10 * 10)
b_斗 = (b % (10 * 10)) // 10
b_升 = b % 10

# Results
a = f"{a_斛}斛 {a_斗}斗 {a_升}升"
b = f"{b_斛}斛 {b_斗}斗 {b_升}升"


"""


The variables `a` and `b` will contain the yearly and nine-year losses in the format of 斛, 斗, and 升.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 11099斛 4斗 21/10升
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 99894斛 7斗 89/10升
Missing variable in output: 'c'
Missing variable in output: 'd'"""
