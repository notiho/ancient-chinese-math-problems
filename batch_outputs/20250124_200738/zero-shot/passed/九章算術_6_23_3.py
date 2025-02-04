"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the size of the field (田) in "頃" (a unit of area) based on the given rates of rent over three years.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate_year1 = Fraction(3, 1)  # 3 畝 per 錢
rate_year2 = Fraction(4, 1)  # 4 畝 per 錢
rate_year3 = Fraction(5, 1)  # 5 畝 per 錢
total_money = 100  # Total 錢 over 3 years

# Step 1: Calculate the 法 (denominator)
法 = (rate_year1 * rate_year2) + (rate_year2 * rate_year3) + (rate_year3 * rate_year1)

# Step 2: Calculate the 實 (numerator)
實 = (rate_year1 * rate_year2 * rate_year3) * total_money

# Step 3: Calculate the size of the field (田) in 畝
田 = 實 / 法

# Convert 畝 to 頃 (1 頃 = 100 畝)
a = 田 / 100

# Result
a  # The size of the field in 頃
#----- content ends here -----


"""


### Explanation:
1. **Rates of rent**: The problem gives the rent rates for three years in terms of 畝 per 錢.
2. **法 (denominator)**: This is calculated as the sum of the products of 畝數 (rates) taken two at a time.
3. **實 (numerator)**: This is calculated as the product of all three rates multiplied by the total money (100 錢).
4. **田 (size of the field)**: The size of the field in 畝 is obtained by dividing 實 by 法.
5. **Conversion to 頃**: Since 1 頃 = 100 畝, we divide the result by 100 to get the size in 頃.

The variable `a` contains the final answer in 頃.
"""


"""
"""
