"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
To solve this problem, we will calculate the amount of grain lost in one year (`a`) and in nine years (`b`). The total amount of grain is given as 369,980斛7斗, and the annual loss rate is 3升 per 斛. Note that 1斛 = 10斗, and 1斗 = 10升.

Here is the Python code:


"""


from fractions import Fraction

# Total grain in 斛 and 斗
total_grain_hu = 369980  # 斛
total_grain_dou = 7      # 斗

# Convert total grain to 升
total_grain_sheng = total_grain_hu * 10 * 10 + total_grain_dou * 10  # 1斛 = 10斗, 1斗 = 10升

# Annual loss rate in 升
annual_loss_rate_sheng = 3  # 升 per 斛

# Calculate total annual loss in 升
a_sheng = total_grain_hu * annual_loss_rate_sheng  # Total annual loss in 升

# Convert annual loss to 斛
a = Fraction(a_sheng, 10 * 10)  # Convert 升 to 斛 (1斛 = 10斗, 1斗 = 10升)

# Calculate nine-year loss in 斛
b = a * 9  # Nine years' loss in 斛

# Results
a, b


"""


### Explanation:
1. Convert the total grain into 升 for easier calculations.
2. Multiply the annual loss rate (3升 per 斛) by the total grain in 斛 to get the annual loss in 升.
3. Convert the annual loss from 升 to 斛 using the conversion factor (1斛 = 10斗 = 100升).
4. Multiply the annual loss by 9 to get the nine-year loss in 斛.

### Final Answer:
- `a` represents the annual loss in 斛.
- `b` represents the nine-year loss in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 55497/5
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 499473/5"""
