"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cone-shaped pile of grain, given its base circumference and height. The formula for the volume of a cone is:

\[
V = \frac{1}{3} \cdot \text{Base Area} \cdot \text{Height}
\]

Here, the base area is derived from the circumference, and the volume is converted into units of "斛" and "分" using the given conversion factor.


"""

#----- content starts here -----

from fractions import Fraction

# Given data
circumference = 48  # in 尺
height = 6  # in 尺
conversion_factor = Fraction(1, 1) / (1 + Fraction(6, 10) + Fraction(2, 100))  # 1斛 = 1尺6寸2分

# Step 1: Calculate the base area
# Base area = (circumference^2) / (4 * π), but π is approximated in ancient Chinese math as 3
base_area = Fraction(circumference**2, 12)  # Using π ≈ 3

# Step 2: Calculate the volume of the cone
volume = Fraction(1, 3) * base_area * height

# Step 3: Convert the volume into "斛" and "分"
volume_in_hu = volume * conversion_factor
a = volume_in_hu.numerator // volume_in_hu.denominator  # Integer part (斛)
b = volume_in_hu - a  # Fractional part (分)
b = b * 100  # Convert fractional part to 分

# Final results
a = int(a)  # Number of 斛
b = int(b)  # Number of 分
#----- content ends here -----


"""


The variables `a` and `b` will contain the final answer in terms of "斛" and "分".
"""


"""
Variable 'a' has wrong value. Expected: 316, Actual: 237
Variable 'b' has wrong value. Expected: 8, Actual: 3"""
