"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a series of geometric measurements using right triangles and proportions to calculate the height of the tower ("樓高"). Let's compute the solution step by step.

Here is the Python code:


"""


from fractions import Fraction

# Given data
句高 = Fraction(6, 10)  # 6尺 = 6/10丈
下股 = Fraction(12, 10)  # 1丈2尺 = 12/10丈
矩間 = Fraction(3, 1)  # 3丈
上股 = Fraction(11, 10) + Fraction(4, 100)  # 1丈1尺4寸 = 11/10 + 4/100丈
入小表 = Fraction(8, 100)  # 8寸 = 8/100丈

# Step 1: Calculate the difference between 上股 and 下股
上下股相減 = 上股 - 下股

# Step 2: Multiply 矩間 by 句高
矩間乘句高 = 矩間 * 句高

# Step 3: Divide the result by 上下股相減
法 = 矩間乘句高 / 上下股相減

# Step 4: Multiply the result by 入小表
實 = 法 * 入小表

# Step 5: The result is the height of the tower
a = 實

# The height of the tower (樓高) is stored in variable 'a'


"""


The variable `a` now contains the height of the tower in 丈 (zhang).
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: -12/5"""
