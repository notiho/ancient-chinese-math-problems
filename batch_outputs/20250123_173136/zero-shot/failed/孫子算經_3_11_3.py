"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
To solve this problem, let's translate it into Python code. We'll compute the values for `a` (一年耗) and `b` (九年耗) using the given information.

### Problem Breakdown:
1. Total amount of 粟 (grain) = 369,980 斛 7 斗.
2. Each year, the grain loses 3 升 per 斛.
3. We need to calculate the total loss for one year (`a`) and for nine years (`b`).

### Conversion:
1 斛 = 10 斗, and 1 斗 = 10 升.  
Thus, 1 斛 = 100 升.

### Python Code:

"""


from fractions import Fraction

# Total grain in 斛 and 斗
total_grain_hu = 369980  # 斛
total_grain_dou = 7      # 斗

# Convert total grain to 升
total_grain_sheng = total_grain_hu * 100 + total_grain_dou * 10  # 1 斛 = 100 升, 1 斗 = 10 升

# Annual loss per 斛 in 升
annual_loss_per_hu = 3  # 升

# Total annual loss in 升
a_sheng = total_grain_hu * annual_loss_per_hu  # Total annual loss in 升

# Convert annual loss to 斛
a = Fraction(a_sheng, 100)  # Convert 升 to 斛 (1 斛 = 100 升)

# Total loss over 9 years in 升
b_sheng = a_sheng * 9  # Total 9-year loss in 升

# Convert 9-year loss to 斛
b = Fraction(b_sheng, 100)  # Convert 升 to 斛 (1 斛 = 100 升)

# Results
a, b


"""


### Explanation:
1. Convert the total grain into 升 for easier calculations.
2. Compute the annual loss in 升 by multiplying the total grain in 斛 by the annual loss per 斛.
3. Convert the annual loss from 升 to 斛.
4. Multiply the annual loss by 9 to get the 9-year loss in 升.
5. Convert the 9-year loss from 升 to 斛.

### Output:
The variables `a` and `b` will store the results:
- `a` = 一年耗 (in 斛)
- `b` = 九年耗 (in 斛)
"""


"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 55497/5
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 499473/5"""
