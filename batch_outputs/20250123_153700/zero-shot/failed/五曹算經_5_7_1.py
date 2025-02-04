"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""
To solve this problem, we will calculate the value of one丈 (zhang), one尺 (chi), and one寸 (cun) based on the given information. Here's the Python code:


"""


from fractions import Fraction

# Given data
total_value = 8  # 8貫
total_length_in_chi = 40  # 40尺 in one bolt of silk

# Calculations
b = Fraction(total_value * 1000, total_length_in_chi)  # 1尺 (chi) value in 文
a = b * 10  # 1丈 (zhang) = 10尺
c = b / 10  # 1寸 (cun) = 1/10尺

# Results
a  # Value of 1丈 in 貫文
b  # Value of 1尺 in 文
c  # Value of 1寸 in 文


"""


### Explanation:
1. The total value of the bolt of silk is 8貫, and the total length is 40尺.
2. To find the value of 1尺 (b), divide the total value (in 文) by the total length in 尺. Since 1貫 = 1000文, we multiply the total value by 1000 to convert it to 文.
3. To find the value of 1丈 (a), multiply the value of 1尺 by 10 (since 1丈 = 10尺).
4. To find the value of 1寸 (c), divide the value of 1尺 by 10 (since 1尺 = 10寸).

### Final Results:
- `a = 2貫文` (value of 1丈)
- `b = 200文` (value of 1尺)
- `c = 20文` (value of 1寸)
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 2000"""
