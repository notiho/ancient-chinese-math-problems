"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field (田) in terms of 畝 (mu) and 步 (bu). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
length = 30  # in 步
width = Fraction(24, 2)  # 半之得一十二步 (half of 24 步)

# Calculate the area in 步²
area_in_bu_squared = length * width

# Conversion factor: 1 畝 = 240 步²
mu_conversion = 240

# Calculate the area in 畝 and 步
a = area_in_bu_squared // mu_conversion  # 畝
b = area_in_bu_squared % mu_conversion  # 步

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. The length of the field is 30 步.
2. The width is given as "half of 24 步," which is 12 步.
3. The area in 步² is calculated as `length * width`.
4. To convert the area into 畝 and 步, we use the conversion factor `1 畝 = 240 步²`.
5. The integer division (`//`) gives the number of 畝, and the remainder (`%`) gives the remaining 步.

### Output:
The variables `a` and `b` will contain the solution:
- `a` is the number of 畝.
- `b` is the number of 步.
"""


"""
"""
