"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the height of a tower (楼高) based on measurements involving a mountain, a ruler, and angles of observation. The solution will follow the steps described in the problem.

Here is the Python code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(6, 10)  # 6尺 = 6/10丈
下股 = Fraction(12, 10)  # 1丈2尺 = 12/10丈
矩間 = Fraction(30, 10)  # 3丈
上股 = Fraction(11.4, 10)  # 1丈1尺4寸 = 11.4/10丈
入小表 = Fraction(8, 100)  # 8寸 = 8/100丈

# Step 1: Calculate the difference between 上股 and 下股
上下股相減 = 上股 - 下股

# Step 2: Multiply 矩間 by 句高 and divide by 上下股相減
法 = 矩間 * 句高 / 上下股相減

# Step 3: Multiply the result by 入小表 to get the 实 (result)
實 = 法 * 入小表

# Step 4: The result is the height of the tower (楼高)
a = 實

# Output the result
a


"""


The variable `a` will contain the height of the tower in 丈 (zhang).
"""


"""
Code error: both arguments should be Rational instances"""
