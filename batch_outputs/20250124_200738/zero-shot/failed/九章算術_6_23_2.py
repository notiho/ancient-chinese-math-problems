"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of the field ("田幾何") in terms of "a" (a unit of area, where 1 頃 = 100 畝). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
year1_acres = 3  # 畝
year1_money = 1  # 錢
year2_acres = 4  # 畝
year2_money = 1  # 錢
year3_acres = 5  # 畝
year3_money = 1  # 錢
total_money = 100  # 錢

# Step 1: Calculate the 法 (denominator)
denominator = (year1_acres * year2_money * year3_money +
               year2_acres * year1_money * year3_money +
               year3_acres * year1_money * year2_money)

# Step 2: Calculate the 實 (numerator)
numerator = (year1_acres * year2_acres * year3_acres) * total_money

# Step 3: Calculate the area in 畝
area_in_acres = Fraction(numerator, denominator)

# Step 4: Convert 畝 to 頃 (1 頃 = 100 畝)
a = area_in_acres / 100

# Result
a  # The area in 頃
#----- content ends here -----


"""


### Explanation:
1. **法 (denominator)**: This is calculated by multiplying the 畝數 (acres) and 錢數 (money) for each year in a specific pattern, as described in the problem.
2. **實 (numerator)**: This is calculated by multiplying the 畝數 (acres) for all three years and then multiplying by the total money (100 錢).
3. **Area in 畝**: The area is obtained by dividing the numerator by the denominator.
4. **Conversion to 頃**: Since 1 頃 = 100 畝, we divide the result by 100 to get the area in 頃.

The variable `a` will contain the final answer in 頃.
"""


"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5"""
