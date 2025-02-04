"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular pit and convert it into a unit of measurement called "斛" (hú) and "寸" (cùn). Here's how we can compute it step by step:

1. The dimensions of the pit are:
   - Length: 1丈3尺 = 13尺 (since 1丈 = 10尺),
   - Width: 6尺,
   - Depth: 1丈 = 10尺.

2. The volume in cubic 尺 is calculated as:
   \[
   \text{Volume} = \text{Length} \times \text{Width} \times \text{Depth}
   \]

3. To convert the volume into 斛 and 寸:
   - 1斛 = 10立方尺 (10 cubic 尺),
   - The remainder (in cubic 尺) is converted into 寸.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the pit
length = 10 + 3  # 1丈3尺 = 13尺
width = 6        # 6尺
depth = 10       # 1丈 = 10尺

# Calculate the volume in cubic 尺
volume = length * width * depth  # in cubic 尺

# Convert the volume into 斛 and 寸
a = volume // 10  # Number of 斛 (1斛 = 10 cubic 尺)
b = volume % 10   # Remaining cubic 尺 as 寸

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Output
- `a` represents the number of 斛.
- `b` represents the remaining cubic 尺 (converted into 寸).

By running this code, you will get the values of `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""
