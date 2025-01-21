"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of families (`a`) in the city based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given values
excess = 4  # 鹿不盡四 (excess of 4 when 72 families share)
deficit = 20  # 鹿不足二十 (deficit of 20 when 90 families share)
families1 = 72  # 假令七十二家
families2 = 90  # 令之九十家

# Calculate the number of families (a)
numerator = families1 * deficit + families2 * excess  # 維乘之所得并為實
denominator = excess + deficit  # 並盈不足為法
a = Fraction(numerator, denominator)  # 除之，即得

# Result
a  # 城中家幾何


"""


### Explanation:
1. The problem uses the "盈不足術" (Excess and Deficit Method) to solve for the unknown number of families (`a`).
2. The formula is derived as:
   \[
   a = \frac{(72 \times 20) + (90 \times 4)}{4 + 20}
   \]
3. The numerator is the sum of the products of families and their respective excess/deficit.
4. The denominator is the sum of the excess and deficit.

When you run the code, the result will be the number of families (`a`) in the city.
"""


"""
"""
