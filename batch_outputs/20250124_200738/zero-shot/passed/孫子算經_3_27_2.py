"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method described into Python code. The problem involves finding the number of families (`a`) in the city based on the given conditions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
excess = 4  # 鹿不盡四 (excess when 72 families share)
deficit = 20  # 鹿不足二十 (deficit when 90 families share)
families_with_excess = 72  # 七十二家
families_with_deficit = 90  # 九十家

# Using the method described:
# 实 = (families_with_excess * deficit) + (families_with_deficit * excess)
# 法 = excess + deficit
# a = 实 / 法

实 = (families_with_excess * deficit) + (families_with_deficit * excess)
法 = excess + deficit
a = Fraction(实, 法)

# The result
a  # Number of families in the city
#----- content ends here -----


"""


### Explanation:
1. **实 (Numerator)**: Multiply the number of families with excess by the deficit, and add the product of the number of families with deficit by the excess.
2. **法 (Denominator)**: Add the excess and deficit.
3. **a**: Divide 实 by 法 to get the number of families.

The variable `a` will contain the number of families in the city as a `Fraction`.
"""


"""
"""
