"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a rectangular field given its width (廣) and length (從). The area is then converted into a combination of 畝 (a traditional Chinese unit of area) and remaining 步. 

The conversion rule is that 1 畝 = 240 步.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given dimensions of the field
width = 80  # in 步
length = 190  # in 步

# Calculate the total area in 步
total_area = width * length  # in 步

# Convert the area into 畝 and 步
a = total_area // 240  # Number of 畝
b = total_area % 240  # Remaining 步

# Results
a, b


"""


The variables `a` and `b` will contain the solution in 畝 and 步, respectively.
"""


"""
"""
