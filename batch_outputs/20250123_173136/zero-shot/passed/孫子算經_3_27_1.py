"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves finding the number of families (`a`) in the city based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given values
excess = 4  # 鹿不盡四
deficit = 20  # 鹿不足二十
families1 = 72  # 七十二家
families2 = 90  # 九十家

# Calculation based on the method described
numerator = (families1 * deficit) + (families2 * excess)  # 維乘之所得并為實
denominator = excess + deficit  # 並盈不足為法
a = Fraction(numerator, denominator)  # 除之，即得

# Result
a  # 城中家數


"""


The variable `a` will contain the number of families in the city as a `Fraction`.
"""


"""
"""
