"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
To solve this problem, we will calculate the amount of grain lost in one year and nine years. The given data is:

- Total grain: 369980斛7斗
- Annual loss rate: 3升 per 斛

We will compute the loss for one year and nine years. Note that 1斛 = 10斗 and 1斗 = 10升.

Here is the Python code:


"""


from fractions import Fraction

# Total grain in 斛, 斗, and 升
total_grain_hu = 369980  # 斛
total_grain_dou = 7  # 斗
total_grain_sheng = total_grain_hu * 10 * 10 + total_grain_dou * 10  # Convert to 升

# Annual loss rate
annual_loss_rate = 3  # 升 per 斛

# Loss in one year
a = Fraction(total_grain_hu * annual_loss_rate)  # Total loss in 升 for one year

# Loss in nine years
b = Fraction(a * 9)  # Total loss in 升 for nine years

# Convert results back to 斛 and 斗
a_hu = a // 100  # Convert 升 to 斛
a_dou = (a % 100) // 10  # Convert remaining 升 to 斗
a_sheng = a % 10  # Remaining 升

b_hu = b // 100  # Convert 升 to 斛
b_dou = (b % 100) // 10  # Convert remaining 升 to 斗
b_sheng = b % 10  # Remaining 升

# Final answers
a = f"{a_hu}斛 {a_dou}斗 {a_sheng}升"
b = f"{b_hu}斛 {b_dou}斗 {b_sheng}升"

# Results
print("一年耗:", a)
print("九年耗:", b)


"""


This code calculates the grain loss for one year (`a`) and nine years (`b`) and expresses the results in terms of 斛, 斗, and 升.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 11099斛 4斗 0升
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 99894斛 6斗 0升
Missing variable in output: 'c'
Missing variable in output: 'd'"""
