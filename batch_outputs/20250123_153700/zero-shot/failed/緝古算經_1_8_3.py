"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
求圓囤上下周及高，術曰：以斛法乘容粟，又三十六乘之，三而一，為方亭之積。又以周差自乘，三而一，為隅陽冪。以乘截高，以減亭積，余為實。又周差乘截高，加隅陽冪，為方法。又以周差加截高，為廉法，從。開立方除之，得上周。加差，而合所問。求粟去口，術曰：以斛法乘出斛，三十六乘之，以乘高冪，如周差冪而一，為實。高乘上周，周差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，即去口。置去口，以周差乘之，以本高除之，所得加上周，即粟周。
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves calculating the upper circumference (`a`), lower circumference (`b`), height (`c`), remaining grain height (`d`), and grain circumference (`e`). The solution uses the `Fraction` class to handle non-integer values.

Here is the Python code:


"""


from fractions import Fraction

# Given values
斛法 = Fraction(2, 5)  # 2尺5寸 = 2.5尺
容粟 = Fraction(7005, 10)  # 700斛6斗 = 700.6斛
已運出 = Fraction(2664, 10)  # 266石4斗 = 266.4石 = 266.4斛
周差 = Fraction(12, 1)  # 1丈2尺 = 12尺
高多上周 = Fraction(18, 1)  # 1丈8尺 = 18尺

# Step 1: Compute the height (c), upper circumference (a), and lower circumference (b)
亭積 = 斛法 * 容粟 * 36 / 3  # 方亭之積
隅陽冪 = (周差 ** 2) / 3  # 隅陽冪
截高 = 高多上周 + 周差  # 截高
實 = 亭積 - 隅陽冪 * 截高  # 實
方法 = 隅陽冪 + 周差 * 截高  # 方法
廉法 = 周差 + 截高  # 廉法
a = (實 / 方法) ** Fraction(1, 3) * 廉法  # 上周
b = a - 周差  # 下周
c = 高多上周 + a  # 高

# Step 2: Compute the remaining grain height (d) and grain circumference (e)
去口實 = 斛法 * 已運出 * 36  # 去口實
小高 = c * a / 周差  # 小高
方法_去口 = (小高 ** 2) / 3  # 方法 for 去口
廉法_去口 = 3 * 小高  # 廉法 for 去口
d = (去口實 / 方法_去口) ** Fraction(1, 3) * 廉法_去口  # 去口
e = d * 周差 / c + a  # 粟周

# Results
a = a / 10  # Convert to 丈
b = b / 10  # Convert to 丈
c = c / 10  # Convert to 丈
d = d / 10  # Convert to 丈
e = e / 10  # Convert to 丈

# Output the results
a, b, c, d, e


"""


### Explanation of Variables:
1. `a`: Upper circumference (上周) in 丈.
2. `b`: Lower circumference (下周) in 丈.
3. `c`: Height (高) in 丈.
4. `d`: Remaining grain height (去口) in 丈.
5. `e`: Grain circumference (粟周) in 丈.

### Notes:
- The `斛法` is given in 尺, so all calculations are initially in 尺. The final results are converted to 丈 by dividing by 10.
- The `Fraction` class ensures precise calculations for non-integer values.
- The steps follow the ancient Chinese mathematical procedure described in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 7.041153658065246
Variable 'b' has wrong value. Expected: 3, Actual: 5.841153658065247
Variable 'c' has wrong value. Expected: 18/5, Actual: 8.841153658065247
Variable 'd' has wrong value. Expected: 9/5, Actual: 54.423242769317696
Variable 'e' has wrong value. Expected: 12/5, Actual: 14.427960159681112"""
