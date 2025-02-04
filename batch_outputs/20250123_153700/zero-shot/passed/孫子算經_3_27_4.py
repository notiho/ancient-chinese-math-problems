"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves finding the number of families (`a`) in a city based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given values
excess = 4  # 鹿不盡四 (excess when 72 families share)
deficit = 20  # 鹿不足二十 (deficit when 90 families share)
families_1 = 72  # 假令七十二家
families_2 = 90  # 令之九十家

# Calculation using the method described
numerator = (families_1 * deficit) + (families_2 * excess)  # 維乘之所得并為實
denominator = excess + deficit  # 並盈不足為法

# Compute the number of families
a = Fraction(numerator, denominator)

# Result
a  # This is the number of families


"""


The variable `a` will contain the solution as a `Fraction`.
"""


"""
"""
