"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the depth of a valley ("谷深") based on the given measurements. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(6, 1)  # 6尺
下股 = Fraction(9, 1) + Fraction(1, 10)  # 9尺1寸 (1寸 = 1/10尺)
矩間 = Fraction(30, 1)  # 3丈 (1丈 = 10尺)
上股 = Fraction(8, 1) + Fraction(5, 10)  # 8尺5寸 (5寸 = 5/10尺)

# Calculation
實 = 矩間 * 上股  # 矩間乘以上股
法 = 下股 - 上股  # 下股減去上股
谷深 = 實 / 法  # 實除以法
谷深 = 谷深 - 句高  # 所得減去句高

# Convert to 丈
a = 谷深 / Fraction(10, 1)  # 1丈 = 10尺

# Result
a
#----- content ends here -----


"""


The result will be stored in the variable `a`, which represents the depth of the valley in 丈.
"""


"""
"""
