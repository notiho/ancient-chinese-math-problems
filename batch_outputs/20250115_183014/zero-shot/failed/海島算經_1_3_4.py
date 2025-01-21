"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the depth of a valley ("谷深") based on the given measurements. Here's the solution:


"""


from fractions import Fraction

# Given data
句高 = Fraction(6)  # 6尺
下股 = Fraction(9) + Fraction(1, 10)  # 9尺1寸 (1寸 = 1/10尺)
上股 = Fraction(8) + Fraction(5, 10)  # 8尺5寸 (5寸 = 5/10尺)
矩間 = Fraction(30)  # 3丈 (1丈 = 10尺)

# Calculation
實 = 矩間 * 上股  # 矩間乘以上股
法 = 下股 - 上股  # 上股與下股相減
谷深 = 實 / 法  # 實除以法
谷深 = 谷深 - 句高  # 用句高減去所得

# Result
a = 谷深  # 谷深 in 丈


"""


### Explanation of the Code:
1. **Input Conversion**: All measurements are converted into fractions to handle non-integer values (e.g., 9尺1寸 = 9 + 1/10).
2. **Formula Application**: The formula from the problem is directly translated into Python:
   - Multiply the distance between the two measuring tools ("矩間") by the upper leg ("上股").
   - Subtract the lower leg ("下股") from the upper leg to get the divisor ("法").
   - Divide the product ("實") by the divisor ("法") to get the intermediate depth.
   - Subtract the height of the measuring tool ("句高") to get the final depth of the valley.
3. **Output**: The result is stored in the variable `a`, representing the depth of the valley in 丈.

### Units:
- 1 丈 = 10 尺
- 1 尺 = 10 寸

The variable `a` will contain the depth of the valley in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 419/10, Actual: 419"""
