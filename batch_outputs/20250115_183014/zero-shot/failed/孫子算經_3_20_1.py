"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
術曰：置長一千步，以廣五百步乘之，得五十萬；以三十六乘之，得一千八百萬尺，即得鶉數；上十之，即得鷃數。
答曰：鶉 a ，鷃 b 。
"""

"""
Here is the Python code to compute the values of the unknowns `a` (鶉) and `b` (鷃):


"""


from fractions import Fraction

# Given data
length = 1000  # in steps
width = 500  # in steps
conversion_to_chi = 36  # 1 step = 36 chi
conversion_to_cun = 10  # 1 chi = 10 cun

# Calculations
area_in_steps = length * width  # area in steps^2
a = area_in_steps * conversion_to_chi  # convert to chi (鶉數)
b = a * conversion_to_cun  # convert to cun (鷃數)

# Results
a  # 鶉數
b  # 鷃數


"""


Explanation:
1. The area of the land is calculated as `length * width` in steps².
2. To find the number of chi (鶉數), the area in steps² is multiplied by the conversion factor `36`.
3. To find the number of cun (鷃數), the chi value is multiplied by the conversion factor `10`.

The results are stored in variables `a` (鶉數) and `b` (鷃數).
"""


"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 180000000"""
