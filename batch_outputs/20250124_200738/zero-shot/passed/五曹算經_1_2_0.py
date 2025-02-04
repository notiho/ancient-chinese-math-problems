"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a rectangular field given its width (廣) and length (從). The area is then converted into units of 畝 (a traditional Chinese unit of area) and remaining 步. 

The problem states:
- Width (廣) = 80 步
- Length (從) = 190 步
- 1 畝 = 240 步²

The area in 畝 and 步 can be calculated as follows:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
width = 80  # 步
length = 190  # 步

# Area in 步²
total_area = width * length  # 步²

# Conversion to 畝 and 步
mu = total_area // 240  # Whole 畝
remaining_bu = total_area % 240  # Remaining 步

# Assign to variables
a = mu
b = remaining_bu

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. Multiply the width and length to get the total area in 步².
2. Divide the total area by 240 to get the number of whole 畝 (a).
3. Use the remainder of the division to find the remaining 步 (b).

### Final Answer:
The variables `a` and `b` will contain the values for 畝 and 步, respectively.
"""


"""
"""
