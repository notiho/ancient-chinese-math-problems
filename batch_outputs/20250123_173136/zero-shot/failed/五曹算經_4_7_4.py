"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
To solve this problem, we need to calculate the volume of a storage space and convert it into a specific unit of measurement called "斛" (hú). The dimensions of the storage space are given in Chinese units: 長 (length) = 1丈9尺, 廣 (width) = 1丈5尺, and 高 (height) = 1丈3尺. The conversion factor for "斛" is also provided: 1斛 = 1尺6寸2分 (or 1.62尺 in decimal).

### Step 1: Convert the dimensions into a consistent unit (尺).
1丈 = 10尺, so:
- 長 = 1丈9尺 = 10尺 + 9尺 = 19尺
- 廣 = 1丈5尺 = 10尺 + 5尺 = 15尺
- 高 = 1丈3尺 = 10尺 + 3尺 = 13尺

### Step 2: Calculate the volume in cubic 尺.
Volume = 長 × 廣 × 高 = 19尺 × 15尺 × 13尺

### Step 3: Convert the volume into 斛.
To find the number of 斛, divide the total volume by 1.62尺 (斛法). The remainder will represent the fractional part in 分.

### Step 4: Write the solution in Python.


"""


from fractions import Fraction

# Dimensions in 尺
length = 19  # 1丈9尺
width = 15   # 1丈5尺
height = 13  # 1丈3尺

# Conversion factor: 1斛 = 1尺6寸2分 = 1.62尺
hu_conversion = Fraction(162, 100)  # 1.62 as a fraction

# Calculate the volume in cubic 尺
volume = length * width * height  # 19 * 15 * 13

# Calculate the number of 斛 and the remainder in 分
a = volume // hu_conversion  # Integer part (number of 斛)
remainder = volume % hu_conversion  # Remainder in 尺
b = remainder * 100 // hu_conversion  # Convert remainder to 分

# Results
a = int(a)  # Number of 斛
b = int(b)  # Number of 分


"""


### Final Answer:
The solution will compute the values of `a` (number of 斛) and `b` (number of 分).
"""


"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 3"""
