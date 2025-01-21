"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the height of a building (楼高) using geometric relationships and measurements. Here's the Python code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(6, 10)  # 6尺 = 0.6丈
下股 = Fraction(12, 10)  # 1丈2尺 = 1.2丈
矩间 = Fraction(3, 1)  # 3丈
上股 = Fraction(11, 10) + Fraction(4, 100)  # 1丈1尺4寸 = 1.14丈
入小表 = Fraction(8, 100)  # 8寸 = 0.08丈

# Step-by-step calculations
上下股相减 = 上股 - 下股  # 上下股相减
法 = 上下股相减  # 法 = 上下股相减
句高而一 = 句高 * 矩间  # 句高而一
所得 = 句高而一 * 入小表  # 所得 = 句高而一 * 入小表
楼高 = 所得 / 法  # 楼高 = 所得 / 法

# Result
a = 楼高  # Assign the result to variable "a"
a


"""


The variable `a` will contain the height of the building in 丈 (zhang).
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: -12/5"""
