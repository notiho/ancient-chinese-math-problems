"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the depth of a valley (谷深) based on measurements using two poles (偃矩). Let's compute the depth of the valley step by step.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = Fraction(6, 1)  # 6尺
下股 = Fraction(9, 1) + Fraction(1, 10)  # 9尺1寸 (1寸 = 1/10尺)
上股 = Fraction(8, 1) + Fraction(5, 10)  # 8尺5寸 (5寸 = 5/10尺)
矩間 = Fraction(3, 1) * 10  # 3丈 (1丈 = 10尺)

# Calculation
實 = 矩間 * 上股  # 矩間 multiplied by 上股
法 = 下股 - 上股  # 下股 minus 上股
谷深 = 實 / 法  # Divide 實 by 法
谷深 = 谷深 - 句高  # Subtract 句高 from the result

# Convert to 丈 (1丈 = 10尺)
a = 谷深 / 10  # Final depth in 丈

# Output the result
a
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The given measurements are converted into fractions. The units are in 尺 (chi), where 1丈 (zhang) = 10尺, and 1寸 (cun) = 1/10尺.
2. **Calculation**:
   - `實` is the product of 矩間 (distance between the poles) and 上股 (upper pole measurement).
   - `法` is the difference between 下股 (lower pole measurement) and 上股.
   - The depth of the valley (谷深) is calculated as `實 / 法`, and then the height of the pole (句高) is subtracted.
3. **Conversion**: The result is converted from 尺 to 丈 by dividing by 10.
4. **Output**: The final depth of the valley is stored in the variable `a`.

### Result:
The variable `a` will contain the depth of the valley in 丈.
"""


"""
"""
