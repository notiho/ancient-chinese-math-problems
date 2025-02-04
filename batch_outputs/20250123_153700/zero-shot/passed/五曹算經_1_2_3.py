"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a rectangular field given its width (廣) and length (從). The area is then converted into a combination of 畝 (a traditional Chinese unit of area) and remaining 步. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions of the field
width = 80  # in 步
length = 190  # in 步

# Calculate the total area in 步^2
total_area = width * length  # in 步^2

# Conversion factor: 1 畝 = 240 步^2
mu_conversion = 240  # 步^2 per 畝

# Calculate the number of 畝 (a) and remaining 步 (b)
a = total_area // mu_conversion  # whole 畝
b = total_area % mu_conversion  # remaining 步

# The results are stored in variables a and b


"""


### Explanation:
1. The area of the rectangular field is calculated as `width * length`.
2. The total area in 步^2 is then divided by 240 (the conversion factor for 1 畝) to determine how many whole 畝 (a) there are.
3. The remainder from the division gives the remaining 步 (b).

### Final Answer:
The variables `a` and `b` will contain the number of 畝 and 步, respectively.
"""


"""
"""
